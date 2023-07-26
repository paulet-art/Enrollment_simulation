from os import path, mkdir, getcwd
from .course import Course
from .student import Student
from .accomodation import Accomodation

class Logger():
    _path = getcwd()
    _classes = ["Student","Course","Accomodation"]
    @classmethod
    def create_path(cls, dir="reports"):
        try:
            new_path = path.join(cls._path,dir)
            mkdir(new_path)
        except(FileExistsError):
            return
    @classmethod
    def create_report(cls, state="initial"):
        current = Student.__name__
        cls.create_path(f"reports/{current}/all")
        for obj in Student._students:
            uuid = "{}_{}_{}".format(obj.name.replace(" ","_"), obj.id, state)
            status = "Paid" if obj.full_fee_paid else "not paid yet"
            hostel = f"{obj.hostel.name}" if obj.hostel else "not yet booked"
            email = f"{obj.email}" if obj.email else "not created yet"
            with open(f"reports/{current}/all/{uuid}", "w") as f:
                f.write(f"Name: {obj.name}\n")
                f.write(f"Cluster Points: {obj.cluster_points}\n")
                f.write(f"Course to take: {obj.course}\n")
                f.write(f"Hostel to take: {hostel}\n")
                f.write(f"Fee Payment Status: {status}\n")
                f.write(f"Fee Balance: {obj.fee_balance}\n")
                f.write(f"Student Email: {email}\n")

    @classmethod
    def create_general_report(cls):
        for k in cls._classes:
            _cls_ = eval(k)
            data = _cls_.get_all()
            current = _cls_.__name__
            if k == "Student":
                current += "/enrolled"
            cls.create_path(f"reports/{current}")

            for obj in data:
                with open(f"reports/{current}/{obj.name}_{obj.id}", "w") as f:
                     for k, v in obj.__dict__.items():
                        f.write("{}: {}\n".format(k.replace("_"," "), v))