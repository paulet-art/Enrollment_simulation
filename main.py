from base_models.enrollment import Enrollment
from dummy import student_database

# before enrollment
for student in student_database:
    student.display_student()
    Enrollment.enroll_student(student)
    student.display_student("finial")
    

