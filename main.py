import csv
import os
from person import Person
import random
from datetime import datetime, timedelta
from csvreader import CsvReader
import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('sqlite3.db')

    def createTable(self):
        c = self.conn.cursor()
        c.execute('''CREATE TABLE if not exists people
                (first_name TEXT, last_name TEXT, address TEXT)''')
        
    def insert(self, person: Person):
        c = self.conn.cursor()
        query = f"""INSERT INTO people(first_name, last_name, address)
            VALUES('{person.first_name}', '{person.last_name}', '{person.address}')"""
        c.execute(query)

    def saveAndCommit(self):
        self.conn.commit()
        

if __name__ == "__main__":
    file_path = os.path.abspath("dane.csv")
    print(file_path)

all_people = CsvReader.ReadCsv(file_path)

#a_names = list(filter(lambda x: x.first_name.startswith('A'), all_people))
#print(a_names)

#google_emails = list(filter(lambda x: '@gmail.com' in x.email, all_people))
#print(google_emails)



#print("\nImiona na 'A':")
#person_with_name_starting_a = list(filter(lambda p: p.first_name.startswith('A') ,all_people))
#print(person_with_name_starting_a)

#print("\nImiona i nazwiska na ta sama litere")
#same_letter = list(filter(lambda p: p.first_name[0] == p.last_name[0], all_people ))
#print(same_letter)

#print("\nMiasto o najwiekszej ilosci osob")
#cities_list = list(map(lambda p: p.city, all_people))
#mpopulous_city = max(cities_list, key=lambda p: cities_list.count(p))
#print(mpopulous_city)

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
person_db = Database()
person_db.createTable()



for p in all_people:
    p.generate_birthday()

f_path = 'persons_data.csv'

with open (f_path, 'w', newline = '') as plik_csv:
    writer = csv.writer(plik_csv)

    for person in all_people:
        writer.writerow(person.__dict__.values())

print("Co chcesz wykonać?\n1.Odfiltruj osoby o imienu na podaną literę \n2.Ofiltruj osoby które mają email w domenie google \n3.Odfiltruj osoby których imię i nazwisko zaczynają się na tą samą literę \n4.Wskaż z jakiego miasta jest najwięcej osób \n5.Wprowadź dane do bazy danych")
choice = input("Wskaż numer polecenia:")

def switch_case(choice):
    if choice == "1":
        print("Wybrano polecenie nr 1: Odfiltruj osoby o imienu na podaną literę")
        letter = input("Wybierz literę:")
        person_with_name_starting = list(filter(lambda p: p.first_name.lower().startswith(letter) ,all_people))
        print(person_with_name_starting)
    elif choice == "2":
        print("Wybrano polecenie nr 2: Ofiltruj osoby które mają email w domenie google")
        google_emails = list(filter(lambda x: '@gmail.com' in x.email, all_people))
        print(google_emails)
    elif choice == "3":
        print("Wybrano polecenie nr 3: Odfiltruj osoby których imię i nazwisko zaczynają się na tą samą literę")
        same_letter = list(filter(lambda p: p.first_name[0] == p.last_name[0], all_people ))
        print(same_letter)
    elif choice == "4":
        print("Wybrano polecenie nr 4: Wskaż z jakiego miasta jest najwięcej osób")
        cities_list = list(map(lambda p: p.city, all_people))
        mpopulous_city = max(cities_list, key=lambda p: cities_list.count(p))
        print(mpopulous_city)
    elif choice == "5":
        print("Wybrano polecenie nr 5: Wprowadź dane do bazy danych")
        try:
            for p in all_people:
                person_db.insert(p)
            person_db.saveAndCommit()
            print("Dane zostały dodane do bazy")
        except Exception as e:
            print(f"Nie udało się dodać danych bo bazy: {e}")
    else:
        print("Wybrano niepoprawny numer")

# Przykłady użycia
switch_case(choice)
#switch_case("2")
#switch_case("3")
#switch_case("4")
#switch_case("5")

