from fastapi        import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session

from util           import hashing, validation, auth_email, oauth2
from models         import User
import database, schemas

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

    if not validation.validate_duplication(data.email, db):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="existing_user")

    inactive_user = db.query(User).filter(User.email==data.email)
    if inactive_user.first():
        inactive_user.delete(synchronize_session=False)

    new_user = User(email=data.email, password=hashing.bcrypt(data.password), is_active=False)
    db.add(new_user)

    db.commit()
    db.refresh(new_user)

    auth_email.google_mail(new_user)

    return new_user

@router.get('/me', response_model=schemas.UserOut)
def get_person(db: Session = Depends(get_db), current_user: schemas.TokenData = Depends(oauth2.get_current_user)):

    user = db.query(User).filter(User.email == current_user.email).first()

    return user

