from itertools import permutations
import re
import functools

numbers = "0123456789"
permutasyonlar = permutations(numbers)

sayac = 1
for i in permutasyonlar:
    if sayac == 1000000:
        a=i
        break
    else:
        sayac += 1
        pass
rakam = ""
for i in a:
    rakam += str(i)

print(rakam)