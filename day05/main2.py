def main():
    f = open('day05/main.txt','r')
    lines = f.readlines()
    lines = [line.strip('\n') for line in lines]

    seeds_line = lines[0][7:].split(' ')
    lines.remove(lines[0])
    lines.remove(lines[0])
    pairs = []
    for i in range(0, len(seeds_line), 2):
        pairs.append(seeds_line[i-1] + ' ' + seeds_line[i])


    seeds = get_seeds(pairs)
    lowest_value = 999999999

    lines = [c for c in lines if 'map' not in c]
    current_seed_value = 0

    for seed in seeds:
        has_changed = False
        for line in lines:
            if line != '':
                if not has_changed:
                    value = get_value(line,seed)
                    if value != None:
                        current_seed_value = value
                        has_changed = True
            else:
                has_changed = False
        if current_seed_value < lowest_value:
            lowest_value = current_seed_value
    
    return lowest_value



def get_value(line,seed):
    line = line.split(' ')
    line = [int(i) for i in line]
    new_value, start, range = line

    if seed >= start and seed <= start+range:
        difference = new_value - start
        return seed + difference
    return None

def get_seeds(pairs):
    seeds = []
    for pair in pairs:
        pair = [int(i) for i in pair.split(' ')]
        for i in range(pair[0]+1):
            seeds.append(pair[1]+i)
    return seeds


print(main())

