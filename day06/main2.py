import re

def main():
    lines = open('day06/main.txt','r').readlines()
    lines = [line.strip('\n') for line in lines]
    time = [t for t in lines[0] if t.isdigit()]
    distance = [d for d in lines[1] if d.isdigit()]
    time = ''.join(time)
    distance = ''.join(distance)
    
    return calc_time(time, distance)


def calc_time(t, d):
    ans = 0
    t = int(t)
    d = int(d)
    for x in range(t):
        r = x*(t-x)
        if r>=d:
            ans += 1
    return ans

print(main())