# Courses

Course structure logic goes here.

Use this folder for:

- Courses
- Modules
- Topics
- Concepts
- Learning objectives
- Content blocks
- Course material ownership

This is how the platform stays content-agnostic across biology, chemistry, finance, psychology, and other subjects.

## Current starting point

`schemas.py` defines the course hierarchy contract:

```text
Course
  Module
    Topic
      Concept
        LearningObjective
```

`service.py` currently provides demo and preview functions. Later, these functions should read and write the real PostgreSQL models in `backend/database/models.py`.
