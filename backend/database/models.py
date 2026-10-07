from __future__ import annotations

import enum
import uuid
from datetime import datetime
from typing import Any

from sqlalchemy import JSON, DateTime, Enum, ForeignKey, String, Text, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class UserRole(str, enum.Enum):
    student = "student"
    instructor = "instructor"
    ta = "ta"
    admin = "admin"


class EnrollmentRole(str, enum.Enum):
    student = "student"
    instructor = "instructor"
    ta = "ta"


class ApprovalStatus(str, enum.Enum):
    draft = "draft"
    pending_review = "pending_review"
    approved = "approved"
    rejected = "rejected"
    archived = "archived"


class QuestionType(str, enum.Enum):
    multiple_select = "multiple_select"
    matching = "matching"
    short_answer = "short_answer"
    multiple_choice = "multiple_choice"
    process_ordering = "process_ordering"


class AIOutputType(str, enum.Enum):
    explanation = "explanation"
    question = "question"
    evaluation = "evaluation"
    summary = "summary"


def new_uuid() -> str:
    return str(uuid.uuid4())


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )


class User(TimestampMixin, Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_uuid)
    email: Mapped[str] = mapped_column(String(320), unique=True, index=True)
    full_name: Mapped[str] = mapped_column(String(200))
    role: Mapped[UserRole] = mapped_column(Enum(UserRole), index=True)

    enrollments: Mapped[list[Enrollment]] = relationship(back_populates="user")
    tutor_sessions: Mapped[list[TutorSession]] = relationship(back_populates="student")


class Course(TimestampMixin, Base):
    __tablename__ = "courses"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_uuid)
    code: Mapped[str] = mapped_column(String(50), index=True)
    title: Mapped[str] = mapped_column(String(200))
    term: Mapped[str] = mapped_column(String(100))
    configuration: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict)

    enrollments: Mapped[list[Enrollment]] = relationship(back_populates="course")
    modules: Mapped[list[Module]] = relationship(back_populates="course")
    documents: Mapped[list[Document]] = relationship(back_populates="course")
    assessments: Mapped[list[Assessment]] = relationship(back_populates="course")


class Enrollment(TimestampMixin, Base):
    __tablename__ = "enrollments"
    __table_args__ = (UniqueConstraint("user_id", "course_id", name="uq_user_course"),)

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_uuid)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"), index=True)
    course_id: Mapped[str] = mapped_column(ForeignKey("courses.id"), index=True)
    role: Mapped[EnrollmentRole] = mapped_column(Enum(EnrollmentRole), index=True)

    user: Mapped[User] = relationship(back_populates="enrollments")
    course: Mapped[Course] = relationship(back_populates="enrollments")


class Module(TimestampMixin, Base):
    __tablename__ = "modules"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_uuid)
    course_id: Mapped[str] = mapped_column(ForeignKey("courses.id"), index=True)
    title: Mapped[str] = mapped_column(String(200))
    position: Mapped[int] = mapped_column(default=0)

    course: Mapped[Course] = relationship(back_populates="modules")
    topics: Mapped[list[Topic]] = relationship(back_populates="module")


class Topic(TimestampMixin, Base):
    __tablename__ = "topics"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_uuid)
    module_id: Mapped[str] = mapped_column(ForeignKey("modules.id"), index=True)
    title: Mapped[str] = mapped_column(String(200))
    position: Mapped[int] = mapped_column(default=0)

    module: Mapped[Module] = relationship(back_populates="topics")
    concepts: Mapped[list[Concept]] = relationship(back_populates="topic")


class Concept(TimestampMixin, Base):
    __tablename__ = "concepts"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_uuid)
    topic_id: Mapped[str] = mapped_column(ForeignKey("topics.id"), index=True)
    title: Mapped[str] = mapped_column(String(200))
    description: Mapped[str | None] = mapped_column(Text)
    difficulty: Mapped[float] = mapped_column(default=0.5)
    prerequisites: Mapped[list[str]] = mapped_column(JSON, default=list)

    topic: Mapped[Topic] = relationship(back_populates="concepts")
    learning_objectives: Mapped[list[LearningObjective]] = relationship(back_populates="concept")
    mastery_states: Mapped[list[MasteryState]] = relationship(back_populates="concept")


