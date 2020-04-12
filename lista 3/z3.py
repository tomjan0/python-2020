def sum_sizes(filename):
    """Funkcja sumująca ostatnią kolumne w pliku z użyciem geeneratora"""
    with open(filename, 'r') as fin:
        return sum(int(line.split(' ')[-1]) for line in fin)
