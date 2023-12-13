class Person:
    def __init__(self, values):
        self.first_name = values[0].strip(',')
        self.last_name = values[1].strip(',')
        self.company_name = values[2].strip(',')
        self.address = values[3].strip(',')
        self.city = values[4].strip(',')
        self.country = values[5].strip(',')
        self.state = values[6].strip(',')
        self.zip = values[7].strip(',')
        self.phone1 = values[8].strip(',')
        self.phone2 = values[9].strip(',')
        self.email = values[10].strip(',')
        self.web = values[11].strip(',')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return self.__str__()
