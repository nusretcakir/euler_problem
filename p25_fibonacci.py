import time
start_time = time.time()


fib = [1,1]


for i in range(2,100000000000):
    
    f = fib[i-2] + fib [i-1]
    if len(str(f)) >= 1000:
        print(i+1)
        break
        exit
    else:
        fib.append(f)


end_time = time.time()
print(f"Kod bloğunun çalışma süresi: {end_time - start_time:.5f} saniye") #Kodun kaç saniyede çalıştığını gösteren kod.
