# Basic - Print all integers from 0 to 150.

for num in range(151):
    print(num)


# Multiples of Five - Print all the multiples of 5 from 5 to 1,000

for num in range(5,1000,5):
    print(num)


# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".

for num in range(1,100):
    if num % 10 == 0:
        print("Coding Dojo")
    elif num % 5 == 0:
        print("Coding")
    else:
        print(num)


# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

for num in range(1,500000,2):
    total = 0
    total = total + num
print(total)

# or...

for num in range(500000):
    total = 0
    if num % 2 != 0:
        total += num
print(total)


# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

for num in range(2018, 0, -4):
    print(num)


# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, 
# print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should 
# print 3, 6, 9 (on successive lines)

lowNum = 2
highNum = 9
mult = 3
for num in range(lowNum, highNum+1, mult):
    if num % mult == 0:
        print(num)

#not sure why this one doesn't work