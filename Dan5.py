with open('day_5.in', encoding='utf-8') as f:
        vsebina_datoteke = f.read()
vsebina_datoteke = vsebina_datoteke.split(",")

inp = "5"
o = []
def out(n):
    o.append(n)

def temp_code(sez, ctr):
    #print("skra", sez[ctr], [sez[ctr + i] for i in range(4)])
    p = [sez[ctr][:-2], sez[ctr][-2:]]
    l = 0
    #print(p, "ojj")
    if (p[1] == "01" or p[1] == "1") or (p[1] == "02" or p[1] == "2") or (p[1] == "07" or p[1] == "7") or (p[1] == "08" or p[1] == "8"):
        l = 3
    elif(p[1] == "03" or p[1] == "3") or (p[1] == "04" or p[1] == "4"):
        l = 1
    elif (p[1] == "05" or p[1] == "5") or (p[1] == "06" or p[1] == "6"):
        l = 2
    else:
        l = 0
    temp_sez = [p[1]]
    #print(l, "ggg")
    for i in range(l):
        try:
            print(p[1], "ajme:/", p[0])
            if p[0][-i-1] == "0":
                #print("pravilno")
                temp_sez.append(str(sez[int(sez[ctr + i + 1])]))
            else:
                print("oops")
                temp_sez.append(str(sez[ctr + i + 1]))
            print("1ka")
        except:
            print("2ka", sez[ctr + i + 1])
            temp_sez.append(str(sez[int(sez[ctr + i + 1])]))
    print(temp_sez, "::", [sez[ctr + i] for i in range(l+1)])
    return temp_sez

def program2(sez, inpt):
    ctr = 0
    mode = 0
    last = len(sez)
    while ctr < last:
        mode = temp_code(sez, ctr)
        #print(mode, "toj tu")
        if mode[0] == "99":
            return sez
        elif mode[0] == "01" or mode[0] == "1":
            try:
                #print(sez[ctr + 3], "yeet")
                sez[int(sez[ctr + 3])] = str(int(mode[1]) + int(mode[2]))
                #print("not sem")
                #print("Na mesto" + sez[ctr + 3] + "shranim vsoto" + str(int(mode[1]) + int(mode[2])))
            except:
                print("1")
                return None
            ctr += 4
            #print(sez)
        elif mode[0] == "02" or mode[0] == "2":
            try:
                sez[int(sez[ctr + 3])] = str(int(mode[1]) * int(mode[2]))
            except:
                return None
            ctr += 4
            #print(sez)
        elif mode[0] == "03" or mode[0] == "3":
            try:
                sez[int(sez[ctr + 1])] = inpt
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
                    print("skorej 21312312312312312321")
                    ctr = int(mode[2])
                else:
                    ctr += 3
            except:
                return None
            #print(sez)
        elif mode[0] == "06" or mode[0] == "6":
            try:
                if mode[1] == "0":
                    print("skorej 21312312312312312321")
                    ctr = int(mode[2])
                else:
                    ctr += 3
            except:
                return None
            #print(sez)
        elif mode[0] == "07" or mode[0] == "7":
            try:
                if int(mode[1]) < int(mode[2]):
                    sez[int(sez[ctr + 3])] = 1
                else:
                    sez[int(sez[ctr + 3])] = 0
            except:
                return None
            ctr += 4
            #print(sez)
        elif mode[0] == "08" or mode[0] == "8":
            try:
                if int(mode[1]) == int(mode[2]):
                    sez[int(sez[ctr + 3])] = 1
                else:
                    sez[int(sez[ctr + 3])] = 0
            except:
                return None
            ctr += 4
            #print(sez)
        else:
            print(sez[ctr], "yote")
            return None
    return sez

s = [3,21,1008,21,8,20,1005,20,22,107,8,
     21,20,1006,20,31,1106,0,36,98,0,
     0,1002,21,125,20,4,20,1105,1,46,
     104,999,1105,1,46,1101,1000,1,20,4,
     20,1105,1,46,98,99]
sd = [3,21,1008,21,8,20,1005,20,22,107,8,
     21,20,1006,20,31,1106,0,36,98,1001,
     9,1002,21,125,20,4,20,1105,1,46,
     104,999,1105,1,46,1101,1000,1,20,4,
     20,1105,1,46,98,99]
s = [str(i) for i in s]
#print(program2(s))
#print(o)
#print(program2(vsebina_datoteke, inp))
#print(o)

program2(vsebina_datoteke[:], "1")
odgovor1 = o[-1]
with open('day_5_1.out', 'w', encoding='utf-8') as f:
    f.write(str(odgovor1))
print(o, "221312312312312312312312312")
o = []
print(o)

program2(vsebina_datoteke, inp)
print(o)
odgovor2 = o[-1]
with open('day_5_2.out', 'w', encoding='utf-8') as f:
    f.write(str(odgovor2))