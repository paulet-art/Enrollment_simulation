class Student():
    def __init__(self, name, cluster_points, enrolled_courses):
        self.name = name
        self.cluster_points = cluster_points
        self.enrolled_courses = enrolled_courses
        self.fee_paid = False
        self.total_fee = 0

class Course():
    def __init__(self, name, no_students=150, fees_per_sem=40000,required_cluster_points=39):
        self.name = name
        self.no_numbers = no_students
        self.fees_per_sem = fees_per_sem
        self.required_cluster_points = required_cluster_points

class Accomodation():
    def __init__(self, name, no_rooms=150, fees_per_room=6500):
        self.name = name
        self.no_rooms = no_rooms
        self.fees_per_room = fees_per_room

# Define the courses and their corresponding fee values
courses = [
    ["Math",100,1000,40],
    ["Science",180,800,35],
    ["History",200,600,30],
    ["English",160,700,25],
    ["Art",80,500,20]
]

hostels = [
    ["Ndovu",100],
    ["Kifaru",80],
    ["Njiwa",200],
    ["Chui",160],
    ["Farasi",80]
]

student_data = [
    {"name": "Alice", "cluster_points": 30, "enrolled_courses": ["Math", "Science", "Art"]},
    {"name": "Bob", "cluster_points": 27, "enrolled_courses": ["History", "English"]},
    {"name": "Charlie", "cluster_points": 41, "enrolled_courses": ["Science", "Art", "English"]},
    {"name": "David", "cluster_points": 35, "enrolled_courses": ["Math", "History"]},
    {"name": "Eva", "cluster_points": 20, "enrolled_courses": ["Math", "Science", "History", "English"]}
]
student_database = [Student(i["name"], i["cluster_points"], i["enrolled_courses"]) for i in student_data]
courses_database = [Course(i[0],i[1],1[2],i[3]) for i in courses]
hostels_database = [Accomodation(i[0],i[1]) for i in hostels]

# Function to check if the student satisfies the set cluster points to pay the fee
def check_cluster_points(student):
    # Assuming the required cluster points to pay the fee is 10
    
    if student.cluster_points <= required_cluster_points:
        student.fee_paid = True

# Function to enroll a student
def enroll_student(student):
    check_cluster_points(student)
    # student.total_fee = student.calculate_total_fee()
    return student

# Enroll students and add them to the database
for student in student_database:
    enroll_student(student)

# Display the student database and their fee payment status
for student in student_database:
    print(f"Name: {student.name}")
    print(f"Cluster Points: {student.cluster_points}")
    print(f"Enrolled Courses: {', '.join(student.enrolled_courses)}")
    if student.fee_paid:
        print("Fee Payment Status: Paid")
    else:
        print("Fee Payment Status: Not Paid")
    print("\n")
