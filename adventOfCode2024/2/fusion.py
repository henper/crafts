import numpy as np

reports = [
[7, 6, 4, 2, 1],
[1, 2, 7, 8, 9],
[9, 7, 6, 2, 1],
[1, 3, 2, 4, 5],
[8, 6, 4, 4, 1],
[1, 3, 6, 7, 9],
]

from input import reports

num_safe = 0




def is_safe(report):
    forwards = report.copy()
    forwards.sort()

    backwards = forwards.copy()
    backwards.reverse()

    if forwards == report or backwards == report:

        off_by_one = report[0:-1]


        gradient = abs(np.array(report[1:]) - np.array(off_by_one))

        least = min(gradient)
        most = max(gradient)

        if least > 0 and most < 4:
            return True

    return False


for report in reports:
    if is_safe(report):
        num_safe += 1
    else:

        for i, r in enumerate(report):
            dampened = report.copy()
            dampened.pop(i)

            if is_safe(dampened):
                num_safe += 1
                break




print(num_safe)
