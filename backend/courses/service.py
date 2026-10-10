from backend.courses.schemas import (
    ConceptRead,
    CourseCreate,
    CourseOutlineRead,
    CourseSummary,
    LearningObjectiveRead,
    ModuleRead,
    TopicRead,
)


def list_demo_courses() -> list[CourseSummary]:
    return [
        CourseSummary(
            id="course_demo_bio301",
            code="BIO 301",
            title="Cell Systems",
            term="Demo term",
            status="prototype",
        )
    ]


def get_demo_course_outline(course_id: str) -> CourseOutlineRead:
    return CourseOutlineRead(
        id=course_id,
        code="BIO 301",
        title="Cell Systems",
        term="Demo term",
        modules=[
            ModuleRead(
                id="module_cell_energy",
                title="Cell Energy",
                position=1,
                topics=[
                    TopicRead(
                        id="topic_respiration",
                        title="Cellular Respiration",
                        position=1,
                        concepts=[
                            ConceptRead(
                                id="concept_glycolysis",
                                title="Glycolysis",
                                description="How glucose is split and prepared for downstream ATP production.",
                                difficulty=0.35,
                                prerequisites=[],
                                learning_objectives=[
                                    LearningObjectiveRead(
                                        id="lo_glycolysis_steps",
                                        objective="Describe the major inputs and outputs of glycolysis.",
                                        bloom_level="Understand",
                                    )
                                ],
                            ),
                            ConceptRead(
                                id="concept_etc",
                                title="Electron Transport Chain",
                                description="How electron carriers and membrane gradients support ATP synthesis.",
                                difficulty=0.68,
                                prerequisites=["concept_glycolysis"],
                                learning_objectives=[
                                    LearningObjectiveRead(
                                        id="lo_nadh_atp",
                                        objective="Explain how NADH contributes to ATP production.",
                                        bloom_level="Apply",
                                    ),
                                    LearningObjectiveRead(
                                        id="lo_proton_gradient",
                                        objective="Distinguish proton pumping from ATP synthase activity.",
                                        bloom_level="Analyze",
                                    ),
                                ],
                            ),
                        ],
                    )
                ],
            )
        ],
    )


def preview_course_outline(payload: CourseCreate) -> CourseOutlineRead:
    modules: list[ModuleRead] = []
    for module_index, module in enumerate(payload.modules, start=1):
        topics: list[TopicRead] = []
        for topic_index, topic in enumerate(module.topics, start=1):
            concepts: list[ConceptRead] = []
            for concept_index, concept in enumerate(topic.concepts, start=1):
                objectives = [
                    LearningObjectiveRead(
                        id=f"preview_lo_{module_index}_{topic_index}_{concept_index}_{objective_index}",
                        objective=objective.objective,
                        bloom_level=objective.bloom_level,
                    )
                    for objective_index, objective in enumerate(concept.learning_objectives, start=1)
                ]
                concepts.append(
                    ConceptRead(
                        id=f"preview_concept_{module_index}_{topic_index}_{concept_index}",
                        title=concept.title,
                        description=concept.description,
                        difficulty=concept.difficulty,
                        prerequisites=concept.prerequisites,
                        learning_objectives=objectives,
                    )
                )
            topics.append(
                TopicRead(
                    id=f"preview_topic_{module_index}_{topic_index}",
                    title=topic.title,
                    position=topic.position,
                    concepts=concepts,
                )
            )
        modules.append(
            ModuleRead(
                id=f"preview_module_{module_index}",
                title=module.title,
                position=module.position,
                topics=topics,
            )
        )

    return CourseOutlineRead(
        id="preview_course",
        code=payload.code,
        title=payload.title,
        term=payload.term,
        modules=modules,
    )
