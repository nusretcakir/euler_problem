fact = 1

for i in range(1,101):
    fact *=i

toplam = 0
for i in str(fact):
    toplam += int(i)

print(toplam)
