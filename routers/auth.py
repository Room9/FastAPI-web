from fastapi           import HTTPException, status, APIRouter, Depends
from fastapi.security  import OAuth2PasswordRequestForm
from fastapi.responses import RedirectResponse
from sqlalchemy.orm    import Session

from util              import hashing, tokens, aes256
from my_settings       import SECRET, EMAIL
import database, models

router = APIRouter(
    prefix = "/auth",
    tags   = ["auth"]
)
get_db = database.get_db


@router.post('/login', status_code=status.HTTP_201_CREATED)
def login(request: OAuth2PasswordRequestForm = Depends(), db:Session= Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first() 

    if not user:
       raise HTTPException(
               status_code=status.HTTP_404_NOT_FOUND, 
               detail="Invalid credentials"
        )

    if not hashing.verify(user.password, request.password):
       raise HTTPException(
               status_code=status.HTTP_400_BAD_REQUEST, 
               detail="Incorrect password"
        )

    if not user.is_active:
       raise HTTPException(
               status_code=status.HTTP_400_BAD_REQUEST,
               detail="inactive user"
        )
   
    user_id      = aes256.AESCipher(bytes(SECRET['AES_KEY'])).encrypt(str(user.id)).decode('utf-8')
    data         = {"sub": user_id}
    access_token = tokens.create_token(data)

    return {"access_token": access_token, "token_type": "bearer"}

@router.get('/email/{uid}/{hashed}', status_code=status.HTTP_200_OK)
def authorize_email(uid: str, hashed: str, db: Session = Depends(get_db)):
    user_id     = aes256.AESCipher(bytes(SECRET['AES_KEY'])).decrypt(uid).decode('utf-8')
    user        = db.query(models.User).filter(models.User.id == user_id).first()
    user_hashed = hashing.create_hash(str(user.id), user.email).decode()

    if user_hashed != hashed:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail = "something's wrong.."
        )

    db.query(models.User).filter(models.User.id == user_id).update({'is_active': True})
    db.commit()

    return RedirectResponse(EMAIL['REDIRECT_URL'])
