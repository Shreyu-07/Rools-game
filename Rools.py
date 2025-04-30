from random import randint
import time
import pyttsx3 as sp

print('''Welcome to the lucky burst: 
you will use your luck and win the game
**Note**
1) if you get odd you are out
2) if ypu get even then you will win

Lets start the game....

''')
time.sleep (1)
print('loding....\n')
sp. speak('loading...')
time.sleep (2)
while 1:
    choice = input("Do you want to play ? y/n:").lower().strip()
    if choice == 'y':
        sp.speak('You are you are taken to the play ground....')
        dice1 = randint(1,5)
        dice2 = randint(6,10)
        print(f'the results are : \n {dice1},{dice2}')
        print('\n')
        sum = dice1+dice2
        print(f'The sum is : {sum}')
        if sum%2==0:
            print('The out put is even')
            print('Hey congratulations you won...')
        elif sum%2!= 0:
            print('The out put is odd')
        
    elif choice == 'n':
        print('Thanks for playing')
        break  
    else:
        print('Invalid input')
        break
