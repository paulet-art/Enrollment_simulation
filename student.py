class Student():
    def __init__(self, name, cluster_points, enrolled_courses):
        self.name = name
        self.cluster_points = cluster_points
        self.enrolled_courses = enrolled_courses
        self.fee_paid = False
        self.total_fee = 0