import pygame
from pygame.math import Vector2

from example import tachyon_manifolds

# figure out the canvas
S = SCALING = 100
HEIGHT = len(tachyon_manifolds) * S
WIDTH  = len(tachyon_manifolds[0]) * S

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

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

# Draw the starting beam
BEAM_COLOR = pygame.Color('darkorchid1')
x,y = start
beam_rect = pygame.Rect(((x+1/4)*S, y*S), (S/2, S))
pygame.draw.rect(screen, BEAM_COLOR, beam_rect)

while(True):
    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        pygame.quit(); exit()
    if event.type == pygame.KEYDOWN and event.key == pygame.K_c and pygame.key.get_mods() & pygame.KMOD_CTRL:
        pygame.quit(); exit()


    pygame.display.flip()
    clock.tick()

