def polowa (dlugosc):
    if dlugosc%2 == 0:
        pol = dlugosc/2
    else:
        pol = (dlugosc-1)/2
    return pol

def bezspacji (znaki):
    znaki=znaki.split()
    ciag=''
    for i in range(0,len(znaki)):
        ciag=ciag+znaki[i]
    return ciag

def odwracanie(znaki):
    dl=len(znaki)
    koniec=''
    poczatek=''
    for i in range(0,polowa(dl)):
        lodp=znaki[i]
        lodk=znaki[dl-i-1]
        poczatek=poczatek+lodk
        koniec=lodp+koniec
    if dl%2==0:
        znaki=poczatek+koniec
    else:
        znaki=poczatek+znaki[polowa(dl)]+koniec
    return znaki
        

def palindrom(tekst):
    bezsp=bezspacji(tekst)
    dl=len(bezsp)
    cz1=bezsp[0:polowa(dl)]
    cz2=odwracanie(bezsp[-polowa(dl):dl])
    if cz1.lower()==cz2.lower():
        return True
    else:
        return False
    
print(palindrom("Kobyla ma maly bok"))
print(palindrom("Zakopane na pokaz"))
print(palindrom("Lubie placki"))
