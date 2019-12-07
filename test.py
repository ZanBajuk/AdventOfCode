def g(n):
    for i in range(3):
        yield n[0]
        n = n[1:]
        print(n)


sez = [1,2,3,4,5,6,7,8,9,123,1413423]
g1 = g(sez[:])
g2 = g(sez[:])
for i in range(3):
    print(next(g1), next(g2))