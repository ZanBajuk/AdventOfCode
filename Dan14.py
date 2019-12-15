with open('day_14.in', encoding='utf-8') as f:
        vsebina_datoteke = f.readlines()
vsebina_datoteke = [x.strip() for x in vsebina_datoteke]
re = [i.split("=>") for i in vsebina_datoteke]
#print(re)
re = [[i[0].split(","),i[1]] for i in re]
#print(re)

memo = {}
po = {"ORE" : 0}
im = {}

def to_dic(s):
    s1 = s[0]
    s2 = s[1]
    d1 = {}
    for i in s1:
        if i[0] == " ":
            i = i[1:]
        j = i.split(" ")
        #print(j, "  d")
        d1[j[1]] = int(j[0])
    if s2[0] == " ":
            s2 = s2[1:]
    j = s2.split(" ")
    im[j[1]] = 0
    return (d1, {j[1] : int(j[0])})
re = [to_dic(i) for i in re]
#print(re)
#print(to_dic([['118 ORE '], ' 7 GTPZ']))

def get_reaction(el):
    for i in re:
        if el in i[1]:
            #print("r:", i)
            return i
    print("wtf", el)

def rabimo(el, am):
    a = get_reaction(el)
    #print(a, "dasfasdfasdfasdfasd")
    if el in im:
        if im[el] >= am:
            po[el] -= am
            im[el] -= am
            return None
        else:
            po[el] -= im[el]
            am -= im[el]
            im[el] = 0
    n = a[1][el]
    t = am // n
    r = 0
    if t * n != am:
        t += 1
        r = (t * n) - am
    #print("hm", am, t, n, r)
    ss = []
    for i in a[0]:
        ss.append((i, t * int(a[0][i])))
    #print("1", ss)
    for i in range(len(ss)):
        if ss[i][0] in im:
            #print(ss[i][0], im[ss[i][0]], ss[i][1])
            if im[ss[i][0]] >= ss[i][1]:
                #print("aamm")
                im[ss[i][0]] += -ss[i][1]
                ss[i] = (ss[i][0], 0)
                #print(i, ss)
            else:
                ss[i] = (ss[i][0],ss[i][1] -im[ss[i][0]])
                im[ss[i][0]] = 0
    #print("tok:", ss)
    for i in ss:
        if i[0] in po:
            po[i[0]] += i[1]
        else:
            po[i[0]] = i[1]
    im[el] = r
    po[el] -= am
    #print(po, im)

def po_to_tuple(im1):
    n = len(im1)
    t = []
    for i in im1:
        t.append((i, im1[i]))
    return tuple(t)


#rabimo("FUEL", 1)
#print(po, im)

#while len(po) != 1 or "ORE" not in po:
#    di = dict(po)
#    for i in di:
#        print(i)
#        if di[i] != 0:
#            if i != "ORE":
#                print("rab", i)
#                rabimo(i,di[i])
#                #po[i] -= di[i]
#    da = dict(po)
#    for i in po:
#       if po[i] == 0:
#            del da[i]
#    po = da
#    print(po, im)
print(im, "ttrt")
def get_fuel(n):
    global po, im
    im = {}
    #if po_to_tuple(im) in memo:
    #    print("DELA!!1")
    #    m = memo[po_to_tuple(im)][0]
    #    im = memo[po_to_tuple(im)][1]
    #    return m
    #n_im = dict(im)
    po = {"FUEL" : n}
    while len(po) != 1 or "ORE" not in po:
        di = dict(po)
        for i in di:
            #print(i)
            if di[i] != 0:
                if i != "ORE":
                    #print("rab", i)
                    rabimo(i,di[i])
                    #po[i] -= di[i]
        da = dict(po)
        for i in po:
            if po[i] == 0 and po[i] != "ORE":
                del da[i]
        po = da
    #memo[po_to_tuple(n_im)] = (po["ORE"],im)
    #print("JJJJ", po_to_tuple(im))
    return po["ORE"]
        #print(po, im)

total = 0
k = 0
#while total < 10 ** 12:
#for i in range(10):
    #k += 1
    #nf = get_fuel()
    #total += nf
    #print(total, k)
    #print("st:", memo)

#print("WOO", po)
#print("WWWWWW", po_to_tuple(im))
print(get_fuel(10000000))
max = 100000000
min = 1
while (max-min) != 1:
    mid = min + (max - min)//2
    o = get_fuel(mid)
    if o < 10 ** 12:
        min = mid
    else:
        max = mid
    print("bi", min, max)
print(min, get_fuel(1))
odgovor1 = get_fuel(1)
odgovor2 = min
with open('day_14_1.out', 'w', encoding='utf-8') as f:
    f.write(str(odgovor1))
with open('day_14_2.out', 'w', encoding='utf-8') as f:
    f.write(str(odgovor2))