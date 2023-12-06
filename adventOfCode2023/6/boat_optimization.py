import numpy as np
from input import *

answer = 1

for race_time, record in zip(times, distances):

    push_times = np.linspace(0, race_time, race_time+1)

    distances = push_times * race_time - push_times * push_times

    num_ways_to_beat_record = (distances > record).sum()

    answer = answer * num_ways_to_beat_record

print(answer)

