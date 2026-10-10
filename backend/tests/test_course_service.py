from backend.courses.schemas import ConceptCreate, CourseCreate, LearningObjectiveCreate, ModuleCreate, TopicCreate
from backend.courses.service import get_demo_course_outline, preview_course_outline


def test_demo_course_outline_has_concepts_and_objectives() -> None:
    outline = get_demo_course_outline("course_demo_bio301")

    assert outline.modules
    assert outline.modules[0].topics
    assert outline.modules[0].topics[0].concepts
    assert outline.modules[0].topics[0].concepts[0].learning_objectives


def test_preview_course_outline_preserves_nested_structure() -> None:
    outline = preview_course_outline(
        CourseCreate(
            code="CHEM 201",
            title="Organic Chemistry",
            term="Fall",
            modules=[
                ModuleCreate(
                    title="Bonding",
                    position=1,
                    topics=[
                        TopicCreate(
                            title="Hybridization",
                            position=1,
                            concepts=[
                                ConceptCreate(
                                    title="sp3 hybridization",
                                    difficulty=0.4,
                                    learning_objectives=[
                                        LearningObjectiveCreate(
                                            objective="Identify sp3 hybridized atoms.",
                                            bloom_level="Apply",
                                        )
                                    ],
                                )
                            ],
                        )
                    ],
                )
            ],
        )
    )

    assert outline.code == "CHEM 201"
    assert outline.modules[0].topics[0].concepts[0].title == "sp3 hybridization"
