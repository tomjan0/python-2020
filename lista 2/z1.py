""" Program zwracający statystyki dla pliku tekstowego """

import sys


def stats(filename):
    """oblicza ilość bajtów, ilość słów,ilość lini i maksymalną długość lini dla zadanego pliku"""
    with open(filename, "r+") as fin:
        text = fin.read()
        lines = text.splitlines()

        word_count = len(text.split())
        lines_count = len(lines)
        byte_count = len(bytes(text, 'utf8'))
        max_line_count = len(max(lines, key=len))

        print('Liczba bajtów: ', byte_count)
        print('Liczba słów: ', word_count)
        print('Liczba lini: ', lines_count)
        print('Maksymalna dlugość lini: ', max_line_count)


def main():
    """main"""
    try:
        stats(sys.argv[1])
    except IndexError:
        print('brak danych')
    except FileNotFoundError:
        print("Błędna nazwa pliku")


if __name__ == "__main__":
    main()
