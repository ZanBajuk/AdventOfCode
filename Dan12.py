import math

with open('day_12.in', encoding='utf-8') as f:
        vsebina_datoteke = f.readlines()
vsebina_datoteke = [x.strip() for x in vsebina_datoteke]
pos = []
for i in vsebina_datoteke:
    s = i.split(",")
    pos.append([int(s[0][3:]), int(s[1][3:]), int(s[2][3:-1])])
vel = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
vel1 = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
zac_pos = [[i[j] for i in pos] for j in range(len(pos[0]))]
sez_uj = []

pos1 = []
for i in vsebina_datoteke:
    s = i.split(",")
    pos1.append([int(s[0][3:]), int(s[1][3:]), int(s[2][3:-1])])

print("zp:", zac_pos)
ctr = 0

def update_vel():
    for i in range(len(vel1)):
        for j in range(len(pos1)):
            if j != i:
                for cr in range(len(pos1[j])):
                    if pos1[j][cr] > pos1[i][cr]:
                        vel1[i][cr] += 1
                    elif pos1[j][cr] < pos1[i][cr]:
                        vel1[i][cr] += -1
    #print(vel)

def update_pos():
    for i in range(len(pos1)):
        for cr in range(len(pos1[i])):
            pos1[i][cr] += vel1[i][cr]
    #print(pos)

def get_kin():
    sum1 = 0
    for j in range(len(pos1)):
        sum1 += sum([abs(i) for i in pos1[j]]) * sum([abs(i) for i in vel1[j]])        
    return sum1

def update_vel_cr(cr):
    for i in range(len(vel)):
        for j in range(len(pos)):
            if i != j:
                if pos[j][cr] > pos[i][cr]:
                    vel[i][cr] += 1
                elif pos[j][cr] < pos[i][cr]:
                    vel[i][cr] += -1
    #print("vel:", vel)

def update_pos_cr(cr):
    for i in range(len(vel)):
        pos[i][cr] += vel[i][cr]
    #print("pos:", pos)

for i in range(1000):
    update_vel()
    update_pos()
    #print("?????")
print(pos,"fdsafadsfasdfadsfasdfs")
print(get_kin())

odgovor1 = get_kin()
with open('day_12_1.out', 'w', encoding='utf-8') as f:
    f.write(str(odgovor1))

print(zac_pos, pos)
#print(k[4])

cikli = []
#for i in range(len(pos)):
    #print(pos[i], "CO*")
for j in range(len(pos[0])):
    k = 2
    while True:
        update_vel_cr(j)
        update_pos_cr(j)
        #print([k[j] for k in pos], zac_pos[j], [k[j] for k in pos] == zac_pos[j], "DD")
        if [k[j] for k in pos] == zac_pos[j]:
            cikli.append(k)
            break
        k += 1
    print("UUUUU", j, "?")
d1 = math.gcd(cikli[0], cikli[1])
lcm1 = cikli[0] * cikli[1] // d1
d2 = math.gcd(lcm1, cikli[2])
lcm2 = lcm1 * cikli[2] // d2
print(lcm2)

odgovor2 = lcm2
with open('day_12_2.out', 'w', encoding='utf-8') as f:
    f.write(str(odgovor2))