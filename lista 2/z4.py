"""pogram wyszukujący powtarzających się plików w zadanej ścieżce"""

import os
from os.path import join, getsize
import sys
import hashlib


def find_replicates(path):
    """ funkcja szuka plików o takich samym rozmiarze i wyniku funkcji sha512"""
    print(15 * '-')
    replicates = {}
    for root, _, files in os.walk(path):
        # print(root, files)
        for filename in files:
            file = join(root, filename)
            size = getsize(file)
            with open(file, 'r+') as fin:
                content = fin.read()
                _hash = hashlib.sha512(content.encode()).hexdigest()
                pair = (size, _hash)
                if replicates.get(pair):
                    replicates[pair] += [file]
                else:
                    replicates[pair] = [file]
    for group in replicates.values():
        for name in group:
            print(name)
        print(15 * '-')


def main():
    """main"""
    try:
        if os.path.isdir(sys.argv[1]):
            find_replicates(sys.argv[1])
        else:
            print(sys.argv[1], ' nie jest katalogiem')
    except IndexError:
        print('brak danych')


if __name__ == "__main__":
    main()
