

def main():
    f = open('day03/main.txt','r')
    lines = f.readlines()
    lines = [line.strip('\n') for line in lines]
    sum = 0
    numbers = '0123456789'
    number = ''
    isvalid = False

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] in numbers:
                number += lines[i][j]
                if not isvalid:
                    isvalid = check_adjacent(lines,i,j)
            elif number != '':
                if isvalid:
                    sum += int(number)
                number = ''
                isvalid = False
    return sum



def check_adjacent(lines,y,x):
    notequal = '1234567890.'
    if y != 0:
        if lines[y-1][x] not in notequal:
            return True
    if x != 0:
        if lines[y][x-1] not in notequal:
            return True
    if y != len(lines)-1:
        if lines[y+1][x] not in notequal:
            return True
    if x != len(lines[y])-1:
        if lines[y][x+1] not in notequal:
            return True
    if y != 0 and x != 0:
        if lines[y-1][x-1] not in notequal:
            return True
    if y != 0 and x != len(lines[y])-1:
        if lines[y-1][x+1] not in notequal:
            return True
    if y != len(lines)-1 and x != 0:
        if lines[y+1][x-1] not in notequal:
            return True
    if y != len(lines)-1 and x != len(lines[y])-1:
        if lines[y+1][x+1] not in notequal:
            return True
    return False


print(main())

