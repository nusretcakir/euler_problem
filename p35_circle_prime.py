from sympy import isprime
import time
start_time = time.time()

primes = []

for i in range(2,1000000):
    if isprime(i)==True:
        primes.append(i)

primes2= []

for p in primes:
    p=str(p)


    degers = []
    for i in range(len(p)):
        degers.append((p[i:] + p[:i]))
    sayac = 0
    for i in range(0,len(degers)):
        if isprime(int(degers[i])) == True:
            sayac += 1
    if len(degers) == sayac:
        primes2.append(p)

print(len(primes2))

end_time = time.time()
print(f"Kod bloğunun çalışma süresi: {end_time - start_time:.5f} saniye") #Kodun kaç saniyede çalıştığını gösteren kod.


    