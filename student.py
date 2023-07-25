from enrollment import courses_database
from email import Email

class Student():
    _id = 0
    def __init__(self, first_name,middle_name,last_name, cluster_points, course, has_all_documents):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.cluster_points = cluster_points
        self.course = course
        self.has_all_documents = has_all_documents
        self.full_fee_paid = False
        self.fee_balance = self.course.fees_per_sem
        self.id = Student._id + 1

    def pay_fee(self, amount):
        self.fee_balance -= amount
        return self
    
    def change_course(self):
        previous_payment = self.course.fees_per_sem - self.fee_balance
        for i in courses_database:
            if i.no_students < i.max_students:
                if self.cluster_points >= i.required_cluster_points:
                    self.course = i
                    self.fee_balance = i.fees_per_sem
                    self.pay_fee(previous_payment)
                    i.add_student()
                    return self
        return self
    
    def generate_email(self):
        self.email = Email(self.first_name,self.middle_name,self.last_name).email
        return self
                    



    
