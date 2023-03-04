from typing import List

from fastapi import APIRouter, Depends

from models.participation import (
    ParticipationCreate, Participation, ParticipationUpdate
)
from services.Participation import ParticipationService

router = APIRouter(
    prefix='/participation',
    tags=['Participation']
)


@router.get('/all', response_model=List[Participation])
def get_participations(service: ParticipationService = Depends()):
    return service.get_list()


@router.post('/create', response_model=Participation)
def create_participation(part_data: ParticipationCreate,
                         service: ParticipationService = Depends()):
    """
    Adding teacher to webinar
    """
    return service.create(part_data=part_data)


@router.put('/{part_id}', response_model=Participation)
def update_course(
        part_id: int,
        part_data: ParticipationUpdate,
        service: ParticipationService = Depends(),
):
    return service.update(part_id=part_id, part_data=part_data)


@router.delete('/{part_id}')
def delete_course(part_id: int,
                  service: ParticipationService = Depends(),
                  ):
    return service.delete(part_id=part_id)