class LearningObjective(TimestampMixin, Base):
    __tablename__ = "learning_objectives"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_uuid)
    concept_id: Mapped[str] = mapped_column(ForeignKey("concepts.id"), index=True)
    objective: Mapped[str] = mapped_column(Text)
    bloom_level: Mapped[str] = mapped_column(String(80))

    concept: Mapped[Concept] = relationship(back_populates="learning_objectives")


class Document(TimestampMixin, Base):
    __tablename__ = "documents"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_uuid)
    course_id: Mapped[str] = mapped_column(ForeignKey("courses.id"), index=True)
    uploaded_by_id: Mapped[str] = mapped_column(ForeignKey("users.id"), index=True)
    title: Mapped[str] = mapped_column(String(250))
    source_type: Mapped[str] = mapped_column(String(50))
    source_tier: Mapped[int] = mapped_column(default=1)
    storage_uri: Mapped[str | None] = mapped_column(String(500))

    course: Mapped[Course] = relationship(back_populates="documents")
    chunks: Mapped[list[DocumentChunk]] = relationship(back_populates="document")


class DocumentChunk(TimestampMixin, Base):
    __tablename__ = "document_chunks"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_uuid)
    document_id: Mapped[str] = mapped_column(ForeignKey("documents.id"), index=True)
    chunk_index: Mapped[int] = mapped_column(index=True)
    text: Mapped[str] = mapped_column(Text)
    chunk_metadata: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict)
    embedding_id: Mapped[str | None] = mapped_column(String(200), index=True)

    document: Mapped[Document] = relationship(back_populates="chunks")


class Question(TimestampMixin, Base):
    __tablename__ = "questions"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_uuid)
    course_id: Mapped[str] = mapped_column(ForeignKey("courses.id"), index=True)
    concept_id: Mapped[str] = mapped_column(ForeignKey("concepts.id"), index=True)
    question_type: Mapped[QuestionType] = mapped_column(Enum(QuestionType), index=True)
    prompt: Mapped[str] = mapped_column(Text)
    expected_answer: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict)
    grading_rubric: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict)
    explanation: Mapped[str | None] = mapped_column(Text)
    difficulty: Mapped[float] = mapped_column(default=0.5)
    bloom_level: Mapped[str] = mapped_column(String(80))
    source_references: Mapped[list[str]] = mapped_column(JSON, default=list)
    approval_status: Mapped[ApprovalStatus] = mapped_column(
        Enum(ApprovalStatus),
        default=ApprovalStatus.draft,
        index=True,
    )

    attempts: Mapped[list[QuestionAttempt]] = relationship(back_populates="question")


class QuestionAttempt(TimestampMixin, Base):
    __tablename__ = "question_attempts"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_uuid)
    question_id: Mapped[str] = mapped_column(ForeignKey("questions.id"), index=True)
    student_id: Mapped[str] = mapped_column(ForeignKey("users.id"), index=True)
    answer: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict)
    correct: Mapped[bool] = mapped_column(default=False)
    score: Mapped[float] = mapped_column(default=0.0)
    feedback: Mapped[str | None] = mapped_column(Text)
    time_taken_seconds: Mapped[int | None] = mapped_column()

    question: Mapped[Question] = relationship(back_populates="attempts")


class Assessment(TimestampMixin, Base):
    __tablename__ = "assessments"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_uuid)
    course_id: Mapped[str] = mapped_column(ForeignKey("courses.id"), index=True)
    title: Mapped[str] = mapped_column(String(250))
    question_count: Mapped[int] = mapped_column(default=5)
    approval_status: Mapped[ApprovalStatus] = mapped_column(
        Enum(ApprovalStatus),
        default=ApprovalStatus.pending_review,
        index=True,
    )
    settings: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict)

    course: Mapped[Course] = relationship(back_populates="assessments")
    questions: Mapped[list[AssessmentQuestion]] = relationship(back_populates="assessment")
    attempts: Mapped[list[AssessmentAttempt]] = relationship(back_populates="assessment")


class AssessmentQuestion(TimestampMixin, Base):
    __tablename__ = "assessment_questions"
    __table_args__ = (UniqueConstraint("assessment_id", "question_id", name="uq_assessment_question"),)

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_uuid)
    assessment_id: Mapped[str] = mapped_column(ForeignKey("assessments.id"), index=True)
    question_id: Mapped[str] = mapped_column(ForeignKey("questions.id"), index=True)
    position: Mapped[int] = mapped_column(default=0)

    assessment: Mapped[Assessment] = relationship(back_populates="questions")


