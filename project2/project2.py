#!/usr/bin/env python
try:
    from HoneyProduction import HoneyProduction
    from Drawer import Drawer
    import matplotlib.pyplot as plt
    import csv
    import re
    import decimal
    import sys
except ModuleNotFoundError as errorModule:
    print("Problem with finding module:", errorModule)
    exit(1)

object_array = []


def open_and_parse_csvfile(path):
    try:
        with open(path, 'r') as csvfile:
            rows = csv.reader(csvfile, delimiter=',')
            next(rows, None)
            for row in rows:
                if isinstance(row[0], str):
                    state = row[0]
                else:
                    print("State wasn't a string.")
                    exit(1)

                int_list = row[1:5] + row[6:8]  # specyficzne dane w pliku, w srodku jest jeden float
                for elem in int_list:
                    try:
                        int(elem)
                    except ValueError as error:
                        tmp = re.search('[e]', elem)
                        if tmp.group(0) == "e":     # znalazlo element typu 6e+06
                            for i, j in enumerate(row):
                                if j == elem:
                                    row[i] = int(decimal.Decimal(elem))    # konwersja liczby typu 6e+06
                        else:
                            print("Some element wasn't a int:", error)
                            exit(1)

                number_of_colonies = int(row[1])
                yield_per_colony = int(row[2])
                total_production = int(row[3])
                stocks = int(row[4])
                production_value = int(row[6])
                year = int(row[7])

                try:
                    float(row[5])
                except ValueError as error:
                    print("Price per lb wasn't a float:", error)
                    exit(1)

                price_per_lb = float(row[5])

                new_object = HoneyProduction(state, number_of_colonies, yield_per_colony, total_production, stocks, price_per_lb, production_value, year)
                # print(new_object.__str__()) //tylko testowo czy obiekty tworza sie poprawne
                object_array.append(new_object)
    except EnvironmentError as error:
        print("Problem with reading a file:", error)
        exit(1)


def main():
    if len(sys.argv) != 3:
        print("Wrong number of arguments: ./project2.py, <path to csv file>, <year for which u want diagrams>")
        exit(1)

    # Czytanie nazwy/sciezki do pliku
    try:
        filename = sys.argv[1]
    except IndexError as error:
        print("Problem with reading a path to file:", error)
        exit(1)

    open_and_parse_csvfile(filename)    # Parsowanie pliku

    # Czytanie i parsowanie roku
    try:
        year = sys.argv[2]
        year_int = int(year)
        if year_int < 1998 or year_int > 2012:
            print("Year should be between 1998 and 2012.")
            exit(1)
    except IndexError as error:
        print("Problem with reading year for diagrams:", error)
        exit(1)
    except ValueError as error:
        print("Year is not a int:", error)
        exit(1)

    # Zmienne do rysowania
    state_array = []
    total_production_array = []
    production_value_array = []

    # Wyciagam dane do wykresu dla danego roku
    for elem in object_array:
        if elem.get_state(year_int) is not False:
            state_array.append(elem.get_state(year_int))
        if elem.get_total_production(year_int) is not False:
            total_production_array.append(elem.get_total_production(year_int))
        if elem.get_production_value(year_int) is not False:
            production_value_array.append(elem.get_production_value(year_int))

    # Rysuje wykresy
    print("In case you forgot, diagrams are for year:", year)
    drawer1 = Drawer("total production", state_array, total_production_array)
    drawer1.draw_bar()
    drawer2 = Drawer("production value", state_array, production_value_array)
    drawer2.draw_bar()


if __name__ == "__main__":
    main()
