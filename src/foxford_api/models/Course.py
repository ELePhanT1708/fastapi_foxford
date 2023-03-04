from enum import Enum

from pydantic import BaseModel


class LevelEnum(str, Enum):
    CHILD = 'for childrens'
    PUPIL = 'for pupils'
    STUDENT = 'for students'
    TEACHER = 'for teachers'


class BaseCourse(BaseModel):
    name: str
    duration: int
    level: LevelEnum
    price: float

    def __repr__(self):
        return f"< Course : {self.name} {self.level} duration: {self.duration} "


class CourseCreate(BaseCourse):
    pass


class CourseUpdate(BaseCourse):
    pass


class Course(BaseCourse):
    id: int

    class Config:
        orm_mode = True
