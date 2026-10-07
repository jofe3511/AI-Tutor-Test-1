from fastapi import APIRouter

from backend.assessments.schemas import AssessmentPreview

router = APIRouter()


@router.get("/preview", response_model=AssessmentPreview)
def assessment_preview() -> AssessmentPreview:
    return AssessmentPreview(
        course_id="course_demo_bio301",
        question_count=5,
        approval_required=True,
        question_types=["multiple_select", "matching", "short_answer", "process_ordering"],
    )
