
import re

with open('./adventOfCode2023/2/example.txt', 'r') as games:

    invalid_games = set()
    all_games     = set()

    powers = []

    for game in games:
        m = re.search('Game ([0-9]+): (.+)', game)

        game_no = int(m.group(1))
        all_games.add(game_no)

        min = {'red': 0, 'green': 0, 'blue': 0}

        handfulls = m.group(2)

        for handfull in handfulls.split('; '):
            for cubes in handfull.split(', '):
                m = re.search('([0-9]+) (red|green|blue)', cubes)
                num   = int(m.group(1))
                color = m.group(2)

                if (min[color] < num):
                    min[color] = num

        powers.append(min['red'] * min['green'] * min['blue'])

    print(sum(powers))
