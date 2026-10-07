from fastapi import APIRouter

from backend.courses.schemas import CourseSummary

router = APIRouter()


@router.get("", response_model=list[CourseSummary])
def list_courses() -> list[CourseSummary]:
    return [
        CourseSummary(
            id="course_demo_bio301",
            title="BIO 301: Cell Systems",
            term="Demo term",
            status="prototype",
        )
    ]
