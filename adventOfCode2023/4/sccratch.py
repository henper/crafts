import re
total_points = 0

winnings = [1]
cards_scratched = 0

with open('./adventOfCode2023/4/example.txt', 'r') as cards:

    for card in cards:
        cards_scratched = cards_scratched + 1
        copies = winnings.pop(0)

        if (copies == 1):
            break

        numbers = re.findall('[0-9]+', card)

        game_no = numbers[0]
        winning = numbers[1:6] # Note: example has 5 winning numbers, input  has 10
        numbers = numbers[6:]

        winners = 0
        for number in numbers:
            if number in winning:
                winners = winners + 1

        if (winners):
            new_cards = [1+copies] * winners

            duplicates = min(len(winnings), len(new_cards))
            for i in range(duplicates):
                winnings[i] = winnings[i] + new_cards.pop(0)

            winnings = winnings + new_cards



print(cards_scratched)
