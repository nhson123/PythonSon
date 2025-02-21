try:
    ergebnis = 10 / 5
    print(str(ergebnis))
except ZeroDivisionError:
    print('bitte nicht durch 0 dividieren')

except TypeError:
    print('Bitte nur Zahlen')

except:
    print('irgendwas stimmt nicht')

finally:
    print('passt doch noch')

if ergebnis == 5:
    raise Exception('bitte nicht 5')
