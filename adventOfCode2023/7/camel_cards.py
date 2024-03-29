from input import game

from enum import Enum
class Type(Enum):
    HIGH_CARD       = 1
    ONE_PAIR        = 2
    TWO_PAIR        = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE      = 5
    FOUR_OF_A_KIND  = 6
    FIVE_OF_A_KIND  = 7

    def determine(cards):
        s = set(cards)


        jokers = cards.count('J')

        match len(s):
            case 1:
                return Type.FIVE_OF_A_KIND
            case 2:
                # four of a kind or full house
                i = cards.count(s.pop())
                if i == 2 or i == 3:
                    if(jokers):
                        return Type.FIVE_OF_A_KIND
                    return Type.FULL_HOUSE

                if (jokers): # one or four
                    return Type.FIVE_OF_A_KIND

                return Type.FOUR_OF_A_KIND
            case 3:
                # three of a kind or two pair
                for c in s:
                    if cards.count(c) == 3:
                        if (jokers): # only one or three possible, 2 would have been categorized as a full house
                            return Type.FOUR_OF_A_KIND
                        return Type.THREE_OF_A_KIND

                if (jokers == 1):
                    return Type.FULL_HOUSE
                if (jokers == 2):
                    return Type.FOUR_OF_A_KIND
                return Type.TWO_PAIR
            case 4:
                if (jokers):
                    return Type.THREE_OF_A_KIND
                return Type.ONE_PAIR
            case 5:
                if (jokers): # can only be one, otherwise they'd be a pair
                    return Type.ONE_PAIR
                return Type.HIGH_CARD

class Hand():

    def __init__(self, cards: str, bid: int):
        self.cards = cards
        self.bid   = bid
        self.type  = Type.determine(cards)

    def __lt__(self, other):
        if (self.type == other.type):
            for i in range(len(self.cards)):
                if self.cards[i] == other.cards[i]:
                    continue

                deck = ['A','K','Q','T','9','8','7','6','5','4','3','2','J']
                deck.reverse()
                val = deck.index(self.cards[i]) < deck.index(other.cards[i])
                return val


        return self.type.value < other.type.value



hands = [Hand(cards, bid) for cards, bid in game]

hands.sort()

answer = 0
for rank, hand in enumerate(hands):
    answer += (rank + 1) * hand.bid

print(answer)
