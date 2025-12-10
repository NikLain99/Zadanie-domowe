def main():
    # Pobranie wymiarów od użytkownika
    rows = int(input("Podaj liczbę wierszy: "))
    cols = int(input("Podaj liczbę kolumn: "))

    # Maksymalna wartość w tabeli (do ustalenia szerokości pól)
    max_value = rows * cols
    cell_width = len(str(max_value)) + 1  # minimalny odstęp

    # Nagłówek kolumn
    print(" " * cell_width, end="")
    for c in range(1, cols + 1):
        print(f"{c:>{cell_width}}", end="")
    print()

    # Oddzielenie nagłówka
    print("-" * (cell_width * (cols + 1)))

    # Wiersze tabliczki
    for r in range(1, rows + 1):
        print(f"{r:>{cell_width}}", end="")  # etykieta wiersza
        for c in range(1, cols + 1):
            print(f"{r * c:>{cell_width}}", end="")
        print()

if __name__ == "__main__":
    main()