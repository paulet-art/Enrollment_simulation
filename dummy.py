from base_models.course import Course
from base_models.accomodation import Accomodation
from base_models.student import Student

courses = [
    #name, max_students=150, fees_per_sem=40000,required_cluster_points=39
    {"name":"Math","max_students":100,"fees_per_sem":1000,"required_cluster_points":40},
    {"name":"Science","max_students":180, "fees_per_sem":800,"required_cluster_points":35},
    {"name":"History","max_students":200, "fees_per_sem":600,"required_cluster_points":30},
    {"name":"English","max_students":160, "fees_per_sem":700,"required_cluster_points":25},
    {"name":"Art","max_students":80, "fees_per_sem":500,"required_cluster_points":20}
]

hostels = [
    #name, no_rooms=150, fees_per_room=6500
    {"name":"Ndovu","no_rooms":100},
    {"name":"Kifaru","no_rooms":80},
    {"name":"Njiwa","no_rooms":200},
    {"name":"Chui","no_rooms":160},
    {"name":"Farasi","no_rooms":80}
]

courses_database = [Course(**i) for i in courses]
hostels_database = [Accomodation(**i) for i in hostels]
student_data = [
    #first_name,middle_name,last_name, cluster_points, course, has_all_documents ,requires_accomodation,requires_change_course
    {"first_name":"Alice","middle_name":"Mwiki", "last_name":"mwingi","cluster_points":30,"course": courses_database[3], "has_all_documents":True,"requires_accomodation":True,"requires_change_course":False},
    {"first_name":"Bob","middle_name":"Macalister" ,"last_name":"mwingi","cluster_points":27,"course": courses_database[4], "has_all_documents":False,"requires_accomodation":False,"requires_change_course":False},
    {"first_name":"Charlie","middle_name": "Winson","last_name":"mwingi","cluster_points":41,"course": courses_database[0], "has_all_documents":True,"requires_accomodation":True,"requires_change_course":True },
    {"first_name":"David","middle_name": "Alister","last_name":"mwingi","cluster_points":35,"course": courses_database[1], "has_all_documents":False,"requires_accomodation":False,"requires_change_course":True },
    {"first_name":"Eva","middle_name": "Mungai","last_name":"mwingi","cluster_points":20,"course": courses_database[2], "has_all_documents":True,"requires_accomodation":True,"requires_change_course":False}
]
student_database = [Student(**i) for i in student_data]

