from input import dig_instructions

# Ok, so lets paint it
import pygame

# figure out the canvas
S = SCALING = 1

top = 0
left = 0
trenches = []
coords = [(0,0)]

for dig in dig_instructions:
    dir, len, color = dig
    x,y = coords[-1]

    # figure out where to start from and where to go
    match(dir):
        case 'L':
            width  = len * S
            height = S
            left  -= width
            coords.append((x-len, y))
        case 'R':
            width  = len * S
            height = S
            left  += S
            coords.append((x+len, y))
        case 'U':
            width  = S
            height = len * S
            top   -= height
            left  -= S
            coords.append((x, y-len))
        case 'D':
            width  = S
            height = len * S
            top   += S
            left  -= S
            coords.append((x, y+len))

    trenches.append(pygame.Rect(left, top, width, height))

    match(dir):
        case 'L':
            left += S
        case 'R':
            left = left + width
        case 'U':
            pass
        case 'D':
            top = top + height - S

y_offset = abs(min([trench.top  + trench.height for trench in trenches]))
x_offset = abs(min([trench.left + trench.width  for trench in trenches]))

HEIGHT = y_offset + max([trench.top  + trench.height for trench in trenches])
WIDTH  = x_offset + max([trench.left + trench.width  for trench in trenches])

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

perimeter_area = 0
for i, trench in enumerate(trenches):
    color = dig_instructions[i][2]
    pygame.draw.rect(screen, color, trench.move(x_offset, y_offset))
    pygame.display.flip()

    perimeter_area += trench.height/S * trench.width/S

print(f'perimeter_area: {perimeter_area}')

area = 0
import numpy as np
#coords = [(1,6), (3,1), (7,2), (4,4), (8,5)]
coords = np.array(coords)
area = 0
for i in range(1, coords.shape[0]):
    a = np.linalg.det(coords[i-1:i+1])
    area += a
area += np.linalg.det([coords[-1], coords[0]])

print(f'inside area: {area/2}')

# Inside area is the coordinates smack dab in the middle of the squares that the
# trenches are made up of. That means the inside perimeter includes half of the perimeter area.
# and apparently +1 because the starting hole doesn't count
print(f'polygon area: {area/2 + perimeter_area/2 + 1}')

while True:
    event = pygame.event.poll() # get event immediately, if any
    # Allow for ways to exit the application
    if event.type == pygame.QUIT: # closing the (proverbial) window
        pygame.quit(); exit()
    if event.type == pygame.KEYDOWN and event.key == pygame.K_c and pygame.key.get_mods() & pygame.KMOD_CTRL:
        pygame.quit(); exit()

    clock.tick(60)

pygame.quit()
