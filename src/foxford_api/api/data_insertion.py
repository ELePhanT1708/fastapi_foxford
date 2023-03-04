from fastapi import APIRouter, Depends
from fastapi.openapi.models import Response

import tables
from db import get_session, Session

router = APIRouter(
    prefix='/data',
    tags=['Data']
)


class DataService:

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def insert_teachers(self):
        teachers_data = {
            1: {
                "first_name": "Ramil",
                "last_name": "Khikmatullin",
                "surname": "Rustamovich",
                "rate_per_hour": 100
            },
            2: {
                "first_name": "Rustem",
                "last_name": "Kharisov",
                "surname": "Ramilevich",
                "rate_per_hour": 150
            },
            3: {
                "first_name": "Irek",
                "last_name": "Giniyatov",
                "surname": "Damirovich",
                "rate_per_hour": 200
            },
            4: {
                "first_name": "Damir",
                "last_name": "Adbullin",
                "surname": "Ilmirovich",
                "rate_per_hour": 70
            }
        }
        for data in teachers_data.values():
            teacher = tables.Teacher(**data)
            self.session.add(teacher)
            self.session.commit()

    def insert_courses(self):
        data = {
            1: {
                "name": "Math for students",
                "duration": 40,
                "level": "for students",
                "price": 10000
            },
            2: {
                "name": "English language",
                "duration": 60,
                "level": "for teachers",
                "price": 30000
            },
            3: {
                "name": "Programming",
                "duration": 60,
                "level": "for students",
                "price": 99999
            },
            4: {
                "name": "Linux",
                "duration": 10,
                "level": "for children",
                "price": 10000
            }
        }
        for course_data in data.values():
            course = tables.Course(**course_data)
            self.session.add(course)
            self.session.commit()

    def insert_webinars(self):
        data = {
            1: {
                "planned_time": "2023-03-05T19:00:00.000Z",
                "name": "Express Math",
                "status": "created",
                "duration": 3,
                "course_id": 1
            },
            2: {
                "planned_time": "2023-03-05T21:00:00.000Z",
                "name": "Language INtro",
                "status": "created",
                "duration": 2,
                "course_id": 2
            },
            3: {
                "planned_time": "2023-03-06T19:00:00.000Z",
                "name": "Python for data science",
                "status": "now",
                "duration": 3,
                "course_id": 3
            },
            4: {
                "planned_time": "2023-03-06T19:00:00.000Z",
                "name": "sudo apt and ....",
                "status": "created",
                "duration": 2,
                "course_id": 4
            },
            5: {
                "planned_time": "2023-03-06T19:00:00.000Z",
                "name": "JS and Ajax",
                "status": "cancelled",
                "duration": 2,
                "course_id": 3
            },
        }
        for web_data in data.values():
            webinar = tables.Webinar(**web_data)
            self.session.add(webinar)
            self.session.commit()

    def insert_participations(self):
        data = {
            1: {
                "webinar_id": 1,
                "teacher_id": 1
            },
            2: {
                "webinar_id": 1,
                "teacher_id": 2
            },
            3: {
                "webinar_id": 2,
                "teacher_id": 3
            },
            4: {
                "webinar_id": 2,
                "teacher_id": 4
            },
            5: {
                "webinar_id": 3,
                "teacher_id": 3
            },
            6: {
                "webinar_id": 3,
                "teacher_id": 1
            }
        }
        for part_data in data.values():
            participation = tables.Participation(**part_data)
            self.session.add(participation)
            self.session.commit()


@router.get('/insert_data')
def insert_courses(service: DataService = Depends()):
    service.insert_teachers()
    service.insert_courses()
    service.insert_webinars()
    service.insert_participations()
    return "Data were inserted !!"
