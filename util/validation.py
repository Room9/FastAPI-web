import re

from sqlalchemy.orm import Session

from models         import User


def validate_email(email: str):
    regex = re.compile('^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*.[a-zA-Z]{2,3}$')

    if regex.match(email):
        return True
    return False

def validate_password(password: str):
    regexs = [
        re.compile(r'^(?=.*[a-zA-Z])(?=.*\d)[A-Za-z\d!@#$%^&*]{6,15}$'),
        re.compile(r'^(?=.*[a-zA-Z])(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{6,15}$'),
        re.compile(r'^(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{6,15}$')
    ]

    for regex in regexs:
        if regex.match(password):
            return True
    return False

def validate_duplication(email: str, db: Session):
    if db.query(User).filter(User.email==email, User.is_active==True).first():
        return False
    return True
