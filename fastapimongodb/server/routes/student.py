from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from fastapimongodb.server.database import (
    add_student,
    delete_student,
    retrieve_student,
    retrieve_students,
    update_student,
)
from fastapimongodb.server.models.student import (
    ErrorResponseModel,
    ResponseModel,
    StudentSchema,
    UpdateStudentModel,
)

router = APIRouter()

@router.post("/", response_description="Student data added into the database")
async def add_student_data(student: StudentSchema = Body(...)):
    student = jsonable_encoder(student)
    new_student = await add_student(student)

    # route expects a payload that matches the format of StudentSchema, for example:
    #
    # {
    #     "fullname": "John Doe",
    #     "email": "jdoe@x.edu.ng",
    #     "course_of_study": "Water resources engineering",
    #     "year": 2,
    #     "gpa": "3.0",
    # }

    return ResponseModel(new_student, "Student added successfully.")