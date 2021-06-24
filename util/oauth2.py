from fastapi          import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from util             import tokens

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user(token_data: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail      = "Could not validate credentials",
        headers     = {"WWW-Authenticate": "Bearer"},
    )

    return tokens.verify_token(token_data, credentials_exception)
