from typing         import Optional, List

from fastapi        import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from models         import Position, KoreanText, EnglishText
import database, schemas

router = APIRouter(
    prefix = "/texts",
    tags   = ["texts"]
)
get_db = database.get_db


@router.get("/{component_number}", status_code=status.HTTP_200_OK, response_model=List[schemas.TextOut])
def get_texts(component_number: int, lan: Optional[schemas.LanguageName] = None, db: Session = Depends(get_db)):

    text_languages = { 
        None  : db.query(KoreanText),
        'kor' : db.query(KoreanText),
        'eng' : db.query(EnglishText)
    }

    contents = text_languages[lan].join(Position).filter(Position.component_number==component_number).all()

    if not contents:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail = f"component_number {component_number} is invalid"
        )

    results = [
            {
                'text'           : content.text,
                'section_number' : content.positions.section_number
            } for content in contents ]

    return results 
