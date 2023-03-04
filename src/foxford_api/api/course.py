from typing import List

from fastapi import APIRouter, Depends

from models.Course import (
    Course, CourseCreate, CourseUpdate
)
from services.Course import CourseService

router = APIRouter(
    prefix='/course',
    tags=['Course']
)


@router.get('/courses')
def get_courses(service: CourseService = Depends()):
    for course in service.get_list():
        print(course)
    return service.get_list()


@router.get('/courses/{course_id}', response_model=Course)
def get_course_by_id(course_id: int,
                     service: CourseService = Depends()):
    return service._get(course_id=course_id)


@router.post('/create', response_model=Course)
def create_Course(course_data: CourseCreate,
                  service: CourseService = Depends()):
    """
    Creating Course
    """
    return service.create(course_data=course_data)


@router.put('/{course_id}', response_model=Course)
def update_course(
        course_id: int,
        course_data: CourseUpdate,
        service: CourseService = Depends(),
):
    return service.update(course_id=course_id, course_data=course_data)


@router.delete('/{course_id}')
def delete_course(course_id: int,
                  service: CourseService = Depends(),
                  ):
    return service.delete(course_id=course_id)
