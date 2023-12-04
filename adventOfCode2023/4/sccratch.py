import re
total_points = 0

with open('./adventOfCode2023/4/input.txt', 'r') as cards:

    for card in cards:

        numbers = re.findall('[0-9]+', card)

        game_no = numbers[0]
        winning = numbers[1:11] # Note: example has 5 winning numbers
        numbers = numbers[11:]

        winners = 0
        for number in numbers:
            if number in winning:
                winners = winners + 1

        if (winners):
            points = pow(2, (winners-1))
            total_points = total_points + points

print(total_points)
