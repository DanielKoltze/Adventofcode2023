def main():
    lines = open('day08/main.txt','r').readlines()
    directions = lines[0].strip()
    del lines[0]
    del lines[0]
    nodes = get_nodes(lines)
    current_node = lines[0][:3]
    index_directions = 0
    sum = 0
    while(current_node != 'ZZZ'):
        direction = directions[index_directions]
        obj = nodes[current_node]
        current_node = obj[direction]
        if index_directions < len(directions)-1:
            index_directions += 1
        else:
            index_directions = 0
        sum += 1
    return sum
        
def get_nodes(lines):
    nodes = {}
    for line in lines:
        nodes[line[:3]] = {'L':line[7:10],'R':line[12:15]}
    return nodes
    
print(main())

