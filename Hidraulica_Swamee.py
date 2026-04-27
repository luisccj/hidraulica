import math

e = .1 #mm
d = 320 * 10 ** -3 #m
v = (11 / 1000) / (.25 * math.pi * d ** 2) #m3/s
ni = .000001 # m2/s


re = v * d / ni
print("O Reynolds é ", re)

## Swamee - Jain (1967)
def fsj(e,D,Re):
    return .25 / (math.log(((e / (3.7 * D)) + (5.74 / (Re ** 0.9))),10) ** 2)

print("O f de Swamee-Jain é ", fsj(.1, 320, 43768))


## Swamee (1993)
def fse(e,D,Re):
    p1 = (64/Re) ** 8
    p2 = e / (3.7 * D)
    p3 = 5.74 / (Re ** .9)
    p4 = (2500 / Re) ** 6
    p5 = 9.5 * (math.log((p2 + p3 - p4),math.e) ** -16)
    return ((p1 + p5) ** .125)

print("O f de Swamee é ", fse(.1, 320, 43768))


