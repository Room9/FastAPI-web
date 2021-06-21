from enum import Enum

from pydantic import BaseModel

class LanguageName(str, Enum):
    korean  = "kor"
    english = "eng"

class TextOut(BaseModel):
    text : str
    section_number : int
    class Config():
        orm_mode = True

class ImageOut(BaseModel):
    directory : str
    section_number : int
    class Config():
        orm_mode = True
