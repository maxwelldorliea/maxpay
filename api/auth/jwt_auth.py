#!/usr/bin/python3
"""Handle JWT"""
from jose import jwt, JWTError
from typing import Dict
from datetime import datetime, timedelta
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from models import storage
from models.user import User


def create_access_token(data: Dict, env: Dict) -> str:
    """Generate Access Token."""
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=int(env['JWT_TIME_TO_LIVE']))
    to_encode.update({'exp': expire})
    return jwt.encode(to_encode, env['JWT_SECRET'])


def decode_access_token(token: str, env: Dict) -> Dict:
    """Decode user access token."""
    try:
        user_data = jwt.decode(
                token, env['JWT_SECRET'], algorithms=env['JWT_ALGORITHM'])
        return user_data
    except JWTError:
        raise HTTPException(
                status.HTTP_401_UNAUTHORIZED,
                detail='Could not validate credentials',
                headers={'WWW-Authenticate': 'Bearer'})

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/sign_in")

def get_current_user(token: str=Depends(oauth2_scheme)) -> User:
    """Return login user."""
    data = decode_access_token(token, storage.env)
    user = storage.get(User, data['id'])
    if not user:
        raise HTTPException(
                status.HTTP_401_UNAUTHORIZED,
                detail='Could not validate credentials',
                headers={'WWW-Authenticate': 'Bearer'})
    return user
