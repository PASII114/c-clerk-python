# for i in range(10, 20):# value of 'i' starts with 10
#     print(i)
#
# for i in range(0, 100, 10):#increment 'i' by 10
#     print(i)
#
#     if i == 3:
#         print("Waiting")
#         break
#     print("Hello")
#     print("Exited")

#simple countdown from 10 to 0
# for i in range(10, -1, -1):
#     print(i)

#use a for loop 0 - 100 range
#if a number is divisible by 3 print fizz
#if a number is divisible by 5 print buzz
#if a number is divisible by both 3 and 5 print fizzbuzz
for i in range(0, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i, "fizzbuzz")
    elif i % 3 == 0:
        print(i, "fizz")
    elif i % 5 == 0:
        print(i, "buzz")
    else:
        print(i)