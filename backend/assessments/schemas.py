from pydantic import BaseModel


class AssessmentPreview(BaseModel):
    course_id: str
    question_count: int
    approval_required: bool
    question_types: list[str]
