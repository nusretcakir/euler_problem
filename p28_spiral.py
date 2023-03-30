import time
start_time = time.time()

toplamlar = 1
toplam = 1
eklenecek = 2
x = 1
for i in range(0,2000):
    if i==0:
        pass
    elif i%4==0:
        eklenecek +=2

    toplam += eklenecek

    toplamlar += toplam


print(toplamlar)

end_time = time.time()
print(f"Kod bloğunun çalışma süresi: {end_time - start_time:.5f} saniye") #Kodun kaç saniyede çalıştığını gösteren kod.
