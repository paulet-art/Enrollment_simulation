from .email import Email
from .common import randomize, random_max_min

class Student():
    _id = 0
    _enrolled = []
    _students = []
    def __init__(self, **kwargs):
        """
        inistantiate an object of Student
        """
        self.first_name = kwargs["first_name"]
        self.middle_name = kwargs["middle_name"]
        self.last_name = kwargs["last_name"]
        self.course = kwargs["course"]
        self.cluster_points = self.calc_cluster()
        self.has_all_documents = kwargs["has_all_documents"]
        self.requires_accomodation = kwargs["requires_accomodation"]
        self.requires_change_course = kwargs["requires_change_course"]
        self.hostel = None
        self.full_fee_paid = False
        self.fee_balance = self.course.fees_per_sem
        self.name = self.get_full()
        self.email = None
        self.id = Student._id
        self.requires_accomodation = False
        Student._id += 1
        Student._students.append(self)

    def get_full(self):
        """
        get students fulll name
        """
        return "{} {} {}".format(self.first_name,self.middle_name,self.last_name)
    
    @classmethod
    def add_enrolled(cls, student):
        """
        add student after finishing enrollment
        """
        cls._enrolled.append(student)

    def calc_cluster(self):
        """
        randomly choose the cluster points of a student
        """
        # take the minimum cluster to be the required cluster of the course allocated to student by KUCCPS
        min_cluster = self.course.required_cluster_points
        # get random values between minimum and maximum cluster points
        return  random_max_min(min_cluster, 48)
    
    def calculate_fee(self):
        """
        calculate fee to be paid by including hostel fee
        """
        total_fee = None
        if self.hostel != None:
            total_fee = self.course.fees_per_sem + self.hostel.fees_per_room
        else:
            total_fee = self.course.fees_per_sem
        #get amount that was paid previously
        previous_payment = total_fee - self.fee_balance
        self.pay_fee(previous_payment)
        return self
    
    def rand_pay_fee(self):
        """
        pay random amount of fees of student
        """
        amount = self.course.fees_per_sem
        # randomize returns random value between 0 and amount add to one to include full fee payment
        self.pay_fee(randomize(amount) + 1)
        return self
    
    def pay_full_fee(self):
        """
        pay full fees of student
        """
        amount = self.course.fees_per_sem
        self.pay_fee(amount)
        return self
    
    def pay_fee(self, amount):
        """
        pay a given amount of fees
        """
        self.fee_balance -= amount
        self.full_fee_paid = self.fee_balance <= 0
        return self
    
    @classmethod
    def get_all(cls):
        """
        returns all enrolled students
        """
        return cls._enrolled
    
    def finished_process(self):
        """
        add students who have finished enrolling
        """
        Student._enrolled.append(self)
        return self
    
    def generate_email(self):
        """
        generate email for a student
        """
        self.email = Email(self).email
        return self
    def display_student(self):
        """
        print student to console
        """
        for k, v in self.__dict__.items():
            print(f"{k}: {v}")
        return self


                    



    
