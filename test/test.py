import string

def main():
    f = open('test.txt', 'r')
    lines = f.readlines()
    letters = []
    sum = 0

    for line in lines():
        found_letter = find_letter(line)
        letters.append(found_letter)

    for letter in letters:
        sum = sum + find_letter_sum(letter)
    return sum



def find_letter(line):
    length = len(line)
    first_part = line[:length//2]
    second_part = line[length//2:]
    for i in first_part:
        for j in second_part:
            if i == j:
                return i
    


def find_letter_sum(letter):
    all_letters_string = string.ascii_lowercase + string.ascii_uppercase
    print(all_letters_string)

find_letter_sum('g')