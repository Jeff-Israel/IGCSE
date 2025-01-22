import random

'''
# Programming Task 7.1

number = random.randint(0, 20)
counter = 0

for i in range(0, 10):
    guess = int(input("Guess the number: "))
    if guess == number:
        print("It took you " + str(counter) + " attempts.")
        break
    else: 
        if guess > number:
            print(">")  
            counter += 1
        else:
            print("<")
            counter += 1

if guess != number:
    print("The number is: ", str(number))
'''

'''
# Programming Task 7.2

numbers = list(map(int,input("\nEnter the numbers : ").strip().split()))
desired_number = int(input("Enter the desired number: "))

def scan_for_desired_number():
   found = False
   for i in range(0, len(numbers)+1):
    while found == False and len(numbers) >= numbers[i]:
        if numbers[i] == desired_number:
            found = True
            print("Value found at place", str(i+1))
        else:
           found = False

scan_for_desired_number()


unsorted_numbers = list(map(int, input("\nEnter the numbers to sort them: ").strip().split()))

def sort_numbers(n):
    changed = True
    counter = 0
    while changed == True:
      for x in range(len(n)-1):
        changed = False
        if n[x] > n[x+1]:
            n[x], n[x+1] = n[x+1], n[x]
            changed = True
            counter += 1
        else:  
           changed = False

    def sort_check(a):
       for y in range(len(n)-1):
          if a[y] > a[y+1]:
             changed = True
             sort_numbers(a) 
          else:
             changed = False
    
    sort_check(n)


sort_numbers(unsorted_numbers)
print(unsorted_numbers)
'''

# Programming Task 7.3

num_of_items = int(input("How many items do you want to buy? "))
total = 0
counter = 0

for i in range(num_of_items):
    price = float(input("Enter the price: "))
    total += price

print("The total price is ", str(total))
print("You have entered " + str(counter) + " items")