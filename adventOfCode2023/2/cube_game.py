
import re

with open('./adventOfCode2023/2/input.txt', 'r') as games:

    invalid_games = set()
    all_games     = set()

    for game in games:
        m = re.search('Game ([0-9]+): (.+)', game)

        game_no = int(m.group(1))
        all_games.add(game_no)

        handfulls = m.group(2)

        for handfull in handfulls.split('; '):
            for cubes in handfull.split(', '):
                m = re.search('([0-9]+) (red|green|blue)', cubes)
                num   = int(m.group(1))
                color = m.group(2)

                match color:
                    case 'red':
                        if num > 12: invalid_games.add(game_no)
                    case 'green':
                        if num > 13: invalid_games.add(game_no)
                    case 'blue':
                        if num > 14: invalid_games.add(game_no)

    print(sum(all_games.difference(invalid_games)))
