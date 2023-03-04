from typing import List

from fastapi import Depends, HTTPException, status, Response

import tables
from db import Session, get_session
from models.Teacher import TeacherCreate, TeacherUpdate
from services.Webinar import WebinarService


class TeacherService:

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, teacher_id: int) -> tables.Teacher:
        teacher = self.session.query(tables.Teacher) \
            .filter_by(id=teacher_id) \
            .first()
        if not teacher:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return teacher

    def get_list(self) -> List[tables.Teacher]:
        teachers = self.session.query(tables.Teacher).all()
        return teachers

    def get_salary(self,
                   teacher_id: int) \
            -> float:
        teacher = self._get(teacher_id)
        # work time for teacher
        hours = 0
        service = WebinarService()
        for webinar in teacher.webinars:
            hours += self.session.query(tables.Webinar) \
                .filter_by(id=webinar.webinar_id) \
                .first().duration
        salary = teacher.rate_per_hour * hours
        return salary

    def create(self, teacher_data: TeacherCreate) -> tables.Teacher:
        teacher = tables.Teacher(**teacher_data.dict())
        self.session.add(teacher)
        self.session.commit()
        return teacher

    def update(self, teacher_id: int, teacher_data: TeacherUpdate) -> tables.Teacher:
        teacher = self._get(teacher_id)
        for key, value in teacher_data:
            setattr(teacher, key, value)
        self.session.commit()
        return teacher

    def delete(self, user_id: int, post_id: int) -> None:
        post = self._get(user_id, post_id)
        self.session.delete(post)
        self.session.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
