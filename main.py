"""
Tic tak toe
"""
import mein_modul

mein_modul.begruesung('Son')


# 1. Spielbrett erstellen
def erstellen_brett():
    brett = []
    for i in range(3):
        zeile = [" ", " ", " "]
        brett.append(zeile)

    return brett


# 2 Spielbrett ausgeben
def print_brett(brett):
    for zeile in brett:
        print('|'.join(zeile))
        print('-----')


# 3 Zug machen
def mache_zug(brett, spieler, zeile, spalte):
    if brett[zeile][spalte] == ' ':
        brett[zeile][spalte] = spieler
        return True
    else:
        return False


# 4 Gewinn check
def gewinn_check(brett, spieler):
    for zeile in range(3):
        if brett[zeile][0] == brett[zeile][1] == brett[zeile][2] == spieler:
            return True

    for spalte in range(3):
        if brett[0][spalte] == brett[1][spalte] == brett[2][spalte] == spieler:
            return True
    if brett[0][0] == brett[1][1] == brett[2][2] == spieler or brett[0][2] == brett[1][1] == brett[2][0] == spieler:
        return True


# 5 unentschieden_check
def unentschieden_check(brett):
    for zeile in brett:
        if ' ' in zeile:
            return False

    return True


def spiel_tic_tac_to():
    brett = erstellen_brett()
    aktueller_spieler = 'X'

    while True:
        print_brett(brett)

        try:
            zeile = int(input(f"Spieler {aktueller_spieler}, wähle deine Zeile (0-2)"))
            spalte = int(input(f" Spieler{aktueller_spieler}, wähle deine Spalte (0-2)"))
            if zeile < 0 or zeile > 2 or spalte < 0 or spalte > 2:
                print('bitte nur 0. 1. oder 2 eingeben')
            else:
                if not mache_zug(brett, aktueller_spieler, zeile, spalte):
                    print('Ungültig, bitte erneut versuchen')
        except ValueError:
            print('Bitte nur zahl eingeben, kein Text')

    if gewinn_check(brett, aktueller_spieler):
        print_brett(brett)
        print(f'Du hat gewonnen {aktueller_spieler}')

    elif unentschieden_check(brett):
        print_brett(brett)
        print(' Unentschieden!')
    aktueller_spieler = 'O' if aktueller_spieler == 'X' else 'X'


spiel_tic_tac_to()
