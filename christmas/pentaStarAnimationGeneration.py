import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame import ftfont
from math import sqrt, sin, cos, radians
import json
from sys import stdin

WIDTH, HEIGHT = (1000, 1000)
WHITE = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))


ftfont.init()
abel = ftfont.Font('christmas/fonts/abel/Abel-Regular.ttf', 15)

def pentaRotate(vec):
    retVal = []
    for i in range(5):
        retVal.append(vec.rotate(360/5 * i))
    return retVal

def translateToPygameOrigin(vecList):
    origin = pygame.Vector2(WIDTH/2, HEIGHT/2)
    translated = []
    for coord in vecList:
        translated.append(coord + origin)
    return translated

def printFrameNo(frame):
    surf = abel.render(f'Frame: {frame}', True, pygame.Color('white'), pygame.Color('black'))
    screen.blit(surf, (0,0))

def draw(led):
    pygame.draw.circle(screen, led['color'], led['rect'].center, 10)

def serialize(frames):
    #Rects and Color objects cannot be serialized so we convert them to what we need to create them
    for frame in frames:
        for led in frame:
            led['rect'] = (led['rect'].left, led['rect'].top, led['rect'].width, led['rect'].height)
            led['color'] = (led['color'].r, led['color'].g, led['color'].b)
    print(json.dumps(frames))

def deserialize():
    if stdin.isatty():
        return [[]]

    frames = json.loads(stdin.read())
    
    #txt = open("christmas/anim.json").read()
    #frames = json.loads(txt)

    for frame in frames:
        for led in frame:
            left, top, width, height = led['rect']
            led['rect'] = pygame.Rect(left, top, width, height)
            r, g, b = led['color']
            led['color'] = pygame.Color(r,g,b)
    return frames

'''
      /|\ 
     / | \
    /  |  \
   /   b   h
  /    |    \
 /_____|_U/2_\
 \     |     /
   \   a   i
     \ | /

'''

# generate pentagram coordinates around true origin (0,0)
FI = (1+sqrt(5))/2

# pentagon width, arbitrarily chosen
U = 200

# hypotenusi
h = U * FI
i = U / (2*cos(radians(54)))

# intersections
a = i * sin(radians(54))
b = h * cos(radians(36))

mountain = pygame.Vector2(0, a+b)
valley = pygame.Vector2(U/2, a)

# turn the thing right side up
#mountain = mountain.rotate(180)
#valley = valley.rotate(180)

mountains = pentaRotate(mountain)
valleys = pentaRotate(valley)

mountains = translateToPygameOrigin(mountains)
valleys = translateToPygameOrigin(valleys)

# disperse
pentagram = mountains + valleys
pentagram[::2] = valleys 
pentagram[1::2] = mountains

pygame.draw.polygon(screen, pygame.Color('grey'), pentagram, 2)

# do linear interpolation to determine led positions
LEDS_PER_FACET = 4
ledCoords = []
leds = []

def createLed(coord):
    rect = pygame.draw.circle(screen, pygame.Color('black'), (int(coord.x),int(coord.y)), 10)
    leds.append({'index': i*5+i+led+1, 'rect': rect, 'color': pygame.Color('black')})

def clearAllLeds():
    for led in leds:
        draw(led)

for i in range(5):
    distBetweeenLeds = 1.0/(LEDS_PER_FACET+1)
    ledOffset = distBetweeenLeds/2

    for led in range(int(LEDS_PER_FACET)):
        coord = valleys[i].lerp(mountains[i], ledOffset+distBetweeenLeds*led)
        createLed(coord)


    # mountain led
    createLed(mountains[i])

    for led in range(int(LEDS_PER_FACET)):
        nextValley = i + 1
        if nextValley == 5:
            nextValley = 0

        coord = mountains[i].lerp(valleys[nextValley], 3*ledOffset+distBetweeenLeds*led)
        createLed(coord)

frames = deserialize()
frame = 0

printFrameNo(frame)

pygame.display.flip()

playing = False

# Game loop
while True:
    event = pygame.event.wait() # sleep until the user acts

    if event.type == pygame.MOUSEBUTTONUP:
        # remove lit from frame
        ledRemoved = False
        for led in frames[frame]:
            if led['rect'].collidepoint(event.pos):
                led['color'] = pygame.Color('yellow')
                frames[frame].remove(led)
                ledRemoved = True
                break
        if ledRemoved:
            continue

        # add led to frame
        for led in leds:
            if led['rect'].collidepoint(event.pos):
                if led not in frames[frame]:
                    nled = led.copy()
                    nled['color'] = pygame.Color('yellow')
                    frames[frame].append(nled)
                break

    if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
        frame = frame + 1

        if frame+1 > len(frames):
            # create new frame
            frames.append([])
            clearAllLeds()
        else:
            # show existing frame
            clearAllLeds()
            for led in frames[frame]:
                draw(led)

    if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
        frame = frame - 1
        if abs(frame) == len(frames):
            frame = 0
        

    if event.type == pygame.KEYUP and event.key == pygame.K_RETURN:
        if playing:
            time = 0
            playing = False
        else:
            time = 500
            playing = True

        pygame.time.set_timer(pygame.USEREVENT, time)

    if event.type == pygame.USEREVENT:
        frame = frame + 1
        if frame == len(frames):
            frame = 0

    # Allow for ways to exit the application
    if event.type == pygame.QUIT: # closing the (proverbial) window
        break
    if event.type == pygame.KEYDOWN and event.key == pygame.K_c and pygame.key.get_mods() & pygame.KMOD_CTRL:
        break

    #show existing frame
    clearAllLeds()
    printFrameNo(frame)
    for led in frames[frame]:
        draw(led)
    pygame.display.update()

# when the application exits, write the frames to json and dump it to stdout
serialize(frames)