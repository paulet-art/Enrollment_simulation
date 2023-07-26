from .student import Student
from .dummy import hostels_database, courses_database


#create intances
class Enrollment():
    @classmethod
    def change_course(cls, student: Student):
        previous_payment = student.course.fees_per_sem - student.fee_balance
        for i in courses_database:
            if i.no_students < i.max_students:
                if student.cluster_points >= i.required_cluster_points:
                    student.course = i
                    student.fee_balance = i.fees_per_sem
                    student.pay_fee(previous_payment)
                    i.add_student(student)
    @classmethod
    def find_hostel(cls, student: Student):
        for i in hostels_database:
            if i.no_rooms > i.no_students:
                    student.hostel = i
                    student.calculate_fee()
                    student.pay_fee(6500)
    @classmethod
    def enroll_student(cls, student: Student):
        if student.has_all_documents:
            if student.full_fee_paid:
                if student.requires_change_course:
                    cls.change_course(student)
                if student.requires_accomodation:
                    cls.find_hostel(student)
                student.generate_email()
                Student.add_enrolled(student)
        return student
