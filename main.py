from base_models.enrollment import Enrollment
from base_models.dummy import student_database

# before enrollment
for student in student_database:
    student.create_report()
    Enrollment.enroll_student(student)
    student.create_report("finial")
    

