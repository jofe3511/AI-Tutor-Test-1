from fastapi import APIRouter

from backend.tutor.schemas import TutorDecisionRequest, TutorDecisionResponse

router = APIRouter()


@router.post("/decision", response_model=TutorDecisionResponse)
def create_tutor_decision(request: TutorDecisionRequest) -> TutorDecisionResponse:
    return TutorDecisionResponse(
        student_id=request.student_id,
        course_id=request.course_id,
        selected_concept="Electron Transport",
        strategy="hint_progression",
        difficulty=0.46,
        source_tier="professor_approved_course_material",
        next_activity="Short-answer practice question with cited course hints.",
    )
