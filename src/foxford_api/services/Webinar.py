from typing import List

from fastapi import Depends, HTTPException, status, Response

import tables
from db import Session, get_session
from models.Webinar import WebinarUpdate, WebinarCreate, Webinar
from sqlalchemy import select

class WebinarService:

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, webinar_id: int) -> tables.Webinar:
        webinar = self.session.query(tables.Webinar)\
            .filter_by(id=webinar_id)\
            .first()
        if not webinar:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return webinar

    def get_list(self):

        webinars = self.session.query(tables.Webinar).all()
        return webinars

    def create(self, webinar_data: WebinarCreate) -> tables.Webinar:
        webinar = tables.Webinar(**webinar_data.dict())
        self.session.add(webinar)
        self.session.commit()
        return webinar

    def update(self, webinar_id: int, webinar_data: WebinarUpdate) -> tables.Webinar:
        webinar = self._get(webinar_id)
        for key, value in webinar_data:
            setattr(webinar, key, value)
        self.session.commit()
        return webinar

    def delete(self, webinar_id: int) -> None:
        webinar = self._get(webinar_id)
        self.session.delete(webinar)
        self.session.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)