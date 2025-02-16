alter = input('Geben Sie bitte ihr alter ein:')
print('Sie haben eingegeben ' + str(alter) + ' als Alter')
if int(alter) <= 18:
    preis = 5
# print('ihr Ticket kostet: 5 Euro')
elif int(alter) >= 65:
    preis = 7.5
# print('ihr ticket kostet 7,5 Euro')
else:
    preis = 10
# print('ihr Ticket kostet 10 Euro')
print('ihr ticket kostet: ' + str(preis))
anzahl = input('wie viele Tickets möchten sie ')
print('dann kosten ihre' + str(anzahl)+' Tickets ingesamt: ' +
str(int(anzahl)* float(preis)))
