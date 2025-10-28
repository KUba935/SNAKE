import random


def numguesser():
    PLAYING = 1
    zakres = int(input('Wprowadz do jakiej liczby chcesz zgadywać: '))
    
    losowa = random.randint(1,zakres)

    liczba_prob = 0 #Jesli 3 to przegrywa
    while(PLAYING == 1):
        if liczba_prob < 3:
            
            wybor = int(input('Zgadnij liczbę: '))
            
            if wybor == losowa:
                print(f'Zgadłeś ukrytą liczbę! to liczba{losowa}')
                PLAYING = 0
            else:
                liczba_prob += 1
                print(f'Pozostało Ci prob {3-liczba_prob}')
        else:
            print('Nie udało Ci się zgadnąć')
            PLAYING = 0

numguesser()
