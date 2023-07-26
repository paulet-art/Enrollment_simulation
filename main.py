from base_models.enrollment import Enrollment
from base_models.dummy import student_database
from base_models.logger import Logger

# before enrollment
Logger.create_report()
for student in student_database:
    Enrollment.enroll_student(student)
Logger.create_report("finial")
Logger.create_general_report()

