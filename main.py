from datetime import date
isikukood = input("Sisestage isikukood: ")
aasta = str(isikukood[1:3])

if isikukood[0:1] == str(1):
    uusaasta = str(18) + aasta
    sugu = "mees"
elif isikukood[0:1] == str(2):
    uusaasta = str(18) + aasta
    sugu = "naine"
elif isikukood[0:1] == str(3):
    uusaasta = str(19) + aasta
    sugu = "mees"
elif isikukood[0:1] == str(4):
    uusaasta = str(19) + aasta
    sugu = "naine"
elif isikukood[0:1] == str(5):
    uusaasta = str(20) + aasta
    sugu = "mees"
elif isikukood[0:1] == str(6):
    uusaasta = str(20) + aasta
    sugu = "naine"
elif isikukood[0:1] == str(7):
    uusaasta = str(21) + aasta
    sugu = "mees"
elif isikukood[0:1] == str(8):
    uusaasta = str(21) + aasta
    sugu = "naine"
else:
    print("Sisestati vigane isikukood.")
    exit()

if int(isikukood[3:5]) == 0 or int(isikukood[3:5]) > 12:
    print("Sisestati vigane isikukood.")
    exit()
if int(isikukood[5:7]) == 0 or int(isikukood[5:7]) > 31:
    print("Sisestati vigane isikukood.")
    exit()

def arvuta(sünnikuupäev):
    täna = date.today()
    vanus = täna.year - sünnikuupäev.year - ((täna.month, täna.day) < (sünnikuupäev.month, sünnikuupäev.day))
    return vanus

print("Vanus:", arvuta(date(int(uusaasta), int(isikukood[3:5]), int(isikukood[5:7]))))
print("Sugu:", sugu)