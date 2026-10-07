from fastapi import APIRouter

from backend.api.routes import assessments, courses, health, knowledge, students, tutor

api_router = APIRouter()

api_router.include_router(health.router, tags=["health"])
api_router.include_router(courses.router, prefix="/courses", tags=["courses"])
api_router.include_router(knowledge.router, prefix="/knowledge", tags=["knowledge"])
api_router.include_router(students.router, prefix="/students", tags=["students"])
api_router.include_router(tutor.router, prefix="/tutor", tags=["tutor"])
api_router.include_router(assessments.router, prefix="/assessments", tags=["assessments"])
