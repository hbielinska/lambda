import csv
from person import Person

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