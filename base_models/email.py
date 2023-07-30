class Email():
    _all_emails = {}
    _emails = []
    id = 0
    def __init__(self, student) -> None:
        """
        initialize object of Email and generates emails for student class
        """
        unique_name = "{}.{}.{}".format(student.first_name, student.middle_name ,student.last_name)
        emails = Email._all_emails
        if unique_name in emails.keys():
            current = unique_name
            count = emails['{}'.format(current)]
            unique_name = "{}.{}".format(unique_name, emails['{}'.format(current)])
            emails['{}'.format(current)] = count + 1
        emails["{}".format(unique_name)] = 0
        self.name = unique_name
        self.id = Email.id
        Email.id += 1
        self.email = "{}@students.jkuat.ac.ke".format(unique_name)
        self.student = student
        Email._emails.append(self)

    @classmethod
    def get_all(cls):
        """
        return all emails generated
        """
        return cls._emails

