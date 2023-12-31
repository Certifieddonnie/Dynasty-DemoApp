from fastapi import Query, APIRouter, Depends, HTTPException, status
from sqlalchemy import text
from sqlalchemy.orm import Session

from dynasty.utils.utils import get_db
from dynasty.services.v1.users import get_current_user
from dynasty.models.schema.users import User
from dynasty.configs.config import HEADERS
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/all/", status_code=status.HTTP_200_OK, tags=["fruits"])
async def get_all_fruits(skip: int = 0, limit: int = 10, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    """ Get all fruits """
    if current_user:
        query = text("SELECT * FROM fruits LIMIT :limit OFFSET :skip")
        results = db.execute(query, {"limit": limit, "skip": skip}).fetchall()
        fruits = [{'id': result[0], 'name': result[1],
                   'botanical_name': result[2],
                   'vitamin': result[3],
                   'benefits': result[4], 'side_effects': result[5],
                   'ph': result[6], 'preservation_methods': result[7]} for result in results]
        custom_data = {"fruits": fruits, "total": len(fruits), "skip": skip, "limit": limit}
        return JSONResponse(content=custom_data, headers=HEADERS)
    HEADERS["WWW-Authenticate"] = "Bearer"
    raise HTTPException(status_code=404, detail="User not found", headers=HEADERS)


@router.get("/search/", status_code=status.HTTP_200_OK, tags=["fruits"])
async def search_fruits(q: str = Query(None, min_length=2, max_length=50), current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    """ Search for a fruit """
    if current_user:
        query = text("SELECT * FROM fruits WHERE fruits LIKE :q")
        results = db.execute(query, {"q": f"%{q}%"}).fetchall()
        fruits = [{'id': result[0], 'name': result[1],
                   'botanical_name': result[2],
                   'vitamin': result[3],
                   'benefits': result[4], 'side_effects': result[5],
                   'ph': result[6], 'preservation_methods': result[7]} for result in results]

        if len(fruits) == 0:
            HEADERS["WWW-Authenticate"] = "Bearer"
            raise HTTPException(status_code=404, detail="Fruit not found", headers=HEADERS)
        custom_data = {"fruits": fruits, "total": len(fruits)}
        return JSONResponse(content=custom_data, headers=HEADERS)
    HEADERS["WWW-Authenticate"] = "Bearer"
    raise HTTPException(status_code=404, detail="User not found", headers=HEADERS)
