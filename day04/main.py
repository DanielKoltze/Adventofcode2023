

def main():
    f = open('day04/main.txt','r')
    lines = f.readlines()
    lines = [line.strip('\n') for line in lines]
    sum = 0

    for line in lines:
        s = line.split(':')
        p = s[1].split('|')
        w = p[0].split(' ')
        l = p[1].split(' ')
        winning_numbers = [char for char in w if char != '']
        card_numbers = [char for char in l if char != '']

        card_winnings = [win for win in winning_numbers if win in card_numbers]
        if len(card_winnings) != 0:
            multiply = 1
            for i in range(len(card_winnings)-1):
                multiply *= 2
            sum += multiply
    return sum

print(main())