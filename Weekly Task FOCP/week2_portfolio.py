
# 1.Last week you wrote a program that printed out a cheery greeting including your
# name. Take a copy of it, and modify it so that the user enters their name at the
# keyboard, and then receives a greeting. For example:
# Hello, what is your name? Mr Apricot
# Hello, Mr Apricot. Good to meet you!



a = input('Hello, what is your name? ')
a = a.title()
print (f'Hello {a}. Good to meet you!')
print('==================================')


# 2.Write a program that prompts a user to enter a temperature in Celsius, and then
# displays the corresponding temperature in Fahrenheit, like so:
# Enter a temperature in Celsius: 32.5
# 32.5C is equivalent to 90.5F.

celsius = float(input('Input the temperature in celsius: '))
fahrenheit = celsius * (9 / 5) + 32
print(f'Hello the temperature is {fahrenheit} degree Fahrenheit.!')
print('==================================')


# 3.The Head of Computing at the University of Poppleton is tasked with dividing a
# group of students into lab groups. A lab group is usually 24 students, but this is
# sometimes varied to create groups of similar size. Write a program that prompts for
# the number of students and group size, and then displays how many groups will be
# needed and how many will be left over in a smaller group.
# How many students? 113
# Required group size? 22
# There will be 5 groups with 3 students left over.
# For bonus credit, see if you can fix the grammar in the output. So if there were 101
# students in groups of 20 the output would be:
# There will be 5 groups with 1 student left over.




t = int(input('Input the total number of students: '))
g = int(input('Input the group size: '))

total_students = t // g
extra_students = t % g

print(f'The total students in the group will be {total_students}, with {extra_students} as extras ')
print('==================================')


# 4.A kindly teacher wishes to distribute a tub of sweets between her pupils. She will first count the sweets and then divide them according to how many pupils attend
# that day. Write a program that will tell the teacher how many sweets to give to each
# pupil, and how many she will have left over.




s = int(input('Total amount of sweets: '))
p = int(input('Total number of pupils: '))

total_sweets_distributed = s // p
extra_sweets = s % p

print(f'Each student will receive {total_sweets_distributed} sweets, with {extra_sweets} as extras ')
print('==================================')







