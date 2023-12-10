def main():
    lines = open('day10/day10.txt','r').readlines()
    steps = 0
    que = []
    map,index = get_map(lines)
    x = 1
    y = len(lines[0])
    que.append(index)
    map[index]['visited'] = True
    while(len(que) != 0):
        if map[index]['right'] and not map[index+x]['visited']:
            map[index+x]['visited'] = True
            que.append(index+x)
            index += x
        elif map[index]['left'] and not map[index-x]['visited']:
            map[index-x]['visited'] = True
            que.append(index-x)
            index -= x
        elif map[index]['up'] and not map[index-y]['visited']:
            map[index-y]['visited'] = True
            que.append(index-y)
            index -= y
        elif map[index]['down'] and not map[index+y]['visited']:
            map[index+y]['visited'] = True
            que.append(index+y)
            index += y
        else:
            obj = que.pop()
            index = obj
        if len(que) > steps:
                steps = len(que)
    return steps
    
        
        
def get_map(lines):
    map = {}
    starting_point = 0
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
        for j in range(len(lines[i])):
            if lines[i][j] != '.':
                symbol = lines[i][j]
                right,left,up,down = False,False,False,False
                if symbol == '|':
                    up,down = True,True
                elif symbol == '-':
                    right,left = True,True
                elif symbol == 'L':
                    up,right = True,True
                elif symbol == 'J':
                    up,left = True, True
                elif symbol == '7':
                    left,down = True,True
                elif symbol == 'F':
                    down,right = True,True
                elif symbol == 'S':
                    right,left,up,down = True,True,True,True
                    starting_point = (len(lines[i])*i) + j
                obj = {'left':False,'right':False,'up':False,'down':False,'visited':False}
                if left and j != 0:
                    if lines[i][j-1] == '-' or lines[i][j-1] == 'L' or lines[i][j-1] == 'F':
                        obj['left'] = True
                if up and i != 0:
                    if lines[i-1][j] == '|' or lines[i-1][j] == '7' or lines[i-1][j] == 'F':
                        obj['up'] = True
                if right and j != len(lines[i])-1:
                    if lines[i][j+1] == '-' or lines[i][j+1] == '7' or lines[i][j+1] == 'J':
                        obj['right'] = True
                if down and i != len(lines)-1:
                    if lines[i+1][j] == '|' or lines[i+1][j] == 'L' or lines[i+1][j] == 'J':
                        obj['down'] = True
                map[(len(lines[i])*i) + j] = obj
    return map, starting_point


                    
                    


print(main())