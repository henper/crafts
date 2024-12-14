import numpy as np


machines =  [(
    (94, 34),
    (22, 67),
    (8400, 5400),
), (
    (26, 66),
    (67, 21),
    (12748, 12176),
), (
    (17, 86),
    (84, 37),
    (7870, 6450),
), (
    (69, 23),
    (27, 71),
    (18641, 10279),
)]

from input import machines

def pythagoras(a, b):
    return np.sqrt(a**2 + b**2)

cost = []

def is_int(x: float) -> bool:
    if x < 1.0:
        return False

    if x.is_integer():
        return True

    f = x - int(x)

    return f < 0.0001 or f > 0.9999

for machine in machines:
    a, b, price = machine

    X,Y = price
    #X += 10000000000000
    #Y += 10000000000000

    Xa, Ya = a
    Xb, Yb = b

    b = (X*Yb)/Y - Xb
    a = Xa - (X*Ya)/Y

    winner = False

    for A in range(1, 100):
        B = A*a/b

        Dx = X/(A*Xa + B*Xb)
        Dy = Y/(A*Ya + B*Yb)

        if is_int(Dx) and abs(Dx-Dy) < 0.0001:
            s = int(np.round(Dx))
            c = s*(3*A+B)

            if not is_int(c):
                continue

            cost.append(c)
            break


'''
        if is_int(B):
            B = int(np.round(B))

            # found a winner!
            winner = True

            # Find how many times we need multiply our perfectly angled vector
            # to get the same length as the price

            p = X**2 + Y**2
            v = (A*Xa + B*Xb)**2 + (A*Ya + B*Yb)**2
            s = np.sqrt(p//v)

            if not is_int(s):
                break

            s = int(np.round(s))

            c = s*(3*A+B)

            cost.append(c)
            break

    if winner:
        continue

    for B in range(1,100):
        A = B*b/a
        if is_int(A):
            A = int(np.round(A))

            # found a winner!
            winner = True

            # Find how many times we need multiply our perfectly angled vector
            # to get the same length as the price

            p = X**2 + Y**2
            v = (A*Xa + B*Xb)**2 + (A*Ya + B*Yb)**2
            s = np.sqrt(p//v)

            if not is_int(s):
                break

            s = int(np.round(s))

            c = s*(3*A+B)

            cost.append(c)
            break
'''

print(sum(cost))


# Too low 14157
# Not rit 17490
# Too low 24488

35729
18335