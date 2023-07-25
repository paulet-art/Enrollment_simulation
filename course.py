
class Course():
    def __init__(self, name, max_students=150, fees_per_sem=40000,required_cluster_points=39):
        self.name = name
        self.no_students = 0
        self.max_students = max_students
        self.fees_per_sem = fees_per_sem
        self.required_cluster_points = required_cluster_points
    
    def add_student(self):
        self.no_students += 1
        return self