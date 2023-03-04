from typing import Optional

from pydantic import BaseModel


class BaseParticipation(BaseModel):
    webinar_id: int
    teacher_id: int
    comment: Optional[str]


class ParticipationCreate(BaseParticipation):
    pass


class ParticipationUpdate(BaseParticipation):
    pass


class Participation(BaseParticipation):

    class Config:
        orm_mode = True
