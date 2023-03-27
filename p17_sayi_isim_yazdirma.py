birler = ["bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]
onlar = ["on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]
yüzler = ["yüz","ikiyüz","üçyüz","dörtyüz","beşyüz","altıyüz","yediyüz","sekizyüz","dokuzyüz"]

yazi = ""
for i in range(1,1001):

    uzunluk = (len(str(i)))

    if uzunluk == 1:
        bir = int(str(i)[0])
        # for i in range(i):
        yazi += birler[bir-1]


    elif uzunluk == 2:
        bir = int(str(i)[1])
        on = int(str(i)[0])


        if bir == 0:
            yazi += onlar[on-1]
        else:
            yazi += (onlar[on-1]+birler[bir-1])
        
    elif uzunluk == 3:
        bir = int(str(i)[2])
        on = int(str(i)[1])
        yuz = int(str(i)[0])

        if bir == 0 and on == 0:
            yazi += (yüzler[yuz-1])
        elif on == 0:
            yazi += (yüzler[yuz-1]+birler[bir-1])
        elif bir == 0:
            yazi += (yüzler[yuz-1]+onlar[on-1])
        else:
            yazi += (yüzler[yuz-1]+onlar[on-1]+birler[bir-1])


    if uzunluk == 4:
        yazi += "bin"

print(len(yazi))