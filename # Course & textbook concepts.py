# Course & textbook concepts

'''
# Sorting Algorithms
def insertion_sort(n):
    sorted_list = [n[0]]

    for i in range(1, len(n)): 
        sorted_list.append(n[i])
        for x in range(len(sorted_list)-1):
           while sorted_list[i] > sorted_list[x]:
             sorted_list[i], sorted_list[x] = sorted_list[x], sorted_list[i]
           while sorted_list[i] < sorted_list[x]:
             sorted_list[x], sorted_list[i] = sorted_list[i], sorted_list[x]
           
    print(sorted_list)
    
unsorted_numbers = list(map(int, input("Enter the numbers to sort them: ").strip().split()))
insertion_sort(unsorted_numbers)

# Challenge: Make it more efficient using only while-else loops or by getting rid of the nested loops.
'''

'''
def merge_sort(n):
   sorted_list = [n[0]]
   # Sort this list, sort as many items as the size of the sorted list, now merge and sort it all.
'''

'''
passes = 0
Names = list(map(str, input("Enter the names: ").strip().split()))

while passes <= len(Names):
    for i in range(len(Names)-1):
      if Names[i][0] > Names[i+1][0]:
          Names[i], Names[i+1] = Names[i+1], Names[i]
      elif Names[i][0] == Names[i+1][0] and Names[i][1] > Names[i+1][1]:
          Names[i], Names[i+1] = Names[i+1], Names[i] 
    passes += 1

print(Names)
'''

# Bubble sort of alphabets - IMPORTANT AND HARD
passes = 0
Names = list(map(str, input("Name plz: ").strip().split()))

while passes <= len(Names):
    for i in range(len(Names)-1):
        changed = False
        if Names[i][0] > Names[i+1][0]:
          Names[i], Names[i+1] = Names[i+1], Names[i]
        if min(Names[i], Names[i+1]) in max(Names[i], Names[i+1]) and len(Names[i]) > len(Names[i+1]):
          Names[i], Names[i+1] = Names[i+1], Names[i] 
        else:
          for j in range(1, min(len(Names[i]), len(Names[i+1]))):
            if  Names[i][0] == Names[i+1][0] and Names[i][j-1] == Names[i+1][j-1] and Names[i][j] > Names[i+1][j] and changed == False:
                Names[i], Names[i+1] = Names[i+1], Names[i]
                changed = True
    passes += 1

print(Names)

''' L8 Programming: String manipulation
stringInput = str(input("Enter a message: "))
for count in range(0, len(stringInput)):
  character = stringInput[count:count+1]
  print(character)
# character = stringInput[len(stringInput)-3:]

print(stringInput.lower())
print(stringInput.upper())
'''