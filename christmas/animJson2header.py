import json, sys

filename = sys.argv[1]
txt = open(filename).read()

frames = json.loads(txt)

print('{')
for frame in frames:
    for led in frame:
        r,g,b = led['color']
        print(f'    {{.index = {led["index"]}, .color = RgbColor({r}, {g}, {b})}},')
print('}')