from fastapi             import FastAPI
from fastapi.staticfiles import StaticFiles

from routers             import texts, images, users, auth
import models, database


models.Base.metadata.create_all(database.engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(texts.router)
app.include_router(images.router)
app.include_router(users.router)
app.include_router(auth.router)
