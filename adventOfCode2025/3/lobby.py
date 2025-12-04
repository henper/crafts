from input import battery_banks

series_joltages = []
for bank in battery_banks:
    joltages = [int(j) for j in bank]

    series_joltage = 0
    idx = -1
    S = 12
    for i in range(S):

        n = len(joltages)
        end_idx = n-(S-(i+1))

        max_j = max(joltages[idx+1:end_idx])
        idx   = joltages.index(max_j, idx+1)

        series_joltage += max_j * 10**(S-1-i)

    print(f"Bank: {bank} -> Series joltage: {series_joltage}")
    series_joltages.append(series_joltage)

print(f"Total series joltage: {sum(series_joltages)}")
