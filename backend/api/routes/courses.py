from fastapi import APIRouter

from backend.courses.schemas import CourseCreate, CourseOutlineRead, CourseSummary
from backend.courses.service import get_demo_course_outline, list_demo_courses, preview_course_outline

router = APIRouter()


@router.get("", response_model=list[CourseSummary])
def list_courses() -> list[CourseSummary]:
    return list_demo_courses()


@router.get("/{course_id}/outline", response_model=CourseOutlineRead)
def get_course_outline(course_id: str) -> CourseOutlineRead:
    return get_demo_course_outline(course_id)


@router.post("/outline/preview", response_model=CourseOutlineRead)
def create_course_outline_preview(payload: CourseCreate) -> CourseOutlineRead:
    return preview_course_outline(payload)
