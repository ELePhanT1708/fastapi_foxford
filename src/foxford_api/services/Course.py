from typing import List

from fastapi import Depends, HTTPException, status, Response

import tables
from db import Session, get_session
from models.Course import CourseUpdate, CourseCreate, Course


class CourseService:

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, course_id: int) -> tables.Course:
        course = self.session.query(tables.Course)\
            .filter_by(id=course_id)\
            .first()
        if not course:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return course

    def get_list(self) -> List[tables.Course]:
        courses = self.session.query(tables.Course).all()
        return courses

    def create(self, course_data: CourseCreate) -> tables.Course:
        course = tables.Course(**course_data.dict())
        self.session.add(course)
        self.session.commit()
        return course

    def update(self, course_id: int, course_data: CourseUpdate) -> tables.Course:
        course = self._get(course_id)
        for key, value in course_data:
            setattr(course, key, value)
        self.session.commit()
        return course

    def delete(self, course_id: int) -> None:
        course = self._get(course_id)
        self.session.delete(course)
        self.session.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)