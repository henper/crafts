import re

my_dict = {}

alphabet = "abcdefghijklmnopqrstuvwxyz"
for letter in alphabet:
    my_dict[letter] = None

no_letters = str.maketrans(my_dict)


decoded_calibrations = []
with open('./adventOfCode2023/1/input.txt', 'r') as calibrations:
    for calibration in calibrations:
        digits = calibration.rstrip().lower().translate(no_letters)
        decoded_calibrations.append(int(digits[0] + digits[-1]))

print(sum(decoded_calibrations))
