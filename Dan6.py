with open('day_6.in', encoding='utf-8') as f:
        vsebina_datoteke = f.readlines()
vsebina_datoteke = [x.strip() for x in vsebina_datoteke]
vsebina_datoteke = [i.split(")") for i in vsebina_datoteke]
#print(vsebina_datoteke[:10], len(vsebina_datoteke))
vsi = {i[0] for i in vsebina_datoteke}
vsi = vsi.union({i[1] for i in vsebina_datoteke})
levi = [i[0] for i in vsebina_datoteke]
desni = [i[1] for i in vsebina_datoteke]

def st_orbit(x):
    if x in desni:
        return 1 + st_orbit(levi[desni.index(x)])
    else:
        return 0

sum = 0
for i in vsi:
    sum += st_orbit(i)

def vrni_skupnega(s1, s2):
    #print(s1, s2)
    for i in s1:
        for j in s2:
            if i == j:
                return j
    return False

def najdi_dolzino(x, y):
    sx = [x]
    sy = [y]
    while True:
        c = vrni_skupnega(sx, sy)
        if c:
            return sx.index(c) + sy.index(c) - 2
        else:
            sx.append(levi[desni.index(sx[-1])])
            sy.append(levi[desni.index(sy[-1])])

odgovor1 = sum
with open('day_6_1.out', 'w', encoding='utf-8') as f:
    f.write(str(odgovor1))

odgovor2 = najdi_dolzino("YOU","SAN")
with open('day_6_2.out', 'w', encoding='utf-8') as f:
    f.write(str(odgovor2))

