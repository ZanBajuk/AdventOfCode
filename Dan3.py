vsebina_datoteke = ""
with open('day_3.in', encoding='utf-8') as f:
        vsebina_datoteke = f.readlines()
vsebina_datoteke = [x.strip() for x in vsebina_datoteke]
vsebina_datoteke = [i.split(",") for i in vsebina_datoteke]
#print(vsebina_datoteke)

set_of_wires = set()
set_of_crossings = set()

def set_wire1_locations(sez):
    current_loc = (0, 0)
    for i in sez:
        if i[0] == "L":
            for i in range(1, int(i[1:]) + 1):
                current_loc = (current_loc[0] - 1, current_loc[1])
                set_of_wires.add(current_loc)
        elif i[0] == "R":
            for i in range(1, int(i[1:]) + 1):
                current_loc = (current_loc[0] + 1, current_loc[1])
                set_of_wires.add(current_loc)
        elif i[0] == "U":
            for i in range(1, int(i[1:]) + 1):
                current_loc = (current_loc[0], current_loc[1] + 1)
                set_of_wires.add(current_loc)
        else:
            for i in range(1, int(i[1:]) + 1):
                current_loc = (current_loc[0], current_loc[1] - 1)
                set_of_wires.add(current_loc)
    if (0,0) in set_of_wires:
        set_of_wires.remove((0, 0))

def get_crossings(sez):
    current_loc = (0, 0)
    for i in sez:
        if i[0] == "L":
            for i in range(1, int(i[1:]) + 1):
                current_loc = (current_loc[0] - 1, current_loc[1])
                if current_loc in set_of_wires:
                    set_of_crossings.add(current_loc)
        elif i[0] == "R":
            for i in range(1, int(i[1:]) + 1):
                current_loc = (current_loc[0] + 1, current_loc[1])
                if current_loc in set_of_wires:
                    set_of_crossings.add(current_loc)
        elif i[0] == "U":
            for i in range(1, int(i[1:]) + 1):
                current_loc = (current_loc[0], current_loc[1] + 1)
                if current_loc in set_of_wires:
                    set_of_crossings.add(current_loc)
        else:
            for i in range(1, int(i[1:]) + 1):
                current_loc = (current_loc[0], current_loc[1] - 1)
                if current_loc in set_of_wires:
                    set_of_crossings.add(current_loc)
    if (0,0) in set_of_wires:
        sset_of_wires.remove((0, 0))

def get_closest():
    try:
        min1 = abs(set_of_crossings[0][0]) + abs(set_of_crossings[0][1])
        min2 = set_of_crossings[0]
        for i in set_of_crossings[1:]:
            if abs(i[0]) + abs(i[1]) < min1:
                min1 = abs(i[0]) + abs(i[1])
                min2 = i
        return min1
    except:
        return None


set_wire1_locations(vsebina_datoteke[0])
get_crossings(vsebina_datoteke[1])
set_of_crossings = list(set_of_crossings)
odgovor1 = get_closest()
with open('day_3_1.out', 'w', encoding='utf-8') as f:
    f.write(str(odgovor1))
            
set_of_wires2 = set()
set_of_wires_and_steps = set()
set_of_crossings_and_steps = set()

def set_wire1_locations_and_steps(sez):
    current_loc = (0, 0)
    steps = 0
    for i in sez:
        if i[0] == "L":
            for i in range(1, int(i[1:]) + 1):
                current_loc = (current_loc[0] - 1, current_loc[1])
                steps += 1
                if (not (current_loc in set_of_wires2)) and (current_loc != (0,0)):
                    set_of_wires2.add(current_loc)
                    set_of_wires_and_steps.add((current_loc, steps))
        elif i[0] == "R":
            for i in range(1, int(i[1:]) + 1):
                current_loc = (current_loc[0] + 1, current_loc[1])
                steps += 1
                if (not (current_loc in set_of_wires2)) and (current_loc != (0,0)):
                    set_of_wires2.add(current_loc)
                    set_of_wires_and_steps.add((current_loc, steps))
        elif i[0] == "U":
            for i in range(1, int(i[1:]) + 1):
                current_loc = (current_loc[0], current_loc[1] + 1)
                steps += 1
                if (not (current_loc in set_of_wires2)) and (current_loc != (0,0)):
                    set_of_wires2.add(current_loc)
                    set_of_wires_and_steps.add((current_loc, steps))
        else:
            for i in range(1, int(i[1:]) + 1):
                current_loc = (current_loc[0], current_loc[1] - 1)
                steps += 1
                if (not (current_loc in set_of_wires2)) and (current_loc != (0,0)):
                    set_of_wires2.add(current_loc)
                    set_of_wires_and_steps.add((current_loc, steps))

def get_crossings_and_steps(sez):
    steps = 0
    current_loc = (0, 0)
    for i in sez:
        if i[0] == "L":
            for i in range(1, int(i[1:]) + 1):
                steps += 1
                current_loc = (current_loc[0] - 1, current_loc[1])
                if current_loc in set_of_wires2:
                    set_of_crossings_and_steps.add(steps + poisci(set_of_wires_and_steps, current_loc))
        elif i[0] == "R":
            for i in range(1, int(i[1:]) + 1):
                steps += 1
                current_loc = (current_loc[0] + 1, current_loc[1])
                if current_loc in set_of_wires2:
                    set_of_crossings_and_steps.add(steps + poisci(set_of_wires_and_steps, current_loc))
        elif i[0] == "U":
            for i in range(1, int(i[1:]) + 1):
                steps += 1
                current_loc = (current_loc[0], current_loc[1] + 1)
                if current_loc in set_of_wires2:
                    set_of_crossings_and_steps.add(steps + poisci(set_of_wires_and_steps, current_loc))
        else:
            for i in range(1, int(i[1:]) + 1):
                steps += 1
                current_loc = (current_loc[0], current_loc[1] - 1)
                if current_loc in set_of_wires2:
                    set_of_crossings_and_steps.add(steps + poisci(set_of_wires_and_steps, current_loc))


def get_closest2():
    return min(set_of_crossings_and_steps)

def poisci(sez, loc):
    for i in sez:
        if i[0] == loc:
            return i[1]

set_wire1_locations_and_steps(vsebina_datoteke[0])
#print(set_of_wires_and_steps)
get_crossings_and_steps(vsebina_datoteke[1])

odgovor2 = get_closest2()
with open('day_3_2.out', 'w', encoding='utf-8') as f:
    f.write(str(odgovor2))