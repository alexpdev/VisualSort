import random

combos = {
    0: [0], 1: [1], 2: [2], 3: [0,1], 4: [0,2], 5: [1,2]
}

START = "#4F7FA4"

def plus(start, index):
    if int(start[index], 16) != 255:
        start[index] = hex(int(start[index], 16) + 1)[2:].upper().rjust(2,"0")
    else:
        raise Exception

def minus(start, index):
    if int(start[index], 16) != 0:
        start[index] = hex(int(start[index], 16) - 1)[2:].upper().rjust(2,"0")
    else:
        raise Exception

def getfigs(start):
    choices = combos[random.randint(0,5)]
    directions = []
    for i in choices:
        if start[i] == "FF":
            directions.append(0)
        elif start[i] == "00":
            directions.append(1)
        else:
            directions.append(random.randint(0,1))
    return directions, choices

def gradgen(start=START, count=5):
    start = [start[1:3], start[3:5], start[5:]]
    choices, direction = getfigs(start)
    while True:
        for i,x in enumerate(choices):
            for _ in range(count):
                if direction[i]:
                    try:
                        plus(start, x)
                    except Exception:
                        choices, direction = getfigs(start)
                        break
                else:
                    try:
                        minus(start, x)
                    except Exception:
                        choices, direction = getfigs(start)
                        break
            yield "".join(["#", *start])
