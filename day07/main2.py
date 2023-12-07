import re
def main():
    lines = open('day07/main.txt','r').readlines()
    lines = [line.strip('\n') for line in lines]
    cards = []
    for line in lines:
        person = re.split(r'\s+', line)
        card = get_card_info(person[0])
        card['bid'] = int(person[1])
        cards.append(card)
    sum = 0
    sorted_cards = sorted(cards,key=sort_cards)
    for i in range(len(sorted_cards)):
        print(sorted_cards[i])
        v = sorted_cards[i]['bid'] * (i+1)
        sum += v

    return sum  
    


def get_card_info(hand):
    h = {}
    order = []
    for char in hand:
        if char !=  '':
            char = get_picture_card(char)
            if char not in h:
                h[char] = 1
            else:
                h[char] += 1
            order.append(char)
    


    value = get_value(h)
    return {'order':order,'value':value}




def get_value(h):

    if 1 in h:
        joker = h[1]
        if joker == 5:
            return 7
        del h[1]

        highest_index = None
        highest_number = 0

        for current_index, value in enumerate(h.values()):
            if value > highest_number:
                highest_number = value
                highest_index = current_index

        if highest_index is not None:
            keys = list(h.keys())
            h[keys[highest_index]] += joker

    if 5 in h.values():
        return 7
    elif 4 in h.values():
        return 6
    elif 3 in h.values() and 2 in h.values():
        return 5
    elif 3 in h.values():
        return 4
    elif list(h.values()).count(2) == 2:
        return 3
    elif 2 in h.values():
        return 2
    else:
        return 1

      
def get_picture_card(c):
    pc = 'AKQJT'
    

    if c == 'A':
        return 14
    if c == 'K':
        return 13
    if c == 'Q':
        return 12
    if c == 'J':
        return 1
    if c == 'T':
        return 10
    return int(c)

def find_card_placement(cards, card):
    index = 1
    for c in cards:
        if c['value'] > card['value']:
            return index
        elif c['value'] == card['value']:
            for i in range(len(c['order'])):

                if check_order(c['order'],card['order'][i]):
                    return index
            index += 1
    return index

def check_order(cards, card):
    for c in cards:
        if card > c:
            return True
        return False
    
def sort_cards(item):
    return item['value'], item['order']

print(main())





    