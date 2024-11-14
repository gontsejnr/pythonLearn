# # for loop
# fruits = ['Banana', 'Pear', 'Apple', 'Lemon', 'Mango']
# # looping through the list and getting the fruits
# for fruit in fruits:
#     # printing each fruit from the list
#     print(fruit)


# # input a list of student heights
# student_heights = input().split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# # 
# total_height = 0
# for height in student_heights:
#     total_height += height
# print(f'total_height = {total_height}')

# number_of_students = 0
# for student in student_heights:
#     number_of_students += 1
# print(f'number of students = {number_of_students}')

# average_height =  round(total_height / number_of_students)
# print(f'average height = {average_height}')

# # for loop with range
# total = 0
# for number in range(1,101, 2):
#     total += number
#     print(total)


# target = int(input())
# even_sum = 0
# for number in range(2, target + 1, 2):
#     even_sum += number
#     print(even_sum)

target = 100
for number in range(1, target+1):
    if number % 3 == 0 and number % 5 ==0:
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)    