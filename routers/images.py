from fastapi        import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from models         import Position, Image
import database, schemas

router = APIRouter(
    prefix = "/images",
    tags   = ["images"]
)
get_db = database.get_db


@router.get("/{component_number}", status_code=status.HTTP_200_OK, response_model=schemas.ImageOut)
def get_images(component_number: int, db: Session = Depends(get_db)):
    contents = db.query(Image).join(Position).filter(Position.component_number==component_number).all()
    
    if not contents:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail = f"component_number {component_number} is invalid"
        )

    results = [
            {
                'directory'      : content.directory,
                'section_number' : content.positions.section_number
            } for content in contents ]

    return results
