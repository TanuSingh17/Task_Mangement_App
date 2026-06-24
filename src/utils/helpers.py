from fastapi import Request, HTTPException, status, Depends
from sqlalchemy.orm import Session
from src.utils.settings import settings
import jwt
from src.user.models import UserModel
from src.utils.db import get_db
from jwt.exceptions import InvalidTokenError
from datetime import datetime, timedelta



def is_authenticated(request: Request, db: Session = Depends(get_db)):
    token = request.headers.get("authorization")
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is missing, Unauthorized access")
    token = token.split(" ")[-1]

    data = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
    user_id = data.get("_id")
    exp_time = data.get("exp")

    current_time = datetime.now().timestamp()
    if current_time > exp_time:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has expired")
    
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid user, Unauthorized access")
    return user