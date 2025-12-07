import pygame
from pygame.math import Vector2

from input import tachyon_manifolds

# figure out the canvas
S = SCALING = 10
HEIGHT = len(tachyon_manifolds) * S
WIDTH  = len(tachyon_manifolds[0]) * S

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Draw a timelines counter
TEXT = (255,255,255)
font = pygame.font.Font(None, S*6)
timeline_counter = font.render('Timelines: ' + '0000000000000000', True, TEXT)
timeline_counter_rect = timeline_counter.get_rect()
timeline_counter_rect.topleft = (0,0)
screen.blit(timeline_counter, timeline_counter_rect)

clock = pygame.time.Clock()

# create a polygon of a splitter (upside down Y-shape)
splitter_coords = [Vector2( -1/4 * S,   0 * S),
                   Vector2( -1/4 * S, 1/4 * S),
                   Vector2(-5/4 * S, 3/4 * S),
                   Vector2(-5/4 * S,   1 * S),
                   Vector2(-3/4 * S,   1 * S),
                   Vector2(-3/4 * S, 3/4 * S),
                   Vector2(   0 * S, 3/8 * S),
                   Vector2(   0 * S,   0 * S)]

reflection = [p.reflect(Vector2(1 * S, 0)) for p in splitter_coords]
splitter_coords += reflection
splitter_coords = [a+b for a, b in zip(splitter_coords, [Vector2(S/2,0)]*len(splitter_coords))]

SPLITTER_COLOR = pygame.Color('aquamarine')

def draw_splitter(s):
    x,y = s
    coord = Vector2(x*S, y*S)
    pygame.draw.polygon(screen, SPLITTER_COLOR, [a+b for a, b in zip(splitter_coords, [coord]*len(splitter_coords))])

# Find and draw the splitters
splitters = []
start = ()
for x in range(len(tachyon_manifolds[0])):
    for y in range(len(tachyon_manifolds)):

        if tachyon_manifolds[y][x] == '^':
            splitters.append((x,y))

        if tachyon_manifolds[y][x] == 'S':
            start = (x,y)


for splitter in splitters:
    draw_splitter(splitter)


BEAM_COLOR = pygame.Color('darkorchid1')

def draw_beam(b):
    x,y = b
    beam_rect = pygame.Rect(((x+1/4)*S, y*S), (S/2, S))
    pygame.draw.rect(screen, BEAM_COLOR, beam_rect)


# Draw the starting beam
draw_beam((start[0], start[1]))

beams = list()
beams.append(start)
timelines = [1]

splits = 0

started = False

while(True):
    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        break
    if event.type == pygame.KEYDOWN and event.key == pygame.K_c and pygame.key.get_mods() & pygame.KMOD_CTRL:
        break

    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
        started = True
        continue


    pygame.display.flip()
    clock.tick()

    if not started:
        continue

    # Draw the timelines counter
    timeline_counter = font.render('Timelines: ' + str(sum(timelines)), True, TEXT)
    screen.fill((0,0,0), timeline_counter_rect)
    screen.blit(timeline_counter, timeline_counter_rect)


    # Move all the beams down
    next_beams = list()
    next_timelines = list()
    for i, beam in enumerate(beams):
        x,y = beam

        tb = (x, y + 1)

        if tb in splitters:
            x,y = tb
            next_beams.append((x-1, y))
            next_beams.append((x+1, y))

            next_timelines.append(timelines[i])
            next_timelines.append(timelines[i])

            splits += 1
        else:
            next_beams.append(tb)
            next_timelines.append(timelines[i])
            draw_beam(tb)

    # Reduce the number of beams by finding duplicates and adding their timelines
    beams.clear()

    while len(beams) != len(next_beams):

        beams = next_beams
        timelines = next_timelines

        for i, beam in enumerate(beams):

            try:
                j = beams[i+1:].index(beam) + i + 1

                timelines[i] = timelines[i] + timelines[j]

                next_beams.pop(j)
                next_timelines.pop(j)
            except ValueError:
                continue



print(f'Beam splits: {splits}, total beams: {len(beams)}, total timelines: {sum(timelines)}')
pygame.quit(); exit()
