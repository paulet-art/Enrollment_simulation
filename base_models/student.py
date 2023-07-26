from .email import Email
from .common import randomize

class Student():
    _id = 0
    _enrolled = []
    def __init__(self, **kwargs):
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

    def get_full(self):
        return "{} {} {}".format(self.first_name,self.middle_name,self.last_name)
    
    
    def calc_cluster(self):
        min = self.course.required_cluster_points
        rand = 48 - self.course.required_cluster_points
        diff =  randomize(5)
        if rand < 5:
            diff = randomize(rand)
        return  min + diff
    
    def calculate_fee(self):
        total_fee = None
        if self.hostel:
            total_fee = self.course.fees_per_sem + self.hostel.fees_per_room
        else:
            total_fee = self.course.fees_per_sem
        previous_payment = total_fee - self.fee_balance
        self.pay_fee(previous_payment)
        return self
    
    def rand_pay_fee(self):
        extra = randomize(self.course.fees_per_sem/2)
        amount = self.course.fees_per_sem
        self.pay_fee(amount)
        return self
    
    def pay_fee(self, amount):
        self.fee_balance -= amount
        self.full_fee_paid = self.fee_balance <= 0
        return self
    
    def finished_process(self):
        Student._enrolled.append(self)
        return self
    
    def generate_email(self):
        self.email = Email(self.first_name,self.middle_name,self.last_name).email
        return self
    def display_student(self, state="initial"):
        status = "Paid" if self.full_fee_paid else "not paid yet"
        hostel = f"{self.hostel.name}" if self.hostel else "not yet booked"
        email = f"{self.email}" if self.email else "not created yet"
        print(f"Name: {self.name}")
        print(f"Cluster Points: {self.cluster_points}")
        print(f"Course to take: {self.course}")
        print(f"Hostel to take: {hostel}")
        print(f"Fee Payment Status: {status}")
        print(f"Fee Balance: {self.fee_balance}")
        print(f"Student Email: {email}")
        print("\n")
        self.create_report(state)

    def create_report(self, state="initial"):
        uuid = "{}_{}_{}".format(self.name.replace(" ","_"), self.id, state)
        status = "Paid" if self.full_fee_paid else "not paid yet"
        hostel = f"{self.hostel.name}" if self.hostel else "not yet booked"
        email = f"{self.email}" if self.email else "not created yet"
        with open(f"reports/{uuid}", "w") as f:
            f.write(f"Name: {self.name}\n")
            f.write(f"Cluster Points: {self.cluster_points}\n")
            f.write(f"Course to take: {self.course}\n")
            f.write(f"Hostel to take: {hostel}\n")
            f.write(f"Fee Payment Status: {status}\n")
            f.write(f"Fee Balance: {self.fee_balance}\n")
            f.write(f"Student Email: {email}\n")

                    



    
