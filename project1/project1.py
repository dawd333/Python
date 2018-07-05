#!/usr/bin/python
try:
    import sys
    import random
    import string
except ModuleNotFoundError as errorModule:
    print("Problem with finding module:", errorModule)
    exit(1)


# Wpisywanie slow z pliku do listy, wraz z usunieciem znakow konca linii po kazdym slowie
def get_list_of_words(path):
    try:
        with open(path) as file:
            list_of_words = [word.rstrip('\n') for word in file]
    except EnvironmentError as error:
        print("Problem with reading a file:", error)
        exit(1)
    return list_of_words


def main():
    # Czytanie nazwy / sciezki do pliku
    try:
        filename = sys.argv[1]
    except IndexError as error:
        print("Problem with opening a path to file with words:", error)
        exit(1)

    # Wpisanie slow z pliku do listy
    words = get_list_of_words(filename)

    # Wybranie losowego slowa z podanych
    target = random.choice(words)
    if len(target.split()) > 1:  # Jesli w wylosowanej linijce bedzie wiecej niz 1 slowo zapisane
        print("There are at least two words in a single line, fix it!")
        exit(1)

    s = 0
    guesses = []

    # Stworzenie listy trafionych juz liter
    while s < len(target):
        guesses.append('_')
        s = s + 1

    # Zmienne potrzebne do obslugi gry
    lives = 3
    already_chosen = []
    letters = len(target)

    # Glowna petla gry sprawdzajaca warunki zakonczenia
    while letters > 0 and lives > 0:
        offset = 0  # Ustawienie trafionej litery w odpowiednim miejscu szukanego wyrazu
        flag = 0  # Flaga sprawdzajaca czy udalo nam sie przeczytac litere
        if lives == 1:
            print("You have", lives, "life.")
        else:
            print("You have", lives, "lives.")
        print("You have already chosen this letters:", *already_chosen, sep=' ')
        print("Try guess the word!:", *guesses, sep=' ')
        print("Please enter next letter: ")
        while flag == 0:
            try:
                letter_input = input()  # Czytanie znaku
                if letter_input.isupper() is True:
                    letter = letter_input.lower()
                else:
                    letter = letter_input
            except IOError as error:
                print("Problem with a given input:", error)
                exit(1)
            if len(letter) != 1:  # Jesli nie bylby to pojedynczy znak
                print("Enter one char please:")
            elif letter.isalpha() is not True:  # Jesli nie bylby to znak
                print("Enter char please:")
            elif letter in already_chosen:  # Jesli powtarzamy dana litere
                print("You have already tried this letter:", letter)
                print("Please try again with another letter:")
            else:
                flag = 1  # Zmienienie flagi odpowiadajacej za to czy przeczytalismy litere
                flag2 = 0  # Flaga odpowiadajaca za to czy trafilismy litere ze slowa czy nie
                for char in target:
                    if letter == char:  # Trafienie litery
                        try:
                            guesses[offset] = letter  # Ustawienie litery w odpowiednim miejscu
                        except IndexError as error:
                            print("Problem with setting up a letter in a appropriate place:", error)
                            exit(1)
                        letters = letters - 1  # Dekrementacja licznika liter do odgadniecia
                        flag2 = 1  # Trafilismy litere ze slowa wiec przestawiamy flage
                    offset = offset + 1  # Ustawienie odpowiedniej pozycji odgadywanie litery
                already_chosen.append(letter)  # Dodanie litery do listy juz zgadywanych
                if flag2 == 0:  # Jesli nie trafilismy litery odejmujemy zycie
                    lives = lives - 1

    if letters == 0:  # Jesli zgadlismy wszystkie litery
        print("Congratulations! You have guessed the word:", target)
        raise SystemExit
    if lives == 0:  # Jesli skonczyly nam sie zycia
        print("The word you was looking for was:", target)
        print("Try again next time :(")
        raise SystemExit


if __name__ == "__main__":
    main()
