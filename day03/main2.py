def main():
    f = open('day03/main.txt','r')
    lines = f.readlines()
    lines = [line.strip('\n') for line in lines]
    sum = 0
    numbers = '0123456789'
    number = ''
    isvalid = False
    coordinates = None
    values = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] in numbers:
                number += lines[i][j]
                if not isvalid:
                    coordinates = check_hashtag(lines,i,j)
                    if coordinates:
                        isvalid = True
            elif number != '':
                if isvalid:
                    values.append({'checked':False, 'value':int(number),'y':coordinates['y'],'x':coordinates['x']})
                number = ''
                isvalid = False
                coordinates = None
    pair = []
    for value1 in values:
        pair.append(value1)
        value1['checked'] = True
        for value2 in values:
            if not value2['checked'] and value1['x'] == value2['x'] and value1['y'] == value2['y']:
                pair.append(value2)
                value2['checked'] = True
        if len(pair) == 2:
            sum += pair[0]['value'] * pair[1]['value']
        pair.clear()
                

    return sum

def check_hashtag(lines,y,x):
    if y != 0:
        if lines[y-1][x] == '*':
            return {'y':y-1,'x':x}
    if x != 0:
        if lines[y][x-1] == '*':
            return {'y':y,'x':x-1}
    if y != len(lines)-1:
        if lines[y+1][x] == '*':
            return {'y':y+1,'x':x}
    if x != len(lines[y])-1:
        if lines[y][x+1] == '*':
            return {'y':y,'x':x+1}
    if y != 0 and x != 0:
        if lines[y-1][x-1] == '*':
            return {'y':y-1,'x':x-1}
    if y != 0 and x != len(lines[y])-1:
        if lines[y-1][x+1] == '*':
            return {'y':y-1,'x':x+1}
    if y != len(lines)-1 and x != 0:
        if lines[y+1][x-1] == '*':
            return {'y':y+1,'x':x-1}
    if y != len(lines)-1 and x != len(lines[y])-1:
        if lines[y+1][x+1] == '*':
            return {'y':y+1,'x':x+1}


print(main())