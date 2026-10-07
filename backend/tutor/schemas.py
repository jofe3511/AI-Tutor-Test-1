from pydantic import BaseModel


class TutorDecisionRequest(BaseModel):
    student_id: str
    course_id: str
    message: str


class TutorDecisionResponse(BaseModel):
    student_id: str
    course_id: str
    selected_concept: str
    strategy: str
    difficulty: float
    source_tier: str
    next_activity: str
