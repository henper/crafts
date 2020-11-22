import json, sys

filename = sys.argv[1]
txt = open(filename).read()


frames = json.loads(txt)

print('#include <NeoPixelBus.h>')
print('RgbColor anim[] =')

print('{')
for frame in frames:
    #print('  {')
    for led in frame:
        i = led['index']
        r,g,b = led['color']
        print(f'    RgbColor({r}, {g}, {b}), // {i}')
    print(' ')
print('};')