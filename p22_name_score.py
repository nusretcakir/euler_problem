import time
start_time = time.time()

with open("p022_names.txt","r",encoding="utf-8") as f:
    isimler = f.read()

isimler = isimler.split(",")
isimler.sort()
harfler = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
toplam = 0

for i in range(0,len(isimler)): # len(isimler)
    isimler[i] = isimler[i].replace("\"","")
    
    kelime_ici = 0
    for x in isimler[i]:  
        for h in range(0,len(harfler)):

            if x.lower()==harfler[h]:

                kelime_ici += h+1

    toplam += (i+1)*kelime_ici

print(toplam) 

end_time = time.time()
print(f"Kod bloğunun çalışma süresi: {end_time - start_time:.5f} saniye") #Kodun kaç saniyede çalıştığını gösteren kod.
