import csv
import os

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


class CsvReader:
    @staticmethod
    def ReadCsv(file_path):
        persons = []

        with open(file_path, 'r') as file:
            reader = csv.reader(file)


            for values in reader:
                # print(values)
                person = Person(list(map(str.strip, values)))
                persons.append(person)


        return persons

if __name__ == "__main__":
    file_path = os.path.abspath("dane.csv")
    print(file_path)

    all_people = CsvReader.ReadCsv(file_path)

    a_names = list(filter(lambda x: x.first_name.startswith('A'), all_people))
    print(a_names)

    google_emails = list(filter(lambda x: '@gmail.com' in x.email, all_people))
    print(google_emails)



    print("\nImiona na 'A':")
    person_with_name_starting_a = list(filter(lambda p: p.first_name.startswith('A') ,all_people))
    print(person_with_name_starting_a)

    print("\nImiona i nazwiska na ta sama litere")
    same_letter = list(filter(lambda p: p.first_name[0] == p.last_name[0], all_people ))
    print(same_letter)

    print("\nMiasto o najwiekszej ilosci osob")
    cities_list = list(map(lambda p: p.city, all_people))
    mpopulous_city = max(cities_list, key=lambda p: cities_list.count(p))
    print(mpopulous_city)

