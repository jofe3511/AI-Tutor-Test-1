from pydantic import BaseModel


class CourseSummary(BaseModel):
    id: str
    title: str
    term: str
    status: str
