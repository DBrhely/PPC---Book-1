#Python Programming Challenge
#10/2/14
#Danielle Brhely
#########################
import random
answer = (random.randint(0,100)
count = 0
guess = 100
while guess != answer:
    guess = input('Enter a number')
    count = count + 1
    if guess > answer:
          print('lower')
    elif guess < answer:
          print('higher')
print('Well done')
print(count)
