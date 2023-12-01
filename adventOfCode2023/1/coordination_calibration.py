import re

my_other_dict = { 'one': 'o1e',
                  'two': 't2o',
                'three': 't3e',
                 'four': 'f4r',
                 'five': 'f5e',
                  'six': 's6x',
                'seven': 's7n',
                'eight': 'e8t',
                 'nine': 'n9e'}

my_dict = {}
alphabet = "abcdefghijklmnopqrstuvwxyz"
for letter in alphabet:
    my_dict[letter] = None

no_letters = str.maketrans(my_dict)


decoded_calibrations = []
with open('./adventOfCode2023/1/input.txt', 'r') as calibrations:
    for calibration in calibrations:

        match = re.search('(one|two|three|four|five|six|seven|eight|nine)', calibration)

        while match:
            calibration = calibration.lower().replace(match.group(1), my_other_dict[match.group(1)])
            match = re.search('(one|two|three|four|five|six|seven|eight|nine)', calibration)


        digits = calibration.rstrip().lower().translate(no_letters)
        decoded_calibrations.append(int(digits[0] + digits[-1]))

print(sum(decoded_calibrations))
