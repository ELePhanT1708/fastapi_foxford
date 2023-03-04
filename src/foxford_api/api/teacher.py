from typing import List

from fastapi import APIRouter, Depends

from models.Teacher import (
    Teacher, TeacherCreate, TeacherUpdate
)
from services.Teacher import TeacherService

router = APIRouter(
    prefix='/teacher',
    tags=['Teacher']
)


@router.get('/teachers', response_model=List[Teacher])
def get_teachers(service: TeacherService = Depends()):
    return service.get_list()

@router.get('/salary/{teacher_id}')
def calculate_salary(teacher_id: int,
                     service: TeacherService = Depends()):
    return service.get_salary(teacher_id=teacher_id)


@router.post('/create', response_model=Teacher)
def create_teacher(teacher_data: TeacherCreate,
                   service: TeacherService = Depends()):
    """
    Creating teacher
    :param teacher_data: dict with data about teahcer
    :param service: util for separating logic and call
    :return:
    """
    return service.create(teacher_data=teacher_data)


@router.put('/{teacher_id}', response_model=Teacher)
def update_course(
        teacher_id: int,
        teacher_data: TeacherUpdate,
        service: TeacherService = Depends(),
):
    return service.update(teacher_id=teacher_id, teacher_data=teacher_data)


@router.delete('/{teacher_id}')
def delete_course(teacher_id: int,
                  service: TeacherService = Depends(),
                  ):
    return service.delete(teacher_id=teacher_id)
