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

locations = []

def traverse_mapping(value, maps):
    for map in maps:
        for mapping in map:
            destination, source, map_length = mapping
            source_end = source + map_length

            start, length = value
            end = start + length

            # check if completely covered
            if start >= source and end <= (source + map_length):
                value = (destination + (start - source), length)
                break

            # check if partly covered, if so split in two value ranges
            # where the part that gets translated spins up a new "thread"
            # and the remainder remains here to be finished in the next iteration
            remaining_maps = maps[(maps.index(map)+1):]

            # middle part
            if start < source and end > (source + map_length):
                traverse_mapping((start, source - start), remaining_maps)
                traverse_mapping((source_end + 1, end - source_end - 1), remaining_maps)

                value = (destination, map_length)
                break

            # bottom part of the values are covered by the mapping
            if start >= source and start <= source_end:

                traverse_mapping((destination + (start - source), source_end + 1 - start), remaining_maps)
                value = (source + map_length, end - source_end + 1)
                break

            # top part
            if end >= source and end <= source_end:
                traverse_mapping((destination, end - source), remaining_maps)
                value = (start, source - start)
                break





    locations.append(value[0])


for seed in seeds:
    traverse_mapping(seed, maps)

print(min(locations))
