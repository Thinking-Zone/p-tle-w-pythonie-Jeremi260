import random


def losuj_pogode():
    return random.choice(['Pada', 'Nie pada'])


def zgadnij_pogode():
    odpowiedzi = ['Pada', 'Nie pada']
    print("Zgadnij, czy pada deszcz!")

    
    pogoda = losuj_pogode()

    while True:
        
        odpowiedz_uzytkownika = input("Czy pada deszcz? (Pada/Nie pada): ").strip()

        
        if odpowiedz_uzytkownika not in odpowiedzi:
            print("Proszę wpisać 'Pada' lub 'Nie pada'.")
            continue

       
        if odpowiedz_uzytkownika == pogoda:
            print("Brawo! Zgadłeś poprawnie!")
            break
        else:
            print("Niestety, spróbuj ponownie.")


zgadnij_pogode()
