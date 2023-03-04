import sqlalchemy as sa
from sqlalchemy import Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


# for creating many-to-many relationship btw teachers and webinars

class Participation(Base):
    __tablename__ = "participation"
    webinar_id = sa.Column(sa.ForeignKey("webinar.id"), primary_key=True)
    teacher_id = sa.Column(sa.ForeignKey("teacher.id"), primary_key=True)
    comment = sa.Column(sa.String(50))
    webinar = relationship("Webinar", back_populates="teachers")
    teacher = relationship("Teacher", back_populates="webinars")


class Webinar(Base):
    __tablename__ = 'webinar'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    planned_time = sa.Column(sa.TIMESTAMP)
    name = sa.Column(sa.String, unique=True)
    status = sa.Column(sa.String)
    course_id = sa.Column(sa.Integer,
                          sa.ForeignKey('course.id', ondelete='CASCADE'),
                          nullable=False)
    duration = sa.Column(sa.Integer)  # hours

    course = relationship("Course", back_populates="webinars")
    teachers = relationship(
        "Participation", back_populates="webinar"
    )


class Course(Base):
    __tablename__ = 'course'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, unique=True)
    duration = sa.Column(sa.Integer)  # days
    level = sa.Column(sa.String)
    price = sa.Column(sa.Float)

    webinars = relationship(
        'Webinar',
        back_populates='course',
        cascade='all, delete-orphan',
    )


class Teacher(Base):
    __tablename__ = 'teacher'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    first_name = sa.Column(sa.String)
    last_name = sa.Column(sa.String)
    surname = sa.Column(sa.String)  # Отчество
    rate_per_hour = sa.Column(sa.Float)

    webinars = relationship(
        "Participation", back_populates="teacher"
    )
