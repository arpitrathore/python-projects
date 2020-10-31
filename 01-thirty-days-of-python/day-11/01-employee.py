import datetime

DATE_FORMAT = "dd-MM-yyyy"

def str_to_date(date_str):
    return datetime.strptime(date_str, DATE_FORMAT)

class Employee:
    company = "Qualys"

    def __init__(self, id, name, doj):
        self.id = id
        self.name = name
        self.doj = doj

    def __str__(self):
        return f"Employee with id={self.id}, name={self.name}, doj={self.doj}, company={self.company}"



doj = datetime.date(year=2016, month=12, day=26)
e1 = Employee(1, "Arpit", doj)
e2 = Employee(2, "Yash", datetime.date(year=2018, month=11, day=11))

print(e1)
print(e2)