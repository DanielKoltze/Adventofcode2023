

def main():
    file = open('day02/main.txt','r')
    lines = file.readlines()
    sum = 0
    colors = [{'value':0, 'color':'red','highest':0}, {'value':0, 'color':'green','highest':0}, {'value':0, 'color':'blue','highest':0}]

    for line in lines:
        line = line.split(':')
        p = line[0].split(' ')
        
        set = line[1].split(';')
        for set in set:
            
            items = set.split(',')
            for item in items:
                item = item.strip()
                item_split = item.split(' ')

                value = int(item_split[0])
                color = item_split[1]


                for c in colors:
                    if c['color'] == color:
                         c['value'] += int(value)
            
            for c in colors:
                if c['value'] > c['highest']:
                    c['highest'] = c['value']
                c['value'] = 0
        v = 1
        for c in colors:
             v = v * c['highest']
             c['highest'] = 0
        sum += v 
        
    return sum

    
print(main())



