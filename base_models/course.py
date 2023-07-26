
class Course():
    _id = 0
    _students = {}
    def __init__(self, **kwargs):
        #max_students=150, fees_per_sem=40000,required_cluster_points=39
        if "max_students" not in kwargs.keys():
            self.max_students = 150
        else:
            self.fees_per_sem = kwargs["max_students"]
        if "fees_per_sem" not in kwargs.keys():
            self.fees_per_sem = 40000
        else:
            self.fees_per_sem = kwargs["fees_per_sem"]
        if "required_cluster_points" not in kwargs.keys():
            self.required_cluster_points = 39
        else:
            self.required_cluster_points = kwargs["required_cluster_points"]
        self.id = Course._id
        self.name = kwargs["name"]
        self.no_students = 0
        Course._id += 1
        
    def __str__(self):
        return "{}".format(self.name)
    
    def add_student(self, student):
        if student.id not in Course._students.keys():
            Course._students[student.id] = student
            self.no_students += 1
        return self