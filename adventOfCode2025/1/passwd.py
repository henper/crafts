
from example import sequence

pos = 50

passwd = 0

print(f"Start position: {pos:2}.")

for op, val in sequence:
    pre = pos
    if op == '+':
        pos += val
    else:
        pos -= val

    pos %= 100
    n = 0

    print(f"After {op}{val:02}: {pos:2}", end='')

    if n:
        print(f"; during this move we passed zero {n} times.")
    else:
        print(".")

    if pos == 0:
        passwd += 1

print(f"Final position: {pos:2} password: {passwd}")
