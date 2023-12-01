


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
    numbers = []
    current_string = ''
    for char in line:
        if char.isdigit():
            numbers.append(char)
            current_string = ''
        else:
            current_string = current_string + char
            number = find_string_number(current_string)
            if number != 0:
                numbers.append(number)
    return numbers
            



def find_string_number(string):
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

    reversed_string = ''.join(reversed(string))

    for word in word_to_number:
        if word in reversed_string:
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
    return 0



print(find_string_number('ksevensixzmrhsszlngfiveztbkqs'))





