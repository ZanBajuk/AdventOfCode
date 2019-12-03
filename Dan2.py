with open('day_2.in', encoding='utf-8') as f:
        vsebina_datoteke = f.read()
vsebina_datoteke = vsebina_datoteke.split(",")
vsebina_datoteke = [int(i) for i in vsebina_datoteke]
#print(vsebina_datoteke)

def program(sez):
    ctr = 0
    mode = 0
    last = len(sez)
    while ctr < last:
        mode = sez[ctr]
        if mode == 99:
            return sez
        elif mode == 1:
            try:
                sez[sez[ctr + 3]] = sez[sez[ctr + 1]] + sez[sez[ctr + 2]]
            except:
                return None
        elif mode == 2:
            try:
                sez[sez[ctr + 3]] = sez[sez[ctr + 1]] * sez[sez[ctr + 2]]
            except:
                return None
        else:
            return None
        ctr += 4
    return sez

def program_alarm(sez):
    try:
        sez[1] = 12
        sez[2] = 2
        return program(sez)
    except:
        return None

def program_with_verb_and_noun(sez, verb, noun):
    try:
        sez[1] = noun
        sez[2] = verb
        return program(sez)
    except:
        return None

def prog2(sez):
    for i in range(100):
        for j in range(100):
            #print(program_with_verb_and_noun(sez[:], i, j))
            if program_with_verb_and_noun(sez[:], i, j)[0] == 19690720:
                return 100 * j + i

odgovor1 = program_alarm(vsebina_datoteke[:])[0]
with open('day_2_1.out', 'w', encoding='utf-8') as f:
    f.write(str(odgovor1))

odgovor2 = prog2(vsebina_datoteke[:])
with open('day_2_2.out', 'w', encoding='utf-8') as f:
    f.write(str(odgovor2))