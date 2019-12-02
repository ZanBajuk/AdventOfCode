import math

vsebina_datoteke = ""
with open('day_1.in', encoding='utf-8') as f:
        vsebina_datoteke = f.readlines()
vsebina_datoteke = [x.strip() for x in vsebina_datoteke] 

sum1 = 0
for i in vsebina_datoteke:
    sum1 += math.floor(int(i)/3) - 2

def get_fuel(x):
    current_sum = 0
    current_x = int(x)
    while current_x > 0:
        current_x = max(math.floor(int(current_x)/3) - 2, 0)
        current_sum += current_x
    return current_sum

sum2 = 0
for i in vsebina_datoteke:
    sum2 += get_fuel(i)

odgovor1 = sum1
with open('day_1_1.out', 'w', encoding='utf-8') as f:
    f.write(str(odgovor1))

odgovor2 = sum2
with open('day_1_2.out', 'w', encoding='utf-8') as f:
    f.write(str(odgovor2))
