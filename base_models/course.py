
class Course():
    _id = 0
    _students = {}
    _courses = []
    def __init__(self, **kwargs):
        #max_students=150, fees_per_sem=40000,required_cluster_points=39
        self.max_students = 150 if "max_students" not in kwargs.keys() else kwargs["max_students"]
        self.fees_per_sem = 40000 if "fees_per_sem" not in kwargs.keys() else kwargs["fees_per_sem"]
        self.required_cluster_points = 39 if "required_cluster_points" not in kwargs.keys() else kwargs["required_cluster_points"]
        self.id = Course._id
        self.name = kwargs["name"]
        self.no_students = 0
        Course._id += 1
        Course._courses.append(self)
        
    def __str__(self):
        return "{} at {}".format(self.name, self.required_cluster_points)
    
    def add_student(self, student):
        if student.id not in Course._students.keys():
            Course._students[student.id] = student
            self.no_students += 1
        return self
    
    @classmethod
    def get_all(cls):
        return cls._courses