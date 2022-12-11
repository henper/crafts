
with open('./adventOfCode2022/6/input.txt', 'r') as input:

    count  = 14
    signal = [*input.read(count)]

    while True:

        if len(set(signal)) == 14:
            print(count)
            exit()

        signal = signal[1:] + [input.read(1)]
        count += 1
