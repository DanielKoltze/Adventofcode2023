

def main():
    f = open('day04/main.txt','r')
    lines = f.readlines()
    lines = [line.strip('\n') for line in lines]
    cards = []

    for i, line in enumerate(lines):
        cards.append(i+1)
        for card in cards:
            if card == i+1:
                new_copies = get_copies(i,line)
                cards.extend(new_copies)
    return len(cards)


def get_copies(game_number, line):
    s = line.split(':')
    p = s[1].split('|')
    w = p[0].split(' ')
    l = p[1].split(' ')
    winning_numbers = [char for char in w if char != '']
    card_numbers = [char for char in l if char != '']
    wins = [char for char in winning_numbers if char in card_numbers]
    copies = []
    for i in range(len(wins)):
        copies.append(game_number+i+2)
    return copies

print(main())