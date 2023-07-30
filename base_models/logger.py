from os import path, mkdir, getcwd,  rmdir
from .course import Course
from .student import Student
from .accomodation import Accomodation
from  .email import Email
import shutil


class Logger():
    _path = getcwd()
    _classes = ["Student","Course","Accomodation","Email"]
    @classmethod
    def create_path(cls, dir="reports"):
        """
        create a logging directory
        if there exists one delete it
        """
        new_path = path.join(cls._path,dir)
        try:
            mkdir(new_path)
        except(FileExistsError):
            shutil.rmtree(new_path)
            mkdir(new_path)
    @classmethod
    def create_report(cls, state="initial"):
        """
        create a report of all the students in the system
        filter to capture only enrolled students
        """
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
        """
        create a report of all the entities of the system
        """
        for class_name in cls._classes:
            _cls_ = eval(class_name)
            data = _cls_.get_all()
            current = _cls_.__name__
            if class_name == "Student":
                current += "/enrolled"
            cls.create_path(f"reports/{current}")
            for obj in data:
                uuid = "{}_{}".format(obj.name.replace(" ","_"),obj.id)
                with open(f"reports/{current}/{uuid}", "w") as f:
                    for k, v in obj.__dict__.items():
                        if k == "student":
                            f.write("{}: {}\n".format("student id", v.id))
                            f.write("{}: {}\n".format("student name", v.name))
                        elif k == "name" and class_name == "Email":
                            f.write("{}: {}\n".format("unique name", v))
                        else:
                            f.write("{}: {}\n".format(k.replace("_"," "), v))