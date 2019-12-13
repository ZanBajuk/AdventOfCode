with open('day_13.in', encoding='utf-8') as f:
        vsebina_datoteke = f.read()
vsebina_datoteke = vsebina_datoteke.split(",")
vsebina_datoteke1 = vsebina_datoteke[:]
vsebina_datoteke1[0] = "2"

o = []
score = 0
s_m = False
b_pos = 0
p_pos = 0
load = False

def inp():
    global load
    global b_pos
    global p_pos
    load = True
    if b_pos > p_pos:
        return 1
    elif b_pos < p_pos:
        return -1
    return 0
    #return input()

def out(n):
    global s_m
    global score
    global b_pos
    global p_pos
    #print(len(o))
    o.append(n)
    if len(o) % 3 == 1:
        #print("seveda1")
        if o[-1] == "-1":
            s_m = True
    elif len(o) % 3 == 2:
        #print("seveda2")
        if s_m and o[-1] != "0":
            sez[10 ** 20]
    else:
        #print("seveda3")
        if s_m:
            score = o[-1]
            print("tt", score)
        else:
            grid[int(o[-2])][int(o[-3])] = o[-1]
            if o[-1] == "3":
                p_pos = int(o[-3])
            elif o[-1] == "4":
                b_pos = int(o[-3])
            #print("seveda4", grid)
        s_m = False


grid = [["0" for i in range(40)] for j in range(24)]

def print_grid():
    global load
    if load:
        print("Score:", score)
        for i in grid:
            print("".join(i).replace("0"," ").replace("3","_").replace("2","X").replace("4","O"))
        load = False

def temp_code(sez, ctr, base):
    #print("skra", sez[ctr], [sez[ctr + i] for i in range(4)])
    p = [sez[ctr][:-2], sez[ctr][-2:]]
    l = 0
    #print(p, "ojj")
    if (p[1] == "01" or p[1] == "1") or (p[1] == "02" or p[1] == "2") or (p[1] == "07" or p[1] == "7") or (p[1] == "08" or p[1] == "8"):
        l = 3
    elif(p[1] == "03" or p[1] == "3") or (p[1] == "04" or p[1] == "4") or (p[1] == "09" or p[1] == "9"):
        l = 1
    elif (p[1] == "05" or p[1] == "5") or (p[1] == "06" or p[1] == "6"):
        l = 2
    else:
        l = 0
    temp_sez = [p[1]]
    #print(l, "ggg")
    for i in range(l):
        try:
            #print(p[0], "prepona")
            #print(p[1], "ajme:/", p[0])
            if p[0][-i-1] == "0":
                #print("pravilno")
                temp_sez.append(str(sez[int(sez[ctr + i + 1])]))
            elif p[0][-i-1] == "2":
                temp_sez.append(str(sez[base + int(sez[ctr + i + 1])]))
            else:
                #print("oops")
                temp_sez.append(str(sez[ctr + i + 1]))
            #print("1ka")
        except:
            #print("2ka", sez[ctr + i + 1])
            temp_sez.append(str(sez[int(sez[ctr + i + 1])]))
    #print(temp_sez, "::", [sez[ctr + i] for i in range(l+1)])
    return temp_sez

