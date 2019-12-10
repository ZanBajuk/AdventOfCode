with open('day_9.in', encoding='utf-8') as f:
        vsebina_datoteke = f.read()
vsebina_datoteke = vsebina_datoteke.split(",")

inp = "1"
o = []
def out(n):
    o.append(n)

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

def program2(sez, inpt):
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
            try:
                if len(sez[ctr]) != 3 or sez[ctr][0] == "0":
                    sez[int(sez[ctr + 1])] = inpt
                    #print("0", sez[ctr])
                else:
                    sez[rel_base + int(sez[ctr + 1])] = inpt
                    #print("2", sez[ctr])
            except:
                return None
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

#program2([str(i) for i in [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]], inp)
#program2([str(i) for i in [1102,34915192,34915192,7,4,7,99,0]], inp)
program2(vsebina_datoteke[:], inp)
odgovor1 = o[0]
with open('day_9_1.out', 'w', encoding='utf-8') as f:
    f.write(odgovor1)
o = []
program2(vsebina_datoteke[:], "2")
odgovor2 = o[0]
with open('day_9_2.out', 'w', encoding='utf-8') as f:
    f.write(odgovor2)
