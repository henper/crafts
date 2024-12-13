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
#from marcus import machines

def pythagoras(a, b):
    return np.sqrt(a**2 + b**2)

cost = []

for machine in machines:
    a, b, price = machine

    X,Y = price
    Xa, Ya = a
    Xb, Yb = b

    b = (X*Yb)/Y - Xb
    a = Xa - (X*Ya)/Y

    winner = False

    for A in range(1,100):
        B = A*a/b
        if B.is_integer():
            B = int(np.round(B))

            # found a winner!
            winner = True

            # Find how many times we need multiply our perfectly angled vector
            # to get the same length as the price

            p = X**2 + Y**2
            v = (A*Xa + B*Xb)**2 + (A*Ya + B*Yb)**2
            s = np.sqrt(p//v)

            if not s.is_integer():
                break

            s = int(np.round(s))

            c = s*(3*A+B)

            cost.append(c)
            break

    if winner:
        continue

    for B in range(1,100):
        A = B*b/a
        if A.is_integer():
            A = int(np.round(A))

            # found a winner!
            winner = True

            # Find how many times we need multiply our perfectly angled vector
            # to get the same length as the price

            p = X**2 + Y**2
            v = (A*Xa + B*Xb)**2 + (A*Ya + B*Yb)**2
            s = np.sqrt(p//v)

            if not s.is_integer():
                break

            s = int(np.round(s))

            c = s*(3*A+B)

            cost.append(c)
            break


print(sum(cost))


# Too low 14157
# Not rit 17490
# Too low 24488

35729
18335