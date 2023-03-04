from enum import Enum

import datetime as dt
from pydantic import BaseModel


class StatusEnum(str, Enum):
    CREATED = 'created'
    NOW = 'now'
    FINISHED = 'finished'
    CANCELLED = 'cancelled'


class BaseWebinar(BaseModel):
    planned_time: dt.datetime
    name: str
    status: StatusEnum = StatusEnum.CREATED
    duration: int  # hours
    course_id: int


class WebinarCreate(BaseWebinar):
    pass


class WebinarUpdate(BaseWebinar):
    pass


class Webinar(BaseWebinar):
    id: int

    class Config:
        orm_mode = True
