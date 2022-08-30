"""
Utils functions for token.
"""

import configparser

from datetime import datetime, timedelta
from jose import jwt
from pydantic import BaseModel

config = configparser.ConfigParser()
config.read('config.ini')


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, config['hash']['secret_key'], algorithm=config['hash']['algorithm'])
    return encoded_jwt