from typing import List

from fastapi import APIRouter, Depends

from models.Webinar import (
    Webinar, WebinarCreate, WebinarUpdate
)
from services.Webinar import WebinarService

router = APIRouter(
    prefix='/webinar',
    tags=['Webinar']
)


@router.get('/webinars')
def get_webinars(service: WebinarService = Depends()):
    return service.get_list()


@router.post('/create', response_model=Webinar)
def create_Webinar(webinar_data: WebinarCreate,
                   service: WebinarService = Depends()):
    """
    Creating Webinar
    """
    return service.create(webinar_data=webinar_data)


@router.put('/{webinar_id}', response_model=Webinar)
def update_course(
        webinar_id: int,
        webinar_data: WebinarUpdate,
        service: WebinarService = Depends(),
):
    return service.update(webinar_id=webinar_id, webinar_data=webinar_data)


@router.delete('/{webinar_id}')
def delete_course(webinar_id: int,
                  service: WebinarService = Depends(),
                  ):
    return service.delete(webinar_id=webinar_id)