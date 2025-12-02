from input import id_ranges

invalid_ids = []
for id_range in id_ranges:

    start, end = id_range

    for id in range(start, end + 1):

        id_str = str(id)
        num_num = int(len(id_str))
        if num_num % 2 != 0:
            continue

        midpoint = num_num >> 1
        left  = int(id_str[midpoint:])
        right = int(id_str[:midpoint])

        if left - right == 0:
            invalid_ids.append(id)
            print(f'found valid id: {id} in range {start} - {end}')


print(sum(invalid_ids))
