#!./venv/bin/python
""" Running Application """
import uvicorn
from dynasty.models.v1 import users
from dynasty.models.schema import users as schema
from dynasty.database.database import engine

users.Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run("dynasty.api:app", host="0.0.0.0", port=8000, reload=True)