def program2(sez):
    l = len(sez)
    if l < 10 ** 5:
        sez += ([0] * (10**5 - l))
    ctr = 0
    rel_base = 0
    mode = 0
    last = len(sez)
    while ctr < last:
        #print("Rel baza:", rel_base)
        mode = temp_code(sez, ctr, rel_base)
        #print(mode, "toj tu")
        #print_grid()
        if mode[0] == "99":
            return sez
        elif mode[0] == "01" or mode[0] == "1":
            try:
                if len(sez[ctr]) != 5:
                    #print("0", sez[ctr])
                    sez[int(sez[ctr + 3])] = str(int(mode[1]) + int(mode[2]))
                elif sez[ctr][0] == "2":
                    sez[rel_base + int(sez[ctr + 3])] = str(int(mode[1]) + int(mode[2]))
                    #print("2", sez[ctr])
                else:
                    sez[int(sez[ctr + 3])] = str(int(mode[1]) + int(mode[2]))
                    #print("0", sez[ctr])
            except:
                print("1")
                return None
            ctr += 4
           #print(sez)
        elif mode[0] == "02" or mode[0] == "2":
            try:
                if len(sez[ctr]) != 5:
                    sez[int(sez[ctr + 3])] = str(int(mode[1]) * int(mode[2]))
                    #print("0", sez[ctr])
                elif sez[ctr][0] == "2":
                    sez[rel_base + int(sez[ctr + 3])] = str(int(mode[1]) * int(mode[2]))
                    #print("2", sez[ctr])
                else:
                    sez[int(sez[ctr + 3])] = str(int(mode[1]) * int(mode[2]))
                    #print("0", sez[ctr])
            except:
                return None
            ctr += 4
            #print(sez)
        elif mode[0] == "03" or mode[0] == "3":
            if len(sez[ctr]) != 3 or sez[ctr][0] == "0":
                sez[int(sez[ctr + 1])] = inp()
                "Slabo"
                #print(o, len(o))
                #sez[10 ** 20]
                #print("0", sez[ctr])
            else:
                sez[rel_base + int(sez[ctr + 1])] = inpt
                #print("2", sez[ctr])
            ctr += 2
            #print(sez)
        elif mode[0] == "04" or mode[0] == "4":
            try:
                out(mode[1])
            except:
                return None
            ctr += 2
            #print(sez)
        elif mode[0] == "05" or mode[0] == "5":
            try:
                if mode[1] != "0":
                    ctr = int(mode[2])
                else:
                    ctr += 3
            except:
                return None
            #print(sez)
        elif mode[0] == "06" or mode[0] == "6":
            try:
                if mode[1] == "0":
                    ctr = int(mode[2])
                else:
                    ctr += 3
            except:
                return None
            #print(sez)
        elif mode[0] == "07" or mode[0] == "7":
            try:
                a = 0
                if len(sez[ctr]) != 5 or sez[ctr][0] == "0":
                    a = int(sez[ctr + 3])
                    #print("0", sez[ctr])
                else:
                    a = rel_base + int(sez[ctr + 3])
                    #print("2", sez[ctr])
                if int(mode[1]) < int(mode[2]):
                    sez[a] = 1
                else:
                    sez[a] = 0
            except:
                return None
            ctr += 4
            #print(sez)
        elif mode[0] == "08" or mode[0] == "8":
            try:
                a = 0
                #print(mode[0], sez[ctr], len(sez[ctr]), sez[ctr][0])
                if len(sez[ctr]) != 5 or sez[ctr][0] == "0":
                    a = int(sez[ctr + 3])
                    #print("0", sez[ctr])
                else:
                    a = rel_base + int(sez[ctr + 3])
                    #print("2", sez[ctr])
                if int(mode[1]) == int(mode[2]):
                    sez[a] = 1
                else:
                    sez[a] = 0
            except:
                return None
            ctr += 4
        elif mode[0] == "09" or mode[0] == "9":
            try:
                rel_base += int(mode[1])
            except:
                return None
            ctr += 2
            #print(sez)
        else:
            #print(sez[ctr], "yote")
            return None
    return sez



program2(vsebina_datoteke)
screen = [o[3*i:3*(i+1)] for i in range(len(o)//3)]
bl = {}
for tile in screen:
    if tile[2] in bl:
        bl[tile[2]] += 1
    else:
        bl[tile[2]] = 1
print(bl)
odgovor1 = bl["2"]
with open('day_13_1.out', 'w', encoding='utf-8') as f:
    f.write(str(odgovor1))
#print(screen[0:3], o[:10])
o = []
program2(vsebina_datoteke1)
print("END", score)
odgovor2 = score
with open('day_13_2.out', 'w', encoding='utf-8') as f:
    f.write(str(odgovor2))