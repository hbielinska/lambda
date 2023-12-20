# lambda

## csvreader.py
Zawiera klasę CSvReader:
odczytuje ona dane z pliku CSV, tworzy obiekty klasy Person na podstawie każdego wiersza w pliku CSV, a następnie zwraca listę tych obiektów. 

## dane.csv
Plik csv zawierający dane osobowe

## dates.csv
Plik csv w którym tworzony jest rok urodzin

## main.py
Plik główny:
* tworzenie tabelki, dodawanie do niej danych z pliku csv
* filtrowanie z użyciem lambdy
* tworzenie pliku dates.csv (zawiera wygenerowane lata)
* tworzenie pliku persons_data.csv - dane z pliku dane.csv + wygenerowane daty urodzenia

## person.py
Zawiera klasę Person:
Struktura przechowywująca dane o osobie

## persons_data.csv
Zawiera dane z pliku dane.csv + wygenerowane daty urodzenia

## sqlite3
Baza danych zawierająca imie, nazwisko i adres osoby