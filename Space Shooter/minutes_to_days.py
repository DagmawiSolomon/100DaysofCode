def duration(integer):
    days = integer // 1440
    hours = integer % 1440 // 60
    minutes = integer % 1440 % 60
    return (days,hours,minutes)

def next_second(tuple):
    t = []
    for i in tuple:
        t.append(i)
    if t[-1] < 59:
        t[-1] += 1
    if t[-1] >= 59:
        t[-1] = 0
        if t[-2] < 59:
            t[-2] += 1
        elif t[-2] >= 59:
            t[-2] = 0
            if t[-3] < 23:
                t[-3] += 1
            elif t[-3] >= 23:
                t[-3] = 0

    tup = (t[0], t[1], t[2])
    return tup


x = next_second((23,10,59))
print(x)

