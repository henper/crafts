

def rotate(matrix):

    # create a 7x7 grid, each with a _unique_ element (and not just 7x7 references to the same period)
    rotated = [['.','.','.','.','.','.','.'],
               ['.','.','.','.','.','.','.'],
               ['.','.','.','.','.','.','.'],
               ['.','.','.','.','.','.','.'],
               ['.','.','.','.','.','.','.'],
               ['.','.','.','.','.','.','.'],
               ['.','.','.','.','.','.','.'],]

    '''
            0 1 2 3 4 5 6
          0 S---->S---->S
          1 ^ A-->A-->A
          2 | ^ M M M
          3 S A M X M A S
          4 ^ ^ M M M
          5 | A   A   A
          6 S     S     S
    '''
    # creamy center
    rotated[3][3] = matrix[3][3]

    # left up diagonal to upwards
    rotated[0][3] = matrix[0][0]
    rotated[1][3] = matrix[1][1]
    rotated[2][3] = matrix[2][2]

    # upwards to right up diagonal
    rotated[0][6] = matrix[0][3]
    rotated[1][5] = matrix[1][3]
    rotated[2][4] = matrix[2][3]

    # right up diagonal to forwards
    rotated[3][6] = matrix[0][6]
    rotated[3][5] = matrix[1][5]
    rotated[3][4] = matrix[2][4]

    # forwards to down right diagonal
    rotated[4][4] = matrix[3][4]
    rotated[5][5] = matrix[3][5]
    rotated[6][6] = matrix[3][6]

    # down right diagonal to downwards
    rotated[4][3] = matrix[4][4]
    rotated[5][3] = matrix[5][5]
    rotated[6][3] = matrix[6][6]

    # downwards to left down diagonal
    rotated[4][2] = matrix[4][3]
    rotated[5][1] = matrix[5][3]
    rotated[6][0] = matrix[6][3]

    # left down diagonal to backwards
    rotated[3][2] = matrix[4][2]
    rotated[3][1] = matrix[5][1]
    rotated[3][0] = matrix[6][0]

    # backwards to left up diagonal
    rotated[0][0] = matrix[3][0]
    rotated[1][1] = matrix[3][1]
    rotated[2][2] = matrix[3][2]

    return rotated


m = ['.......',
     '.......',
     '.......',
     '...X...',
     '....M..',
     '.....A.',
     '......S',]


for i in range(8):
    m = rotate(m)

    for j in range(7):
        print(' '.join(m[j][:]), end='')
        print('')

    print('')
    print('')


def count_xmases(matrix) -> int:
    '''
    Given a 7x7 matrix of a word jumble,
    count how many times the word 'XMAS' appears starting from the center
    '''
    count = 0

    if matrix[3][3] != 'X':
        return 0

    # Forwards
    if matrix[3][3:] == 'XMAS':
        count += 1

    for i in range(7):
        matrix = rotate(matrix)
        s = ''.join(matrix[3][3:])
        if s == 'XMAS':
            count += 1

    return count

def count_x_mases(matrix) -> int:
    '''
    Given a 7x7 matrix of a word jumble,
    count how many times the word 'XMAS' appears starting from the center
    '''
    count = 0

    if matrix[3][3] != 'A':
        return 0

    # Cross
    '''
    s = matrix[3][2:5]
    if s == 'MAS' or s == 'SAM':
        matrix = rotate(rotate(matrix))
        s = ''.join(matrix[3][2:5])
        if s == 'MAS' or s == 'SAM':
            count = 1
    '''

    matrix = rotate(matrix)

    s = ''.join(matrix[3][2:5])
    if s == 'MAS' or s == 'SAM':
        matrix = rotate(rotate(matrix))
        s = ''.join(matrix[3][2:5])
        if s == 'MAS' or s == 'SAM':
            count += 1

    return count

jumble = [
    '................',
    '................',
    '................',
    '....M.S.........',
    '.....A..MSMS....',
    '....M.S.MAA.....',
    '.....A.ASMSM....',
    '....M.S.M.......',
    '................',
    '...S.S.S.S.S....',
    '....A.A.A.A.....',
    '...M.M.M.M.M....',
    '................',
    '................',
    '................',
    '................',
]

jumble = [
    '................',
    '................',
    '................',
    '...MMMSXXMASM...',
    '...MSAMXMSMSA...',
    '...AMXSXMAAMM...',
    '...MSAMASMSMX...',
    '...XMASAMXAMM...',
    '...XXAMMXXAMA...',
    '...SMSMSASXSS...',
    '...SAXAMASAAA...',
    '...MAMMMXMMMM...',
    '...MXMXAXMASX...',
    '................',
    '................',
    '................',
]

from input import jumble

height = len(jumble)
width  = len(jumble[0])

num_xmases = 0

for yp in range(3, height-3):
    for xp in range(3, width-3):

        y = yp - 3
        x = xp - 3

        matrix = [
            jumble[y+0][x:x+7],
            jumble[y+1][x:x+7],
            jumble[y+2][x:x+7],
            jumble[y+3][x:x+7],
            jumble[y+4][x:x+7],
            jumble[y+5][x:x+7],
            jumble[y+6][x:x+7],
        ]

        if (matrix[3][3]=='A'):
            for j in range(2,5):
                print(' '.join(matrix[j][2:5]))

            is_x_mas = count_x_mases(matrix)

            if is_x_mas:
                print('x-mas')
            else:
                print('')

            print('')

            num_xmases += is_x_mas

print(num_xmases)



# 4011 Too High
# 1907 Too High
# 1913 Too High


