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
    counter = 0
    changed = True
    while changed == True or counter <= len(n)+1:
        changed = False
        for x in range(len(n)-1):
            if n[x] > n[x+1]:
                n[x], n[x+1] = n[x+1], n[x]
                changed = True
            else:
                changed = False
                counter += 1



sort_numbers(unsorted_numbers)
print(unsorted_numbers)
'''

'''
# Programming Task 7.3

num_of_items = int(input("How many items do you want to buy? "))
total = 0
counter = 0
avg_cost = total/num_of_items

for i in range(num_of_items):
    price = float(input("Enter the price: "))
    total += price
    counter += 1

print("The total price is ", str(total))
print("You have entered " + str(counter) + " items")
print("The average cost is: " str(avg_cost))
'''

'''
# Programming Task 7.4

parcel_below_1_kg = 0
parcel_between_1_and_2_kg = 0
parcel_above_2_kg = 0
num_of_parcels = int(input("Enter the number of parcels: "))

for t in range(num_of_parcels):
    parcel_weight = float(input("Enter the weight of the parcel: "))
    if parcel_weight < 1:
        parcel_below_1_kg += 1
    elif parcel_weight >= 1 and parcel_weight <= 2:
        parcel_between_1_and_2_kg += 1
    elif parcel_weight > 2:
        parcel_above_2_kg += 1

print("There are " + str(parcel_below_1_kg) + " parcels below 1 kg.")
print("There are " + str(parcel_between_1_and_2_kg) + " parcels between 1 and 2 kg.")
print("There are " + str(parcel_above_2_kg) + " parcels above 2 kg.")
'''