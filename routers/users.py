from fastapi        import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session

from util           import hashing, validation
import database, schemas, models

router = APIRouter(
    prefix = "/users",
    tags   = ["users"]
)
get_db = database.get_db

@router.post("/signup", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def signup(data: schemas.UserIn, db: Session = Depends(get_db)):

    if not validation.validate_email(data.email):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="invalid_email")

    if not validation.validate_password(data.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="invalid_password")

    if not validation.validate_duplication(data.email):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="existing_user")


    # delete inactive user

    user = models.User(email=data.email, password=hashing.bcrypt(data.password))

    print(user.password)
    return user 

