from .course import Course
from .accomodation import Accomodation
from .student import Student
from .common import randomize, random_max_min, RandomizeData


courses = [
    #name, max_students=150, fees_per_sem=40000,required_cluster_points=39, department (class format)
    {"name":"BSc. (General)","max_students":100,"fees_per_sem":15000,"required_cluster_points":random_max_min(41,30), "department":"Pure and Applied Mathematics"},
    {"name":"BSc. in Mathematics and Computer Science","max_students":180, "fees_per_sem":1800,"required_cluster_points":random_max_min(41,30), "department":"Pure and Applied Mathematics"},
    {"name":"BSc. Industrial Mathematics","max_students":200, "fees_per_sem":1600,"required_cluster_points":random_max_min(41,30), "department":"Pure and Applied Mathematics"},
    {"name":"BSc. Actuarial Science","max_students":160, "fees_per_sem":1700,"required_cluster_points":random_max_min(41,30), "department":"Statistics and  acturial Science"},
    {"name":"BSc. Financial Engineering","max_students":80, "fees_per_sem":1500,"required_cluster_points":random_max_min(41,30), "department":"Statistics and  acturial Science"},
    {"name":"BSc. Statisctics","max_students":100,"fees_per_sem":15000,"required_cluster_points":random_max_min(41,30) , "department": "Statistics and  acturial Science" },
    {"name":"BSc. Biostatics","max_students":180, "fees_per_sem":1800,"required_cluster_points":random_max_min(41,30) , "department":"Statistics and  acturial Science"},
    {"name":"BSc. Operation Research","max_students":200, "fees_per_sem":1600,"required_cluster_points":random_max_min(41,30) , "department":"Statistics and  acturial Science"},
    {"name":"BSc. in Physics","max_students":160, "fees_per_sem":1700,"required_cluster_points":random_max_min(41,30) , "department":"Physics"},
    {"name":"BSc. in Control and Instrumentation","max_students":80, "fees_per_sem":1500,"required_cluster_points":random_max_min(41,30) , "department":"Physics"},
    {"name":"BSc. in Geophysics","max_students":80, "fees_per_sem":1500,"required_cluster_points":random_max_min(41,30) , "department":"Physics"},
    {"name":"BSc. in Renewable Energy and Environmental Physics","max_students":200, "fees_per_sem":1600,"required_cluster_points":random_max_min(41,30) , "department":"Physics"},
    {"name":"BSc. Analytical Chemistry","max_students":160, "fees_per_sem":1700,"required_cluster_points":random_max_min(41,30) , "department":"Chemistry"},
    {"name":"BSc. Industrial Chemistry","max_students":80, "fees_per_sem":1500,"required_cluster_points":random_max_min(41,30) , "department":"Chemistry"},
    {"name":"BSc. Chemistry","max_students":80, "fees_per_sem":1500,"required_cluster_points":random_max_min(41,30) , "department":"Chemistry"}
]

hostels = [
    #name, no_rooms=150, fees_per_room=6500 (class format)
    {"name":"Ndovu","no_rooms":100},
    {"name":"Kifaru","no_rooms":80},
    {"name":"Njiwa","no_rooms":200},
    {"name":"Chui","no_rooms":160},
    {"name":"Farasi","no_rooms":80}
]

# initialize object for each dictionary in courses
courses_database = [Course(**i) for i in courses]

# initialize object for each dictionary in hostels
hostels_database = [Accomodation(**i) for i in hostels]

def calc_course():
        """
        create a random index of the courses_database
        return a random course offered
        """
        courses_len = len(courses_database)
        return courses_database[randomize(courses_len)]

def generate_students(no_students):
        """
        create and add random student_data  to list
        return a list of dictionary of random student data
        """
        boolean_values = [True,False]
        length_boolean = len(boolean_values)
        student_data = []
        obj = RandomizeData()
        while no_students > 0:
            random_name = obj.generate_name()
            student_data.append({"first_name":random_name["first_name"],"middle_name":random_name["middle_name"],
             "last_name":random_name["last_name"],"course": calc_course(),
             "has_all_documents":boolean_values[randomize(length_boolean)],
             "requires_accomodation":boolean_values[randomize(length_boolean)],
             "requires_change_course":boolean_values[randomize(length_boolean)]})
            no_students -= 1
        return student_data

student_data = generate_students(10)
                
# creates instances of Student class for each dictionary in student_data
student_database = [Student(**i) for i in student_data]

