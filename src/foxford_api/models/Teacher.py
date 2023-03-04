from pydantic import BaseModel


class BaseTeacher(BaseModel):
    first_name: str
    last_name: str
    surname: str
    rate_per_hour: float

    def __repr__(self):
        return f'< Teacher : {self.first_name} {self.surname}' \
               f' {self.last_name}'


class TeacherCreate(BaseTeacher):
    pass


class TeacherUpdate(BaseTeacher):
    pass


class Teacher(BaseTeacher):
    id: int

    class Config:
        orm_mode = True
