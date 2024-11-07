def zapytaj_o_pogode():
    licznik_nie = 0
    
    while True:
        odpowiedz = input("Czy pada? (tak/nie/nie wiem): ").strip().lower()

        if odpowiedz == "tak":
            print(f"Program zakończony. Liczba odpowiedzi 'nie': {licznik_nie}")
            break
        elif odpowiedz == "nie":
            licznik_nie += 1
        elif odpowiedz == "nie wiem":
            print("To wyjdź na zewnątrz i się dowiedz.")
        else:
            print("Proszę odpowiedzieć 'tak', 'nie' lub 'nie wiem'.")
        
zapytaj_o_pogode()
