from os import path, mkdir, getcwd
class Logger():
    _path = getcwd()
    def create_path(self, dir="reports"):
        try:
            new_path = path.join(Logger._path,dir)
            mkdir(new_path)
        except(FileExistsError):
            return
        
    def create_report(self, state="initial"):
        current = self.__class__.__name__
        self.create_path(f"reports/{current}")
        if current == "Student":
            uuid = "{}_{}_{}".format(self.name.replace(" ","_"), self.id, state)
            status = "Paid" if self.full_fee_paid else "not paid yet"
            hostel = f"{self.hostel.name}" if self.hostel else "not yet booked"
            email = f"{self.email}" if self.email else "not created yet"
            with open(f"reports/students/{uuid}", "w") as f:
                f.write(f"Name: {self.name}\n")
                f.write(f"Cluster Points: {self.cluster_points}\n")
                f.write(f"Course to take: {self.course}\n")
                f.write(f"Hostel to take: {hostel}\n")
                f.write(f"Fee Payment Status: {status}\n")
                f.write(f"Fee Balance: {self.fee_balance}\n")
                f.write(f"Student Email: {email}\n")
