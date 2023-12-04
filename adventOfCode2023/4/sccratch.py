import re
total_points = 0


with open('./adventOfCode2023/4/input.txt', 'r') as cards:

    cards = cards.readlines()
    winnings = [1] * len(cards)
    tot_cards = []

    for card in cards:
        copies = winnings.pop(0)
        tot_cards.append(copies)

        numbers = re.findall('[0-9]+', card)

        game_no = numbers[0]
        winning = numbers[1:11] # Note: example has 5 winning numbers, input  has 10
        numbers = numbers[11:]

        winners = 0
        for number in numbers:
            if number in winning:
                winners = winners + 1

        for winner in range(winners):
            winnings[winner] = winnings[winner] + copies




print(sum(tot_cards))

