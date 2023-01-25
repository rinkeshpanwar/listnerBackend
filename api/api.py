from fastapi import APIRouter
from api import test, auth
api_router = APIRouter()

# add the api router to the main app

api_router.include_router(test.router, prefix="/test", tags=["test"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])