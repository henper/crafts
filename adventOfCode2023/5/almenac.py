import numpy as np
from input import *

maps = [
    seed_to_soil,
    soil_to_fertilizer,
    fertilizer_to_water,
    water_to_light,
    light_to_temperature,
    temperature_to_humidity,
    humidity_to_location
]

nesting_doll = []

for seed in seeds:

    value = seed

    nesting_doll.append([])
    nesting_doll[-1].append(value)

    for map in maps:

        for tuple_range in map:
            destination, source, length = tuple_range

            if value in range(source, source+length):
                value = destination + (value - source)
                break

        nesting_doll[-1].append(value)

nesting_doll = np.array(nesting_doll)
locations = nesting_doll[:,-1]

print(min(locations))
