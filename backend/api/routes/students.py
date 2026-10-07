from fastapi import APIRouter

from backend.students.schemas import MasterySummary

router = APIRouter()


@router.get("/{student_id}/mastery", response_model=MasterySummary)
def get_student_mastery(student_id: str) -> MasterySummary:
    return MasterySummary(
        student_id=student_id,
        course_id="course_demo_bio301",
        course_mastery=0.68,
        concept_mastery={
            "Glycolysis": 0.82,
            "Krebs Cycle": 0.61,
            "Electron Transport": 0.43,
            "ATP Production": 0.52,
        },
    )
