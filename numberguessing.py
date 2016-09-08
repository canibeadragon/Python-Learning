# Writing a code to help me learn more about python coding.
# Perhaps a code about a number game

import random

randnum = random.randrange(1, 10, 1)
print(randnum);
print('Hello there');
print('I am guessing a number from 1 to 10, what do you think it is?')

number = input()

while ( int(number) != int(randnum)):
    print('That is wrong!')
    number = input();
else:
    print('That is correct!')
         
