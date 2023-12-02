
def main():
    file = open('other/test.txt','r')
    lines = file.readlines()
    for line in lines:
        upper_row = 48
        lower_row = 32
        upper_column = 8
        low_column = 1
        for char in line:
            if char == 'F':
                upper_row = ((upper_row - lower_row) // 2) + lower_row
            if char == 'B':
                lower_row = ((upper_row - lower_row) // 2) + upper_row


main()