
def play(them, me):
    match them:
        case 'A': # Rock
            match me:
                case 'X': # Rock
                    return 'draw'
                case 'Y': # Paper
                    return 'win'
                case 'Z': # Scissors
                    return 'loss'
                case other:
                    pass
        case 'B': # Paper
            match me:
                case 'X': # Rock
                    return 'loss'
                case 'Y': # Paper
                    return 'draw'
                case 'Z': # Scissors
                    return 'win'
                case other:
                    pass
        case 'C': # Scissors
            match me:
                case 'X': # Rock
                    return 'win'
                case 'Y': # Paper
                    return 'loss'
                case 'Z': # Scissors
                    return 'draw'
                case other:
                    pass
        case other:
            pass
    return 'fuck'

def play2(them, result):
    match them:
        case 'A': # Rock
            match result:
                case 'X': # loss
                    return 'Z' # Scissors
                case 'Y': # draw
                    return 'X' # Rock
                case 'Z': # win
                    return 'Y' # Paper
                case other:
                    pass
        case 'B': # Paper
            match result:
                case 'X': # loss
                    return 'X' # Rock
                case 'Y': # draw
                    return 'Y' # Paper
                case 'Z': # win
                    return 'Z' # Scissors
                case other:
                    pass
        case 'C': # Scissors
            match result:
                case 'X': # loss
                    return 'Y' # Paper
                case 'Y': # draw
                    return 'Z' # Scissors
                case 'Z': # win
                    return 'X' # Rock

        case other:
            pass
    return 'fuck'

def freeScore(me):
    match me:
            case 'X':
                return 1
            case 'Y':
                return 2
            case 'Z':
                return 3

with open('./adventOfCode2022/2/input.txt', 'r') as strategy_guide:

    score = 0
    score2 = 0

    for round in strategy_guide:
        them, me = round.split()

        increment = freeScore(me)

        match play(them, me):
            case 'win':
                score = score + 6 + increment
            case 'draw':
                score = score + 3 + increment
            case 'loss':
                score = score + increment
            case other:
                print(other)

        result = me

        match result:
            case 'X': # loss
                pass
            case 'Y': # draw
                score2 = score2 + 3
            case 'Z': # win
                score2 = score2 + 6

        me = play2(them, result)
        score2 = score2 + freeScore(me)

    print(f'strategy guide score: {score}, elf {score2}')


