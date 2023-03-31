import math
import time
start_time = time.time()

digits = []

for sayi in range(3,2540160): # 1 ve 2 dahil değil.
    toplam = 0
    bas = str(sayi)
    for b in bas:
        b=int(b)
        toplam += math.factorial(b)
    if sayi == toplam:
        digits.append(sayi)

print(sum(digits))

end_time = time.time()
print(f"Kod bloğunun çalışma süresi: {end_time - start_time:.5f} saniye") #Kodun kaç saniyede çalıştığını gösteren kod.