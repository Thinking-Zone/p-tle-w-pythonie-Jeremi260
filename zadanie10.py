# Zadanie:
# Napisz program, który wypisze wszystkie liczby, które są podzielne zarówno przez 3, jak i przez 5 w zakresie od 1 do 100.
# Program powinien wypisać te liczby w jednej linii, oddzielone spacjami.

print("A pod spodem rozwiązanie tego zadanka, napisane w Pythonie :)")

# Rozwiązanie:
for i in range(1, 101):  # Iterujemy po liczbach od 1 do 100
    if i % 3 == 0 and i % 5 == 0:  # Sprawdzamy, czy liczba jest podzielna przez 3 i 5
        print(i, end=" ")  # Wypisujemy liczbę, oddzielając je spacją
