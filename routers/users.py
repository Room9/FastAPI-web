from fastapi import APIRouter
import database

router = APIRouter(
    prefix = "/users",
    tags   = ["users"]
)
get_db = database.get_db
