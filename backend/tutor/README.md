# Tutor Engine

The core tutoring decisions go here.

This layer answers: given the course content and this student's mastery, what should happen next?

Use this folder for:

- Tutor orchestrator
- Conversation manager
- Teaching strategy selector
- Difficulty adjustment
- Question generator coordination
- Answer evaluator coordination
- Feedback generation
- Mastery update triggers

The LLM should be called through `backend/ai`, not directly from everywhere.
