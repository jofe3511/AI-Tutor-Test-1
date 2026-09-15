# AI Model Layer

The provider-independent LLM interface goes here.

This folder should not spread one model provider throughout the app.

Expected interface ideas:

- `generate_explanation()`
- `generate_question()`
- `evaluate_answer()`
- `classify_misconception()`
- `summarize_student_questions()`

Start with one provider, but keep the app ready to swap providers later.
