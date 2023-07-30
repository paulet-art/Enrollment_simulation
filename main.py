from base_models.enrollment import Enrollment
from base_models.dummy import student_database
from base_models.logger import Logger


for student in student_database:
    Enrollment.enroll_student(student)
Logger.create_report("finial")
Logger.create_general_report()

