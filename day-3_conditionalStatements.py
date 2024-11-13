print("Welcome to Geeza's Liquor Store!")

age = int(input('How old are you? '))

if age >= 21:
    print('You are old enough to purchase alcohol')
    drink = input('What would you like to drink? ')
    print(f'Here is your {drink} drink')
elif age < 21:
    print('Your are not old enough to drink alcohol.')
else:
    print('You are not of legal age to be drinking alcohol.')






