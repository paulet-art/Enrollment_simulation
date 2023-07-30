class Accomodation():
    _id = 0
    _accomodation = {}
    _hostels = []
    def __init__(self, **kwargs):
        """
        to initialize object of class
        """
        if "fees_per_room" in kwargs.keys():
            self.fees_per_room = kwargs["fees_per_room"]
        else:
            self.fees_per_room = 6500
        self.name = kwargs["name"]
        self.no_rooms = kwargs["no_rooms"]
        self.no_students = 0
        self.id = Accomodation._id
        Accomodation._id += 1
        Accomodation._hostels.append(self)

    def add_student(self, student):
        """
        add students who have been allocated accomodation to _accomodation
        """
        if student.id not in Accomodation._accomodation.keys():
            Accomodation._accomodation[student.id] = self.no_students
            self.no_students += 1
        return self


    @classmethod
    def get_all(cls):
        """
        return all available hostels
        """
        return cls._hostels
        