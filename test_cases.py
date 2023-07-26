from  enrollment import student_database

obj = student_database[0].generate_email()
print(obj.email)