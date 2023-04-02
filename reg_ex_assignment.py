import re

hand = open('regex_actual.txt')
#txt = hand.read()

sum = 0
count = 0

for line in hand:
    line = line.rstrip()
    # print(line)
    y = re.findall('[0-9]+', line)
    # I had the if conditional and the for loop reversed and it was driving me crazy. Finally got it to work like this.
    for num in y:
        if len(y) > 0:
            count = count + 1
            sum = sum + int(num)
print("The count is ", count, "and the sum is ", sum)
