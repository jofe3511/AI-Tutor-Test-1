from pydantic import BaseModel


class MasterySummary(BaseModel):
    student_id: str
    course_id: str
    course_mastery: float
    concept_mastery: dict[str, float]
