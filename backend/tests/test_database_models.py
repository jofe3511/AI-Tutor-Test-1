from backend.database.models import Base


def test_core_database_tables_are_declared() -> None:
    expected_tables = {
        "users",
        "courses",
        "enrollments",
        "modules",
        "topics",
        "concepts",
        "learning_objectives",
        "documents",
        "document_chunks",
        "questions",
        "question_attempts",
        "assessments",
        "assessment_questions",
        "assessment_attempts",
        "mastery_states",
        "tutor_sessions",
        "tutor_messages",
        "instructor_feedback",
        "ai_outputs",
        "evaluation_results",
    }

    assert expected_tables.issubset(set(Base.metadata.tables.keys()))
