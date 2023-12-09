def main():
    lines = open('day09/main.txt','r').readlines()
    sum = 0
    for line in lines:
        sequences = [[int(n) for n in line.split(' ')]]
        not_all_zeroes = True
        while(not_all_zeroes):
            latest_sequece = sequences[-1]
            new_sequece = []
            for i in range(len(latest_sequece)-1):
                new_sequece.append(latest_sequece[i+1]-latest_sequece[i])
            sequences.append(new_sequece)
            if new_sequece.count(0) == len(new_sequece):
                not_all_zeroes = False
        
        first = []
        value = 0
        for sequence in sequences:
            first.append(sequence[0])
        for i in range(len(first)-2,-1,-1):
            value = first[i] - value
        sum += value
    return sum

print(main())
