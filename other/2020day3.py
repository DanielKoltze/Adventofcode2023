def main():
    file = open('test/test.txt','r')
    lines = file.readlines()
    point = -3
    trees = 0
    for line in lines:
        line = line.rstrip('\n')
        point = point + 3
        if len(line) <= point:
            point = point % len(line)
        if line[point] == '#':
            trees = trees + 1
    return trees

print(main())