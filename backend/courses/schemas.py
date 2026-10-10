from pydantic import BaseModel, Field


class CourseSummary(BaseModel):
    id: str
    code: str
    title: str
    term: str
    status: str


class LearningObjectiveRead(BaseModel):
    id: str
    objective: str
    bloom_level: str


class ConceptRead(BaseModel):
    id: str
    title: str
    description: str | None = None
    difficulty: float = Field(ge=0.0, le=1.0)
    prerequisites: list[str] = Field(default_factory=list)
    learning_objectives: list[LearningObjectiveRead] = Field(default_factory=list)


class TopicRead(BaseModel):
    id: str
    title: str
    position: int
    concepts: list[ConceptRead] = Field(default_factory=list)


class ModuleRead(BaseModel):
    id: str
    title: str
    position: int
    topics: list[TopicRead] = Field(default_factory=list)


class CourseOutlineRead(BaseModel):
    id: str
    code: str
    title: str
    term: str
    modules: list[ModuleRead] = Field(default_factory=list)


class LearningObjectiveCreate(BaseModel):
    objective: str
    bloom_level: str


class ConceptCreate(BaseModel):
    title: str
    description: str | None = None
    difficulty: float = Field(default=0.5, ge=0.0, le=1.0)
    prerequisites: list[str] = Field(default_factory=list)
    learning_objectives: list[LearningObjectiveCreate] = Field(default_factory=list)


class TopicCreate(BaseModel):
    title: str
    position: int = 0
    concepts: list[ConceptCreate] = Field(default_factory=list)


class ModuleCreate(BaseModel):
    title: str
    position: int = 0
    topics: list[TopicCreate] = Field(default_factory=list)


class CourseCreate(BaseModel):
    code: str
    title: str
    term: str
    modules: list[ModuleCreate] = Field(default_factory=list)
