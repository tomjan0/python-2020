""" Program zmieniający nazwy na małe litery"""

import os
import sys


def all_to_lower(path):
    """ funkcja zmienia wszystkie nazwy na małe litery w zadanej ścieżce"""
    for name in os.listdir(path):
        current = path + '/' + name
        if os.path.isdir(current):
            all_to_lower(current)
        os.rename(current, path + '/' + name.lower())


def main():
    """main"""
    try:
        if os.path.isdir(sys.argv[1]):
            all_to_lower(sys.argv[1])
        else:
            print(sys.argv[1], ' nie jest katalogiem')
    except IndexError:
        print('brak danych')


if __name__ == "__main__":
    main()
