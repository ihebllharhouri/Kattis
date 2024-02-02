def main():
    seatSequence = input()
    length = len(seatSequence)
    count1 = 0
    count2 = 0
    count3 = 0

    for i in range(1, length):
        if seatSequence[i] != seatSequence[i-1]:
            if i == 1:
                count1 += 1
                count2 += 1
                count3 += 1

            else:
                if seatSequence[i-1] == 'U':
                    count1 += 1
                    count2 += 1
                    count3 += 1
                else:
                    count1 += 1
                    count2 += 1
                    count3 += 1
        elif i != 1:
            if seatSequence[i-1] == 'U':
                count2 += 2
            else:
                count1 += 2
        if i == length-1:
            if seatSequence[i] == 'U':
                count2 += 1
            else:
                count1 += 1
    print(count1)
    print(count2)
    print(count3)
    
if __name__ == '__main__':
    main()