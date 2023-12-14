import csv
import os
from person import Person
import random
from datetime import datetime, timedelta



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

    dof_birth = []

    for i in range(501):
        random_number = random.randint(18*365, 60*365)
        current_date = datetime.now()
        random_year = current_date - timedelta(days=random_number)
        dof_birth.append(random_year.year)
        #print(dof_birth[i])


    f_path = 'dates.csv'
    with open (f_path, 'w', newline = '') as plik_csv:
        writer = csv.writer(plik_csv)

        for dataur in dof_birth:
            writer.writerow([dataur])

    print(f'Dane zostały zapisane do pliku CSV: {f_path}')

    if __name__ == "__main__":
        file_path = os.path.abspath("dane.csv")

        all_people = CsvReader.ReadCsv(file_path)

        for p in all_people:
            p.generate_birthday()

        f_path = 'persons_data.csv'

        with open (f_path, 'w', newline = '') as plik_csv:
            writer = csv.writer(plik_csv)

            for person in all_people:
                writer.writerow(person.__dict__.values())

