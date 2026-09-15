# Build Order

This is the recommended order for turning the prototype into a real app.

## 1. Backend skeleton

Create the basic FastAPI server and route folders.

Goal: the app has a real API server, even if most endpoints return sample data at first.

## 2. Database models

Define PostgreSQL tables for users, courses, concepts, questions, attempts, mastery, documents, and assessments.

Goal: the backend has a clear source of truth.

## 3. Course structure

Build course, module, topic, concept, and learning objective records.

Goal: the tutor can understand what a course teaches.

## 4. Knowledge layer

Add document upload, text extraction, chunking, embeddings, vector search, and citations.

Goal: the tutor can answer from professor-approved material.

## 5. AI model adapter

Create one interface for model calls, then connect the first provider.

Goal: the app can use an LLM without locking the whole project to one model company.

## 6. Student model and mastery

Track concept mastery, confidence, attempts, recent performance, and last practiced date.

Goal: the tutor knows what each student understands.

## 7. Tutor engine

Combine course knowledge, student mastery, teaching strategy, difficulty, and AI responses.

Goal: the app becomes an adaptive tutor instead of a chatbot.

## 8. Practice and assessment

Generate questions, grade answers, log attempts, update mastery, and show immediate feedback.

Goal: students can practice and professors can review generated assessments.

## 9. React frontend

Replace the static prototype with a React or Next.js frontend that talks to the backend.

Goal: the user interface becomes a real app connected to data.

## 10. Instructor review workflow

Add approval, editing, replacement, and steering tools for professors and TAs.

Goal: high-stakes AI output stays auditable and instructor-controlled.
