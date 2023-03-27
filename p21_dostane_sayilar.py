import time

start_time = time.time()
sayilarimiz = []

for i in range(1,10001):
    sayilarimiz.append(i)

# print(sayilarimiz)


bolenler = []

for sayi in range(1,10001):
    toplam = 0
    for bolen in range(1,sayi):
        if sayi % bolen == 0:
            toplam += bolen
    bolenler.append(toplam)

# print(bolenler)

bolenler2 = []

for sayi in bolenler:
    toplam2 = 0
    for x in range(1,sayi):
        if sayi % x == 0:
            toplam2 += x
    bolenler2.append(toplam2)

# print(bolenler2)

sonuc = []

for i in range(0,len(sayilarimiz)):
    if sayilarimiz[i] == bolenler2[i]:
        # print(sayilarimiz[i],bolenler[i])
        if sayilarimiz[i] != bolenler[i]:

            sonuc.append(sayilarimiz[i])

print(sum(sonuc))





















end_time = time.time()
print(f"hesaplama bloğunun çalışma süresi: {end_time - start_time:.5f} saniye")