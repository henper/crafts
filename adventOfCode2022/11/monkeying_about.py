import yaml, csv, operator
from time import time
"""
Note, search-replace:
'    If' with:
'  If'
"""
troop = yaml.load(open('./adventOfCode2022/11/example.txt'), Loader=yaml.FullLoader)

# parse Starting items to list and add an inspection counter
for monkey in troop.keys():
    starting_items = troop[monkey]['Starting items']
    if isinstance(starting_items, str):
        items = list(csv.reader([starting_items]))
        troop[monkey]['Items'] = [int(n) for n in items[0]]
    else:
        troop[monkey]['Items'] = [starting_items] # achtually only one item
    troop[monkey]['Inspections'] = 0

do = {'+': operator.add, '*': operator.mul, '**': operator.ipow}

timestamp = time()

#for round in range(20):
for round in range(1000):
    for monkey in troop.keys():

        op, v = troop[monkey]['Operation'].split()[3:]
        div   = troop[monkey]['Test'].split()[2]

        # special case for when the operation is pow2
        if v == 'old':
            op = '**'
            v  = 2
        else:
            v = int(v)

        items = troop[monkey]['Items']
        while items:
            # inspect
            item = items.pop(0)
            troop[monkey]['Inspections'] += 1

            # worry, get bored and be relieved
            #item = int(do[op](item, int(v)) / 3)

            # worry and get bored
            item = do[op](item, v)

            # test
            if item % int(div) == 0:
                m = troop[monkey]['If true'].split()[3]
            else:
                m = troop[monkey]['If false'].split()[3]

            # throw
            troop['Monkey '+m]['Items'].append(item)

    if (round + 1 in [1, 20, 100, 500, 600, 700, 725, 750, 800, 900, 1000, 2000, 3000, 4000, 6000, 7000, 8000, 9000, 10000]):
        print(f"== After Round {round+1} ==")
        for monkey in troop.keys():
            print(f"{monkey} inspected items {troop[monkey]['Inspections']} times.")
        print("=== %.2f seconds ===" % (time() - timestamp))


inspections = ([monkey['Inspections'] for monkey in troop.values()])
inspections.sort()
print(inspections[-1] * inspections[-2])
