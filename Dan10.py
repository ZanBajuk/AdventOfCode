import math

with open('day_10.in', encoding='utf-8') as f:
        vsebina_datoteke = f.readlines()
vsebina_datoteke = [x.strip() for x in vsebina_datoteke]

print(vsebina_datoteke)
def delitelji(n):
    return [i for i in range(abs(n)+1) if i > 1 and int(float(n)/float(i)) * i == n]

print(2.5 % 2)

def skupni(s1, s2):
    sez = []
    for i in s1:
        for j in s2:
            if j == i:
                sez.append(i)
    return sez

def polja_med_tockama(t1, t2):
    dx = t2[0] - t1[0]
    dy = t2[1] - t1[1]
    delx = delitelji(dx)
    dely = delitelji(dy)
    c = skupni(delx, dely)
    #print(c, dely, delx, dx, dy)
    polja = set()
    if dx == 0:
        if dy > 0:
            for i in range(1,dy):
                polja.add((t1[0], t1[1] + i))
        else:
            for i in range(1,-dy):
                polja.add((t1[0], t1[1] - i))
        return polja
    if dy == 0:
        if dx > 0:
            for i in range(1,dx):
                polja.add((t1[0]+i, t1[1]))
        else:
            for i in range(1,-dx):
                polja.add((t1[0]-i, t1[1]))
        return polja
    for i in c:
        for j in range(1, i):
            polja.add((t1[0] + dx * j/i, t1[1] + dy * j/i))
    return polja

def preg_as(s):
    for i in s:
        if vsebina_datoteke[int(i[1])][int(i[0])] == "#":
            return False
    return True

#print(polja_med_tockama((0, 2), (4, 2)), "fd")
sez_st = []
for y in range(len(vsebina_datoteke)):
    vm = []
    print(y)
    for x in range(len(vsebina_datoteke[y])):
        st = 0
        if vsebina_datoteke[y][x] == "#":
            for y1 in range(len(vsebina_datoteke)):
                for x1 in range(len(vsebina_datoteke[y1])):
                    if vsebina_datoteke[y1][x1] == "#" and (x,y) != (x1,y1):
                        polja = polja_med_tockama((x,y),(x1,y1))
                        #print(polja, "polja", (x,y),(x1,y1))
                        #print("polja:",(x,y),(x1,y1))
                        if preg_as(polja):
                            st += 1
        vm.append(st)
    sez_st.append(vm)
for i in sez_st:
    print(i)
#print(max([max(i) for i in sez_st]))
odgovor1 = max([max(i) for i in sez_st])
with open('day_10_1.out', 'w', encoding='utf-8') as f:
    f.write(odgovor1)
max_el = (0,0)
#print(sez_st)
for y in range(len(sez_st)):
    for x in range(len(sez_st[0])):
        if sez_st[max_el[1]][max_el[0]] < sez_st[y][x]:
            max_el = (x, y)
#print(sez_st[max_el[1]][max_el[0]])
dic_kotov = {}
for y in range(len(vsebina_datoteke)):
    for x in range(len(vsebina_datoteke[y])):
        if (x, y) != max_el:
            dx = x - max_el[0]
            dy = y - max_el[1]
            kot = (2 * math.pi + (math.atan2(dy, dx) + math.pi/2)) % (2 * math.pi)
            if kot in dic_kotov:
                dic_kotov[kot].append((x,y))
            else:
                dic_kotov[kot] = [(x,y)]
def dolzina (x): return abs(x[0] - max_el[0]) + abs(x[1] - max_el[1])
for key in dic_kotov:
    dic_kotov[key].sort(key=dolzina)
#print(max_el, dic_kotov)
kljuci = [key for key in dic_kotov]
kljuci.sort()
#print(kljuci)

poceni_as = []
def gen_kotov():
    while True:
        for i in kljuci:
            for polje in dic_kotov[i]:
                if vsebina_datoteke[polje[1]][polje[0]] == "#" and polje not in poceni_as:
                    poceni_as.append(polje)
                    yield polje
                    break

g = gen_kotov()
for i in range(200):
    next(g)
#print(poceni_as)
odgovor2 = poceni_as[-1]
with open('day_10_1.out', 'w', encoding='utf-8') as f:
    f.write(odgovor2)
    