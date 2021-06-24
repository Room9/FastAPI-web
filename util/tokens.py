from datetime    import datetime, timedelta
from typing      import Optional

from jose        import JWTError, jwt

from my_settings import SECRET
import schemas


def create_token(data: dict, minutes: Optional[int] = None):

    expire_minutes = timedelta(minutes=minutes if minutes else SECRET['ACCESS_TOKEN_EXPIRE_MINUTES'])
    expired_at = datetime.utcnow() + expire_minutes
    data.update({"exp": expired_at})

    return jwt.encode(data, SECRET['KEY'], algorithm=SECRET['ALGORITHM'])

def verify_token(token:str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET['KEY'], algorithms=SECRET['ALGORITHM'])
        email = payload.get("sub")

        if email is None:
            raise credentials_exception

        return schemas.TokenData(email=email)

    except JWTError:
        raise credentials_exception
