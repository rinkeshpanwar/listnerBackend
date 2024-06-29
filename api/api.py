from fastapi import APIRouter
from api import test, auth, questions, answers, search,ai
api_router = APIRouter()

# add the api router to the main app

api_router.include_router(test.router, prefix="/health", tags=["health"])
api_router.include_router(auth.router, prefix="", tags=["auth"])
api_router.include_router(questions.router, prefix="/question", tags=["questions"])
api_router.include_router(answers.router, prefix="/answer", tags=["answers"])
api_router.include_router(search.router, prefix="/search", tags=["search"])
api_router.include_router(ai.router, prefix="/ai", tags=["ai"])