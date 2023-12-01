def main():
    file = open('day01/main.txt','r')
    lines = file.readlines()
    sum = 0

    for line in lines:
        numbers = find_numbers(line)
        number = numbers[0] + numbers[-1]
        sum = sum + int(number)
    return sum


 
def find_numbers(line):
    number = ''
    for i in range(len(line)):
        if line[i].isdigit():
            number = line[i]
            break
        num = find_number(line[:i+1])
        if num != -1:
            number = num
            break

    for i in range(len(line),0,-1):
        if line[i-1].isdigit():
            number = number + line[i-1]
            break
        num = find_number(line[i-1:])
        if num != -1:
            number = number + num
            break
      
    return number

def find_number(string):
    word_to_number = [
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine',
    ]
    w = ''
    for word in word_to_number:
        if word in string:
            w = word
    
    if w == 'one':
        return '1'
    elif w == 'two':
        return '2'
    elif w == 'three':
        return '3'
    elif w == 'four':
      return '4'
    elif w == 'five':
        return '5'
    elif w == 'six':
        return '6'
    elif w == 'seven':
        return '7'
    elif w == 'eight':
        return '8'
    elif w == 'nine':
        return '9'
    return -1





print(main())


