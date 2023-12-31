def main():
    f = open('day05/main.txt','r')
    lines = f.readlines()
    lines = [line.strip('\n') for line in lines]

    seeds_line = lines[0][7:].split(' ')
    seeds_line = [int(v) for v in seeds_line]
    lines.remove(lines[0])
    lines.remove(lines[0])
    seeds = []
    for seed in seeds_line:
        seeds.append({'is_changed':False,'seed':seed})

    lines = [c for c in lines if 'map' not in c]
    v = 0
    for line in lines:
        if line != '':
            for i in range(len(seeds)):
                if not seeds[i]['is_changed']:
                    value = get_value(line,seeds[i]['seed'])
                    if value != None:
                        seeds[i]['seed'] = value
                        seeds[i]['is_changed'] = True
        else:
            for seed in seeds:
                seed['is_changed'] = False
    result = 0      
    for seed in seeds:
        if result == 0 or seed['seed'] < result:
            result = seed['seed']
    return result



def get_value(line,seed):
    line = line.split(' ')
    line = [int(i) for i in line]
    new_value, start, range = line

    if seed >= start and seed <= start+range:
        difference = new_value - start
        return seed + difference
    return None

print(main())