class AssessmentAttempt(TimestampMixin, Base):
    __tablename__ = "assessment_attempts"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_uuid)
    assessment_id: Mapped[str] = mapped_column(ForeignKey("assessments.id"), index=True)
    student_id: Mapped[str] = mapped_column(ForeignKey("users.id"), index=True)
    score: Mapped[float] = mapped_column(default=0.0)
    submitted_at: Mapped[datetime | None] = mapped_column(DateTime)

    assessment: Mapped[Assessment] = relationship(back_populates="attempts")


class MasteryState(TimestampMixin, Base):
    __tablename__ = "mastery_states"
    __table_args__ = (UniqueConstraint("student_id", "concept_id", name="uq_student_concept_mastery"),)

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_uuid)
    student_id: Mapped[str] = mapped_column(ForeignKey("users.id"), index=True)
    concept_id: Mapped[str] = mapped_column(ForeignKey("concepts.id"), index=True)
    mastery_score: Mapped[float] = mapped_column(default=0.0)
    confidence: Mapped[float] = mapped_column(default=0.0)
    attempt_count: Mapped[int] = mapped_column(default=0)
    recent_performance: Mapped[float] = mapped_column(default=0.0)
    last_practiced_at: Mapped[datetime | None] = mapped_column(DateTime)
    strategy_version: Mapped[str] = mapped_column(String(80), default="simple_weighted_v1")

    concept: Mapped[Concept] = relationship(back_populates="mastery_states")


class TutorSession(TimestampMixin, Base):
    __tablename__ = "tutor_sessions"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_uuid)
    student_id: Mapped[str] = mapped_column(ForeignKey("users.id"), index=True)
    course_id: Mapped[str] = mapped_column(ForeignKey("courses.id"), index=True)
    active_concept_id: Mapped[str | None] = mapped_column(ForeignKey("concepts.id"))
    strategy: Mapped[str | None] = mapped_column(String(100))
    session_metadata: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict)

    student: Mapped[User] = relationship(back_populates="tutor_sessions")
    messages: Mapped[list[TutorMessage]] = relationship(back_populates="session")


class TutorMessage(TimestampMixin, Base):
    __tablename__ = "tutor_messages"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_uuid)
    session_id: Mapped[str] = mapped_column(ForeignKey("tutor_sessions.id"), index=True)
    sender: Mapped[str] = mapped_column(String(30))
    content: Mapped[str] = mapped_column(Text)
    citations: Mapped[list[str]] = mapped_column(JSON, default=list)

    session: Mapped[TutorSession] = relationship(back_populates="messages")


class InstructorFeedback(TimestampMixin, Base):
    __tablename__ = "instructor_feedback"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_uuid)
    course_id: Mapped[str] = mapped_column(ForeignKey("courses.id"), index=True)
    instructor_id: Mapped[str] = mapped_column(ForeignKey("users.id"), index=True)
    target_type: Mapped[str] = mapped_column(String(80))
    target_id: Mapped[str] = mapped_column(String(36), index=True)
    feedback: Mapped[str] = mapped_column(Text)


class AIOutput(TimestampMixin, Base):
    __tablename__ = "ai_outputs"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_uuid)
    course_id: Mapped[str | None] = mapped_column(ForeignKey("courses.id"))
    output_type: Mapped[AIOutputType] = mapped_column(Enum(AIOutputType), index=True)
    provider: Mapped[str] = mapped_column(String(80))
    model_name: Mapped[str] = mapped_column(String(120))
    prompt: Mapped[str] = mapped_column(Text)
    output: Mapped[str] = mapped_column(Text)
    output_metadata: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict)


class EvaluationResult(TimestampMixin, Base):
    __tablename__ = "evaluation_results"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_uuid)
    ai_output_id: Mapped[str] = mapped_column(ForeignKey("ai_outputs.id"), index=True)
    evaluator: Mapped[str] = mapped_column(String(120))
    passed: Mapped[bool] = mapped_column(default=False)
    score: Mapped[float | None] = mapped_column()
    notes: Mapped[str | None] = mapped_column(Text)
