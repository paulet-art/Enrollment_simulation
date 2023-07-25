class Email():
    _all_emails = {}
    def __init__(self, first_name, middle_name ,last_name) -> None:
        unique_name = "{}.{}.{}".format(first_name, middle_name ,last_name)
        emails = Email._all_emails
        if unique_name in emails.keys():
            current = unique_name
            count = emails['{}'.format(current)]
            unique_name = "{}.{}".format(unique_name, emails['{}'.format(current)])
            emails['{}'.format(current)] = count + 1
        emails["{}".format(unique_name)] = 0
        self.email = "{}@students.jkuat.ac.ke".format(unique_name)
    @classmethod
    def getAll(cls):
        return cls._all_emails

