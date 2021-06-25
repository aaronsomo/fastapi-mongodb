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


@router.get("/", response_description="Students retrieved")
async def get_students():
    students = await retrieve_students()
    if students:
        return ResponseModel(students, "Students data retrieved successfully")
    return ResponseModel(students, "Empty list returned")


@router.get("/{id}", response_description="Student data retrieved successfully")
async def get_student_data(id):
    student = await retrieve_student(id)
    if student:
        return ResponseModel(student, "Student data retrieved successfully")
    return ErrorResponseModel("An error occured.", 404, "Student doesn't exist.")