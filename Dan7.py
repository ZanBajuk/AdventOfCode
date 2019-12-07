import itertools

with open('day_7.in', encoding='utf-8') as f:
        vsebina_datoteke = f.read()
vsebina_datoteke = vsebina_datoteke.split(",")
print(vsebina_datoteke)

o = ["0"]
def out(n):
    o.append(n)

def inp_gen(sez):
    for i in sez:
        yield i
        yield o[-1]
    while True:
        yield o[-1]

inp = ""

def temp_code(sez, ctr):
    p = [sez[ctr][:-2], sez[ctr][-2:]]
    l = 0
    if (p[1] == "01" or p[1] == "1") or (p[1] == "02" or p[1] == "2") or (p[1] == "07" or p[1] == "7") or (p[1] == "08" or p[1] == "8"):
        l = 3
    elif(p[1] == "03" or p[1] == "3") or (p[1] == "04" or p[1] == "4"):
        l = 1
    elif (p[1] == "05" or p[1] == "5") or (p[1] == "06" or p[1] == "6"):
        l = 2
    else:
        l = 0
    temp_sez = [p[1]]
    for i in range(l):
        try:
            if p[0][-i-1] == "0":
                temp_sez.append(str(sez[int(sez[ctr + i + 1])]))
            else:
                temp_sez.append(str(sez[ctr + i + 1]))
        except:
            temp_sez.append(str(sez[int(sez[ctr + i + 1])]))
    #print(temp_sez, "::", [sez[ctr + i] for i in range(l+1)])
    return temp_sez

def program2(sez):
    ctr = 0
    mode = 0
    last = len(sez)
    while ctr < last:
        mode = temp_code(sez, ctr)
        if mode[0] == "99":
            return sez
        elif mode[0] == "01" or mode[0] == "1":
            try:
                sez[int(sez[ctr + 3])] = str(int(mode[1]) + int(mode[2]))
            except:
                return None
            ctr += 4
        elif mode[0] == "02" or mode[0] == "2":
            try:
                sez[int(sez[ctr + 3])] = str(int(mode[1]) * int(mode[2]))
            except:
                return None
            ctr += 4
        elif mode[0] == "03" or mode[0] == "3":
            try:
                sez[int(sez[ctr + 1])] = next(inp)
            except:
                return None
            ctr += 2
        elif mode[0] == "04" or mode[0] == "4":
            try:
                out(mode[1])
            except:
                return None
            ctr += 2
        elif mode[0] == "05" or mode[0] == "5":
            try:
                if mode[1] != "0":
                    ctr = int(mode[2])
                else:
                    ctr += 3
            except:
                return None
        elif mode[0] == "06" or mode[0] == "6":
            try:
                if mode[1] == "0":
                    ctr = int(mode[2])
                else:
                    ctr += 3
            except:
                return None
        elif mode[0] == "07" or mode[0] == "7":
            try:
                if int(mode[1]) < int(mode[2]):
                    sez[int(sez[ctr + 3])] = 1
                else:
                    sez[int(sez[ctr + 3])] = 0
            except:
                return None
            ctr += 4
        elif mode[0] == "08" or mode[0] == "8":
            try:
                if int(mode[1]) == int(mode[2]):
                    sez[int(sez[ctr + 3])] = 1
                else:
                    sez[int(sez[ctr + 3])] = 0
            except:
                return None
            ctr += 4
        else:
            print(sez[ctr], "yote")
            return None
    #print(sez)
    return sez

max_sez = []
for i in itertools.permutations([0, 1, 2, 3, 4]):
    inp = inp_gen(i)
    for j in range(5):
        program2(vsebina_datoteke[:])
        #print(o, i)
    print(o[-1], i)
    max_sez.append(int(o[-1]))
    o = ["0"]
print(max(max_sez), max_sez)
odgovor1 = max(max_sez)
with open('day_7_1.out', 'w', encoding='utf-8') as f:
    f.write(str(odgovor1))

def program3(sez):
    ctr = 0
    mode = 0
    last = len(sez)
    while ctr < last:
        mode = temp_code(sez, ctr)
        if mode[0] == "99":
            #print(sez)
            yield False
        elif mode[0] == "01" or mode[0] == "1":
            try:
                sez[int(sez[ctr + 3])] = str(int(mode[1]) + int(mode[2]))
                #print(sez)
            except:
                yield None
            ctr += 4
        elif mode[0] == "02" or mode[0] == "2":
            try:
                sez[int(sez[ctr + 3])] = str(int(mode[1]) * int(mode[2]))
                #print(sez)
            except:
                yield None
            ctr += 4
        elif mode[0] == "03" or mode[0] == "3":
            try:
                sez[int(sez[ctr + 1])] = next(inp)
                print("inp:", sez[int(sez[ctr + 1])])
                #print(sez)
            except:
                yield None
            ctr += 2
        elif mode[0] == "04" or mode[0] == "4":
            try:
                #print(sez)
                print("Out:", mode[1])
                yield mode[1]
            except:
                yield None
            ctr += 2
        elif mode[0] == "05" or mode[0] == "5":
            try:
                if mode[1] != "0":
                    ctr = int(mode[2])
                else:
                    ctr += 3
                #print(sez)
            except:
                yield None
        elif mode[0] == "06" or mode[0] == "6":
            try:
                if mode[1] == "0":
                    ctr = int(mode[2])
                else:
                    ctr += 3
                #print(sez)
            except:
                yield None
        elif mode[0] == "07" or mode[0] == "7":
            try:
                if int(mode[1]) < int(mode[2]):
                    sez[int(sez[ctr + 3])] = 1
                else:
                    sez[int(sez[ctr + 3])] = 0
                #print(sez)
            except:
                yield None
            ctr += 4
        elif mode[0] == "08" or mode[0] == "8":
            try:
                if int(mode[1]) == int(mode[2]):
                    sez[int(sez[ctr + 3])] = 1
                else:
                    sez[int(sez[ctr + 3])] = 0
                #print(sez)
            except:
                yield None
            ctr += 4
        else:
            print(sez[ctr], "yote")
            yield None
    yield False

max_sez = []
for i in itertools.permutations([5, 6, 7, 8, 9]):
    inp = inp_gen(i)
    a1 = program3(vsebina_datoteke[:])
    a2 = program3(vsebina_datoteke[:])
    a3 = program3(vsebina_datoteke[:])
    a4 = program3(vsebina_datoteke[:])
    a5 = program3(vsebina_datoteke[:])
    #print(next(inp),"skr")
    last = ""
    #print(a1, "asdfadfad")
    while True:
        c = next(a1)
        print(c, 1)
        if c:
            out(c)
        else:
            break
        c = next(a2)
        print(c, 2)
        if c:
            out(c)
        else:
            break
        c = next(a3)
        print(c, 3)
        if c:
            out(c)
        else:
            break
        c = next(a4)
        print(c, 4)
        if c:
            out(c)
        else:
            break
        c = next(a5)
        print(c, 5)
        if c:
            out(c)
            last = c
            print(last, "js sm last")
        else:
            break
    max_sez.append(int(last))
    o = ["0"]

print(max(max_sez))
odgovor2 = max(max_sez)
with open('day_7_2.out', 'w', encoding='utf-8') as f:
    f.write(str(odgovor2))