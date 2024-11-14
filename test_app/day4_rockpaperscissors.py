import random

Rock = 'Rock'
Paper = 'Paper'
Scissor = 'Scissors'

choice = [Rock, Paper, Scissor]

my_choice = int(input('What do you choose? 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
print('\n' +choice[my_choice])

PC = random.randint(0, 2)
print(f'PC chose:')
print(choice[PC])

if my_choice == 0 and PC == 1:
    print('PC win!')
elif PC >= 3 or my_choice < 0:
    print('invalid number entered') 
elif PC > my_choice:
    print('PC win!')
elif PC < my_choice:
    print('You win')    
elif PC == my_choice:
    print('Draw!')
elif PC == 0 and my_choice == 2:
    print('You lose')
elif my_choice == 1 and PC == 0:
    print('You win!')   
   
  

