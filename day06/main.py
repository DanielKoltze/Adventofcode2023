import re

def main():
    lines = open('day06/main.txt','r').readlines()
    lines = [line.strip('\n') for line in lines]
    times = re.split(r'\s+', lines[0])
    distances = re.split(r'\s+', lines[1])
    sum = 1
    for i in range(1,len(times)):
        above_record = calc_time(distances[i],times[i])
        sum *= above_record
    return sum

def calc_time(distance,t):
    distance = int(distance)
    t = int(t)
    sum = 0
    for i in range(1,distance-1):
        time_left = t - i
        time = i*time_left
        if time > distance:
            sum += 1
    return sum

print(main())