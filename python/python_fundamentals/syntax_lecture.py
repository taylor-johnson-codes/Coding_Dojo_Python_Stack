# # Python good back-end/server-side language because it's good at AI/machine learning/data science/math
# # uses tabs instead of {} to nest stuff
# # using 4 spaces instead of tabs can mess up how code runs (common issue when copy/pasting code)


# # FOR LOOP (range is a method)
# # 3 parameters: 
# # 1-optional. starting index (default 0) 
# # 2-required. ending position (not included) 
# # 3-optional. increment/decrement integer (default 1)

# for i in range(5):  # doesn't include 5; semicolon means next lines need to be indented
#     print(i)
#     # prints 0 1 2 3 4 

# for i in range(2,5):
#     print(i)
#     # prints 2 3 4

# for i in range(10,0,-2):  # starting at index 9, going to index 0 (not included), decrementing by 2
#     print(i)
#     # prints 10 8 6 4 2 


# # DATA TYPES (not using var keyword)
# mystring = "hello"
# myboolean = True  # must be capitalized
# mylist = []  # "array" in JS
# mydictionary = {}  # "object" in JS


# # COMMON FUNCTIONS

# print(len(mylist))  # to get length of something use len()

# for i in range (0, len(mylist)):  # how to loop through a list
#     print (mylist[i])
#     if i < 3:
#         print("i is less than 3")
#     elif i == 2:
#         print("i is 2")
#     else: 
#         print("something else")

# print(type(mystring))  # to get variable type use type()


# # TYPE CASTING
# # need to cast data to the same type to concatenate it

# str(12345)  # will return a string version
# print(type(str(12345)))
# int("123")  # will return an int version
# print(type(int("123")))


# # TRUTHY OR FALSEY

# check = 0  # 0 means false; 1 means true
# if check:
#     print("if statement")
# else:
#     print("else statement")

# check = 1
# if check:
#     print("if statement")
# else:
#     print("else statement")

# check = []  # empty list results in False; list with items results in True
# if check:
#     print("if statement")
# else:
#     print("else statement")

# check = ""  # empty string results in False; string with items results in True
# if check:
#     print("if statement")
# else:
#     print("else statement")


# def reverseArray(arr):  # def is the keyword for a function
#     for i in range(0, len(arr)//2):  # // is syntax for math.floor; alternative is to import math and use math.floor()
#         temp = arr[i]
#         arr[i] = arr[len(arr) - 1 - i]
#         arr[len(arr) - 1 - i] = temp
#     return arr
# print(reverseArray([1,2,3]))


# swapping
myList = [1,3,5,7]
myList[0], myList[1] = myList[1], myList[0]
print(myList)  # [3,1,5,7]