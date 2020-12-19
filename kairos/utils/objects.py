import datetime as dt
from config import Config

import jwt

SECRET_KEY = Config.SECRET_KEY
ENCRYPTION_ALGO = Config.ENCRYPTION_ALGO
ACCESS_TOKEN_EXPIRE_MINUTES = Config.ACCESS_TOKEN_EXPIRE_MINUTES


class Token:
    @staticmethod
    def create_access_token(data, expires_delta=None):
        to_encode = data.copy()

        if expires_delta:
            expires_delta = dt.timedelta(minutes=expires_delta)
            expire = dt.datetime.utcnow() + expires_delta
        else:
            expire = dt.datetime.utcnow() + dt.timedelta(
                minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES)
            )
        to_encode.update({"exp": expire})
        print(to_encode)
        print(SECRET_KEY)
        print(ENCRYPTION_ALGO)
        encoded_jwt = jwt.encode(
            to_encode, SECRET_KEY, algorithm=ENCRYPTION_ALGO
        ).decode("utf-8")
        return encoded_jwt

    @staticmethod
    def decode(token):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ENCRYPTION_ALGO])
            return payload
        except jwt.PyJWTError as e:
            raise ValueError("Could not validate credentials.")
