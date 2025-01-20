# Course & textbook concepts

# Sorting ALgorithms
def insertion_sort(n):
    sorted_list = [n[0]]

    # Comparing the item and putting it in the right place IS the algorithm!
    # Try placing the item using an AND condition where it's between the smaller & larger numbers.
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
