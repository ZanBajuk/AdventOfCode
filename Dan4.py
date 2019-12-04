vsebina_datoteke = ""
with open('day_4.in', encoding='utf-8') as f:
        vsebina_datoteke = f.readlines()
vsebina_datoteke = [x.strip() for x in vsebina_datoteke]
vsebina_datoteke = vsebina_datoteke[0].split("-")
min1 = int(vsebina_datoteke[0])
max1 = int(vsebina_datoteke[1])

def succ_test(n):
    last = str(n)[0]
    for i in str(n)[1:]:
        if i == last:
            return True
        last = i
    return False

def dec_test(n):
    last = str(n)[0]
    for i in str(n):
        if int(i) < int(last):
            return False
        last = i
    return True

sez = []
for i in range(min1, max1):
    if succ_test(i) and dec_test(i):
        sez.append(i)

odgovor1 = len(sez)
with open('day_4_1.out', 'w', encoding='utf-8') as f:
    f.write(str(odgovor1))

def succ2_test(n):
    last = str(n)[0]
    num_of_sames = 0
    for i in str(n)[1:]:
        if i == last:
            num_of_sames += 1
        elif num_of_sames == 1:
            return True
        else:
            last = i
            num_of_sames = 0
    if num_of_sames == 1:
        return True
    return False

sez2 = []
for i in range(min1, max1):
    if succ2_test(i) and dec_test(i):
        sez2.append(i)

odgovor2 = len(sez2)
with open('day_4_2.out', 'w', encoding='utf-8') as f:
    f.write(str(odgovor2))