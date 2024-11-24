def flip_horizontal(result):
    # Tworzenie listy do przechowywania wartości wierszy
    horizontal_values = []
    for value in result.values():
        horizontal_values.append(value)  # Dodawanie wartości z każdego bębna do listy poziomej

    # Ustalanie liczby wierszy i kolumn na podstawie wyników bębnów
    rows, cols = len(horizontal_values), len(horizontal_values[0])

    # Tworzenie pustej macierzy o wymiarach [kolumny][wiersze]
    hvals2 = [[""] * rows for _ in range(cols)]

    # Obracanie macierzy tak, aby kolumny stały się wierszami
    for x in range(rows):
        for y in range(cols):
            hvals2[y][rows - x - 1] = horizontal_values[x][y]  # Przypisanie odwróconych wartości

    # Odwracanie kolejności elementów w każdej kolumnie, aby uzyskać poprawny układ poziomy
    hvals3 = [item[::-1] for item in hvals2]

    return hvals3  # Zwrócenie wynikowej listy wierszy

def longest_seq(hit):
    # Zmienna do śledzenia aktualnej i najdłuższej długości sekwencji
    subSeqLength, longest = 1, 1
    start, end = 0, 0  # Indeksy początku i końca najdłuższej sekwencji

    # Iteracja przez listę symboli
    for i in range(len(hit) - 1):
        if hit[i] == hit[i + 1] - 1:  # Sprawdzanie, czy bieżący element tworzy sekwencję rosnącą
            subSeqLength += 1  # Zwiększanie długości bieżącej sekwencji
            if subSeqLength > longest:  # Aktualizacja najdłuższej sekwencji
                longest = subSeqLength
                start = i + 2 - subSeqLength  # Obliczanie początku sekwencji
                end = i + 2  # Obliczanie końca sekwencji
        else:
            subSeqLength = 1  # Resetowanie długości sekwencji, jeśli nie ma ciągłości

    return hit[start:end]  # Zwrócenie najdłuższej znalezionej sekwencji
