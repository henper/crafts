import pygame

warehouse = [
    '########',
    '#..O.O.#',
    '##@.O..#',
    '#...O..#',
    '#.#.O..#',
    '#...O..#',
    '#......#',
    '########',
]

moves = '<^^>>>vv<v>>v<<'

warehouse = [
    '#######',
    '#...#.#',
    '#.....#',
    '#..OO@#',
    '#..O..#',
    '#.....#',
    '#######',
]

moves = '<vv<<^^<<^^'

warehouse = [
    '##########',
    '#..O..O.O#',
    '#......O.#',
    '#.OO..O.O#',
    '#..O@..O.#',
    '#O#..O...#',
    '#O..O..O.#',
    '#.OO.O.OO#',
    '#....O...#',
    '##########',
]

moves = '<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^' \
        'vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v' \
        '><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<' \
        '<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^' \
        '^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><' \
        '^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^' \
        '>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^' \
        '<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>' \
        '^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>' \
        'v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^'

warehouse = [
    '######',
    '#....#',
    '#.O..#',
    '#.OO@#',
    '#.O..#',
    '#....#',
    '######',
]

moves = '<vv<<^'

from input import warehouse, moves

moves = moves + moves

# set up rects
SCALE = S = 16

width  = len(warehouse[0])
height = len(warehouse)

walls = []
boxes = []
robot = None
for y in range(height):
    for x in range(width):
        if warehouse[y][x] == '#':
            walls.append(pygame.Rect(x*S*2, y*S, S*2, S))
        if warehouse[y][x] == 'O':
            boxes.append(pygame.Rect(x*S*2, y*S, S*2, S))
        if warehouse[y][x] == '@':
            robot = pygame.Rect(x*S*2, y*S, S, S)


# Visualization
pygame.init()
screen = pygame.display.set_mode((width*SCALE*2,height*SCALE))
screen.fill("black")
clock  = pygame.time.Clock()



def draw_border(r : pygame.Rect, color, T = S//10):
    pygame.draw.rect(screen, color, pygame.Rect(r.left,    r.top, T, r.height))
    pygame.draw.rect(screen, color, pygame.Rect(r.right-T, r.top, T, r.height))
    pygame.draw.rect(screen, color, pygame.Rect(r.left, r.top,      r.width, T))
    pygame.draw.rect(screen, color, pygame.Rect(r.left, r.bottom-T, r.width, T))

for wall in walls:
    pygame.draw.rect(screen, "green", wall)

for box in boxes:
    pygame.draw.rect(screen, "yellow", box)
    draw_border(box, "brown", S//5)

pygame.draw.rect(screen, "purple", robot)
pygame.display.flip()

halted = True
while halted:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            halted = False

def trainer(dx, dy, colliders: list[pygame.Rect]) -> list[pygame.Rect]:
    collisions = []
    for collider in colliders:
        if dx == 0:
            collider = collider.move(dx, dy)
        elif dx == -S:
            collider = pygame.Rect(collider.left + dx, collider.top, S, S)
        else:
            collider = pygame.Rect(collider.right, collider.top, S, S)

        for box in boxes:
            if box in collisions:
                continue

            if (collider.colliderect(box)):
                collisions.append(box)

    return collisions


for move in moves:
    dx, dy = 0,0
    if move == '^':
        dy = -1 * S
    if move == 'v':
        dy =  1 * S
    if move == '<':
        dx = -1 * S
    if move == '>':
        dx =  1 * S

    if robot.move(dx,dy).collidelist(walls) != -1:
        continue

    colliders = []
    new = trainer(dx,dy, [robot])

    # get all the boxes in a straight line from where we are
    while new:
        colliders += new
        new = trainer(dx,dy, new)

    wall_hit = False
    for collider in colliders:

        moved = collider.move(dx,dy)

        #draw_border(moved, "blue")
        #pygame.display.flip()

        if moved.collidelist(walls) != -1:
            wall_hit = True
            break

    #pygame.display.flip()

    if wall_hit:
        continue

    # update the position of the robot and all boxes
    colliders.reverse()
    for collider in colliders:
        i =  boxes.index(collider)
        pygame.draw.rect(screen, "black", collider)
        collider.move_ip(dx, dy)
        pygame.draw.rect(screen, "yellow", collider)
        draw_border(collider, "brown", S//5)
        pygame.display.flip()

    pygame.draw.rect(screen, "black", robot)
    robot.move_ip(dx,dy)
    pygame.draw.rect(screen, "purple", robot)

    pygame.display.flip()
    pass

gps = []
for box in boxes:
    gps.append(box.x//S + box.y//S * 100)
print(sum(gps))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    clock.tick(60)