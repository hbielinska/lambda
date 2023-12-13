import csv
import os
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

    dof_birth = ["1987", "1978", "1984", "1964", "1974", "1961", "1996", "1988", "1993", "1989"]

    f_path = 'dates.csv'


    with open (f_path, 'w', newline = '') as plik_csv:
        writer = csv.writer(plik_csv)
        for rok in dof_birth:
            writer.writerow([rok])

    print(f'Dane zostały zapisane do pliku CSV: {f_path}')

