with open('day_8.in', encoding='utf-8') as f:
        vsebina_datoteke = f.read()
x, y = 25, 6
#print(x, y)
plasti = []
l = len(vsebina_datoteke)
st_plasti = int(l/(x*y))
#print(vsebina_datoteke[0:100])
for i in range(st_plasti):
    #print(vsebina_datoteke[i*(x*y):(i+1)*(x*y)])
    plasti.append(vsebina_datoteke[i*(x*y):(i+1)*(x*y)])
min_plasti = [i.count("0") for i in plasti]
min_plast = min_plasti.index(min(min_plasti))
odgovor1 =(plasti[min_plast].count("1") * plasti[min_plast].count("2"))
with open('day_8_1.out', 'w', encoding='utf-8') as f:
    f.write(odgovor1)
def ret_pixel(n):
    for i in range(st_plasti):
        if plasti[i][n] != "2":
            return plasti[i][n]

image = ""
for i in range(x*y):
    image += ret_pixel(i)
image = image.replace("0", ".").replace("1", "X")
image = ["\n" + image[j*(x):(j+1)*(x)] for j in range(y)]
print(image)
with open('day_8_2.out', 'w', encoding='utf-8') as f:
    f.writelines(image)