import math
from student import Student
from accomodation import Accomodation
from course import Course
#assumption
#fees per sem remains constant

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
courses_database = [Course(i[0],i[1],i[2],i[3]) for i in courses]
hostels_database = [Accomodation(i[0],i[1]) for i in hostels]

student_data = [
    ["Alice", 30, hostels_database[3], True],
    ["Bob", 27, hostels_database[4], False],
    ["Charlie", 41, hostels_database[0], True ],
    ["David", 35, hostels_database[1], False ],
    ["Eva", 20, hostels_database[2], True]
]
student_database = [Student(i[0],i[1],i[2],i[3]) for i in student_data]

# Function to check if the student satisfies the set cluster points to pay the fee
def check_cluster_points(student):
    # Assuming the required cluster points to pay the fee is 10
    if student.cluster_points <= 20:
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
