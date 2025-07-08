'''
# Programming Task 8.1

name = str(input("Please enter your legal name: ")) 
print("Legal name:", name)
acc_type = input("Is this your personal account? [Leave it if it's not...] ")
print("Personal Account:", bool(acc_type))

dob_month = int(input("Please enter your month of birth: "))
if dob_month > 12 or dob_month < 1: 
    print("Please enter a valid month: ")
    dob_month = int(input())
    print('Month of birth:' + dob_month)
else:
    print(dob_month)

dob_date = int(input("Please enter your date of birth: "))
if dob_date > 31 or dob_date < 1:
    print("Please enter a valid date: ")
    dob_date = int(input())
    print(dob_date)
else:
    print(dob_date)

dob_year = int(input("Please enter your year of birth: "))
if len(str(dob_year)) != 4:
    print("Please enter a valid year: ")
    dob_year = int(input())  
    print(dob_year)
else:
    print(dob_year)

username = str(input("Please enter your desired username: "))
if len(username) < 8:
    print("please enter a username with at least 8 characters: ")
    username = str(input())

print(acc_type)
'''

'''
# Programming Task 8.2

num1 = float(input("One number pwese: "))
op = str(input("operation pls: "))
while op != '+' and op != '-' and op != 'x' and op != '/' and '^' and '%': 
    op = str(input("Please enter a valid operation: "))
num2 = float(input("Another one pwese: "))

if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == 'x':
    print(num1 * num2)
elif op == '/':
    print(num1 / num2)
elif op == '^':
    print(num1 ^ num2)
elif op == '%':
    print(num1 % num2)
'''

'''
# Programming Task 8.3

number = int(input("Enter a number between 1 to 10 for the user to guess: "))
guess = int(input("Guess: "))
count = 0

while guess != number:
    count += 1
    if guess < number:
        print("think higher...")
    else:
        print("think lower...")
    guess = int(input("Guess: "))
else:
    print("Good. ", "It took you", count, "tries!")
'''    

# File handling
file = open("# Course & textbook concepts.py")
print(file.read())
file.close()

