
step_one = 0

def traverse(wd: dict):
    global step_one
    for dir in wd['dirs'].keys():
        traverse(wd['dirs'][dir])

    for dir in wd['dirs'].keys():
        wd['size'] += wd['dirs'][dir]['size']

    for _, size in wd['files']:
        wd['size'] += size

    if wd['size'] <= 100000:
        step_one += wd['size']

def flatten(wd: dict, dir : str, dirs: list):
    for dir in wd['dirs'].keys():
        flatten(wd['dirs'][dir], dir, dirs)
    dirs.append(( wd['size'], dir))



with open('./adventOfCode2022/7/input.txt', 'r') as input:
    tree = {'dirs': {}, 'files': [], 'parent': {}, 'size': 0}
    tree['dirs']['/'] = {'dirs': {}, 'files': [], 'parent': {}, 'size': 0}

    # create reference in the tree to the working directory
    wd  = tree

    for line in input:
        line = line.split()

        if 'cd' in line:
            if line[2] == '..':
                wd = wd['parent']
            else:
                pwd = wd
                wd  = wd['dirs'][line[2]]
                wd['parent'] = pwd

        elif 'dir' in line:
            wd['dirs'][line[1]] = {'dirs': {}, 'files': [], 'parent': {}, 'size': 0}

        elif line[0].isdigit():
            file = line[1]
            size = int(line[0])
            wd['files'].append((file, size))

    traverse(tree)

    print(step_one)

    dirs = []
    flatten(tree['dirs']['/'], '/', dirs)
    dirs.sort()

    available = 70000000 - tree['size']
    needed = 30000000 - available

    for size, dir in dirs:
        if size >= needed:
            print(size)
            break
