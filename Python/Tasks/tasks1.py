import random

random_number = random.randint(0,10)
count = 3
# print(random_number)
# while count > 0:
#     number = int(input('Put number from 0 to 10: '))
#     count -= 1
#     if number >= random_number:
#         print('your number is more then needed')
#     elif number <= random_number and number < 11:
#         print('your number is less then needed')
#     elif number == random_number:
#         print('you won')

#     if count == 0:
#         print("You loose")
    

count = 3
print(random_number)
while count > 0:
    def my_number():
        number = int(input("Enter your number"))
        if number >= random_number:
            return ('your number is more then needed')
        elif number <= random_number and number < 11:
            return ('your number is less then needed')
        elif number == random_number:
            return ('you won')
        if count == 0:
            return ("You loose")
    count -= 1
    print(my_number())
    
    

