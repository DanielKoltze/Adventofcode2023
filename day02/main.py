

def main():
    file = open('day02/main.txt','r')
    lines = file.readlines()
    sum = 0

    for line in lines:
        line = line.split(':')
        p = line[0].split(' ')
        game_number = int(p[1])
        
        set = line[1].split(';')
        bagvalid = True
        for set in set:
            red = blue = green = 0
            items = set.split(',')
            for item in items:
                item = item.strip()
                item_split = item.split(' ')
               
                value = int(item_split[0])
                if item_split[1] == 'blue':
                    blue += + value
                if item_split[1] == 'red':
                    red += value
                if item_split[1] == 'green':
                    green += value
        
            if red > 12 or green > 13 or blue > 14:
                bagvalid = False
        if bagvalid:
            sum += game_number
    return sum

    
print(main())


