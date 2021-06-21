from fastapi import APIRouter
import database

router = APIRouter(
    prefix = "/auth",
    tags   = ["auth"]
)
get_db = database.get_db

