from typing import List

from fastapi import Depends, HTTPException, status, Response

import tables
from db import Session, get_session
from models.participation import ParticipationCreate, Participation, ParticipationUpdate


class ParticipationService:
    """
    Class for working with relation teacher -- webinar
    """

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, part_id: int) -> tables.Participation:
        part = self.session.query(tables.Participation)\
            .filter_by(id=part_id)\
            .first()
        if not part:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return part

    def get_list(self) -> List[tables.Participation]:
        parts = self.session.query(tables.Participation).all()
        return parts

    def create(self, part_data: ParticipationCreate) -> tables.Participation:
        participation = tables.Participation(**part_data.dict())
        self.session.add(participation)
        self.session.commit()
        return participation

    def update(self, part_id: int, part_data: ParticipationUpdate) -> tables.Participation:
        course = self._get(part_id)
        for key, value in part_data:
            setattr(course, key, value)
        self.session.commit()
        return course

    def delete(self, part_id: int) -> None:
        participation = self._get(part_id)
        self.session.delete(participation)
        self.session.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)