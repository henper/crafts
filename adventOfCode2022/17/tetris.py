import pygame
from pygame import Rect
from copy import deepcopy

S = SCALING = 100
WIDTH = 7 * S
HEIGHT = 20 * S


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

top = HEIGHT
scroll = 0
static = screen.copy()

TEXT = (255,255,255)
font = pygame.font.Font(None, S)
block_counter = font.render('B: ' + str(0), True, TEXT)
block_counter_rect = block_counter.get_rect()
block_counter_rect.topleft = (0,0)
screen.blit(block_counter, block_counter_rect)

top_counter = font.render('T: ' + str(0), True, TEXT)
top_counter_rect = block_counter.get_rect()
top_counter_rect.topleft = (0,S)
screen.blit(top_counter, top_counter_rect)
pygame.display.flip()


# shapes
line = {'colour': (  0,255,255), 'rects':  [Rect((0*S,0*S), (4*S,1*S))]}
plus = {'colour': (255,127,  0), 'rects':  [Rect((1*S,0*S), (1*S,3*S)), Rect((0*S,1*S), (3*S,1*S))]}
elle = {'colour': (  0,255,  0), 'rects':  [Rect((2*S,0*S), (1*S,3*S)), Rect((0*S,2*S), (3*S,1*S))]}
barr = {'colour': (255,  0,  0), 'rects':  [Rect((0*S,0*S), (1*S,4*S))]}
sqre = {'colour': (255,255,  0), 'rects':  [Rect((0*S,0*S), (2*S,2*S))]}

shapes = [line, plus, elle, barr, sqre]

input = open('./adventOfCode2022/17/input.txt', 'r')


global count
count = 0

# spawn point for new blocks
spawn = (2*S, HEIGHT-3*S)

# blocks at rest
rubble = []

# state variables
at_rest = True # spawn new blocks when at rest
jet = True # if not jet, then drop

def collides(block, delta):
    for r in range(len(block['rects'])):
        rect = block['rects'][r].move(delta)

        # collides with walls or floor?
        if rect.right > WIDTH or rect.left < 0 or rect.bottom > HEIGHT:
            return True

        # collides with rubble?
        if (rect.collidelist(rubble)) != -1:
            return True

    return False

while True:
    event = pygame.event.poll() # get event immideately, if any
    # Allow for ways to exit the application
    if event.type == pygame.QUIT: # closing the (proverbial) window
        break
    if event.type == pygame.KEYDOWN and event.key == pygame.K_c and pygame.key.get_mods() & pygame.KMOD_CTRL:
        break

    if at_rest and count % 10000 == 0:
        pygame.display.flip()

    if at_rest and count >= 1000000000000:
        pygame.display.flip()
        continue

    if at_rest:
        at_rest = False
        # spawn new block
        block = deepcopy(shapes[count % len(shapes)])
        count += 1

        # set its origins and draw its rects
        bottom = block['rects'][0].bottom
        if len(block['rects']) == 2:
            bottom = max(bottom, block['rects'][1].bottom)

        dx, dy = spawn
        dy -= bottom
        for r in range(len(block['rects'])):
            block['rects'][r] = block['rects'][r].move((dx,dy))
            pygame.draw.rect(screen, block['colour'], block['rects'][r].move(0, scroll))

        block_counter = font.render('B: ' + str(count), True, TEXT)
        screen.fill((0,0,0), block_counter_rect)
        screen.blit(block_counter, block_counter_rect)

        #pygame.display.flip()

    dx, dy = (0,1*S) # drop
    if jet:
        dy = 0
        # apply jet-stream
        char = input.read(1)
        if char == '\n':
            input.seek(0,0)
            char = input.read(1)

        match char:
            case '<':
                dx = -S
            case '>':
                dx = S
            case other:
                assert(False)
    jet = not jet

    if collides(block, (dx,dy)):
        at_rest = jet # can only be at rest if dropped

        if at_rest:
            # add to rubble
            rubble += block['rects']

            # update spawn point
            top = min(top, block['rects'][0].top)
            if len(block['rects']) == 2:
                top = min(top, block['rects'][1].top)

            spawn = (2*S, top - 3*S)

            # update scrolling
            over_the_top = int(HEIGHT / 2) - (top + scroll)
            if over_the_top > 0:
                scroll += over_the_top

                screen.fill((0,0,0), Rect((0,0), (WIDTH, 2*S)))

                static.blit(screen, (0, over_the_top))
                screen.fill((0,0,0))
                screen.blit(static, (0,0))

            # update top counter
            top_counter = font.render('T: ' + str(int((HEIGHT-top)/S)), True, TEXT)
            screen.fill((0,0,0), top_counter_rect)
            screen.blit(top_counter, top_counter_rect)


    else:
        # clear the current position on the screen
        for r in range(len(block['rects'])):
            pygame.draw.rect(screen, (0,0,0), block['rects'][r].move(0, scroll))

        for r in range(len(block['rects'])):
            block['rects'][r] = block['rects'][r].move((dx,dy))
            pygame.draw.rect(screen, block['colour'], block['rects'][r].move(0, scroll))

    #pygame.display.flip()

print(top)
pygame.quit()
