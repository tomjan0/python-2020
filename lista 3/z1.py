def transpose(matrix):
    """Funkcja transponująca zadaną macierz"""
    return [" ".join([row.split(" ")[i] for row in matrix]) for i in range(len(matrix))]