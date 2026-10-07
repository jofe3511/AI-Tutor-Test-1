from typing import Protocol


class AIModelProvider(Protocol):
    def generate_explanation(self, prompt: str) -> str:
        """Generate a student-facing explanation."""

    def generate_question(self, concept_id: str, difficulty: float) -> str:
        """Generate a practice or assessment question."""

    def evaluate_answer(self, question: str, answer: str) -> dict[str, object]:
        """Evaluate a student answer and return structured feedback."""
