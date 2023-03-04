import asyncio
import time
from typing import List, Union

from fastapi import FastAPI, Depends
import logging

import tables
from db import engine, Session, get_session
from api.teacher import router as teacher_router
from api.webinar import router as webinar_router
from api.course import router as course_router
from api.participation import router as participation_router
from api.data_insertion import router as data_router

logger = logging.getLogger(__name__)
tables.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='Foxford API',
    description='API for work with Webinars',
    version='1.0.0',
)

app.include_router(teacher_router)
app.include_router(webinar_router)
app.include_router(course_router)
app.include_router(participation_router)
app.include_router(data_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
