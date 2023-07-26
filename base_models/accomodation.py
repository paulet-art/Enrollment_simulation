class Accomodation():
    _id = 0
    _accomodation = {}
    def __init__(self, **kwargs):
        if "fees_per_room" in kwargs.keys():
            self.fees_per_room = kwargs["fees_per_room"]
        else:
            self.fees_per_room = 6500
        self.name = kwargs["name"]
        self.no_rooms = kwargs["no_rooms"]
        self.no_students = 0
        self.id = Accomodation._id
        Accomodation._id += 1

    def add_student(self, student):
        if student.id not in Accomodation._accomodation.keys():
            Accomodation._accomodation[student.id] = self.no_students
            self.no_students += 1
        return self
        