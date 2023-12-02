def main():
    file = open('other/test.txt','r')
    lines = file.readlines()
    sum = 0
    passportdata = 0

    for line in lines:
        if line == '\n':
            if passportdata == 7:
                sum = sum + 1
            passportdata = 0
        else:
            data = line.split(' ')
            for d in data:
                da = d.split(':')
                if da[0] == 'byr' and int(da[1]) > 1920 and int(da[1]) < 2002:
                    passportdata += 1
                if da[0] == 'iyr' and int(da[1]) > 2010 and int(da[1]) < 2020:
                    passportdata += 1
                if da[0] == 'eyr' and int(da[1]) > 2020 and int(da[1]) < 2030:
                    passportdata += 1
                if da[0] == 'hgt':
                    if da[1][-2:] == 'cm':
                        if int(data[1][:-2]) > 150 and int(data[1][:-2]) < 193:
                            passportdata += 1
                    if da[1][-2:] == 'in':
                        print(data[1][:-2])
                        if int(data[1][:-2]) > 59 and int(data[1][:-2]) < 76:
                            passportdata += 1

    return sum

main()






