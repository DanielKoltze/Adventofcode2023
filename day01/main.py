

def main():
    file = open('day01/main.txt','r')
    lines = file.readlines()

    sum = 0

    for line in lines:
        number = find_first_and_last_number(line)
        sum = sum + int(number)
    return sum


def find_first_and_last_number(line):
    numbers_string = '0123456789'
    numbers_in_line = []
    for char in line:
        for num in numbers_string:
            if num == char:
                numbers_in_line.append(num)
    return numbers_in_line[0] + numbers_in_line[-1]
    

print(main())
