import random
import time

"""
Here's my code! Mode 1 is to verify that each sorting algorithm works and uses small lists, while Mode 2 shows how each algorithms handles much larger lists.
"""


dialog=input("Mode? 1 for full lists, 2 for times only ")

def insertion(sorted):
    length = len(sorted)
    i = 1
    while i != length: # Iterating through the list starting at 1
        j = 0
        while j< len(sorted[:i]): # Iterating through the sorted section of whats before i
            if sorted[i]<sorted[j]:
                temp=sorted[i]
                sorted[j+1:i+1]=sorted[j:i] # Swapping
                sorted[j]=temp
            j += 1
        i += 1
    return sorted

def counting_sort(original, min, max):
    counter=[0]*(max-min+1) # initialize counter array
    for i, n in enumerate(original):
        counter[n-min]+=1 # count occurences of each number in unsorted list
    final=[]
    for i,n in enumerate(counter): # iterate through counter array
        e=0
        while e < n: # append number (index of the counter array + minimum value) number of times that the counter array specifies
            final.append(i+min)
            e+=1
    return final

# Generating test case based on mode

if dialog==1:
    length=random.randint(1,15)
if dialog==2:
    length=input("Length of list? ")

i=0
test_case=[]
while i < length:
    if dialog==1:
        test_case.append(random.randint(1,15))
    if dialog==2:
        test_case.append(random.randint(1,500))
    i += 1

# Showing test case

if dialog==1:
    print "\nOriginal List:"
    print test_case
if dialog==2:
    print "\nTest case is %s elements long" % (len(test_case))

# Insertion sorting

print "\nInsertion Sorted List:"
start_time = time.time()
if dialog==1:
    print insertion(test_case)
if dialog==2:
    x=insertion(test_case)
print("--- %s seconds to sort list with %s items---" % ((time.time() - start_time), len(test_case)))
print test_case

# Counting sorting

print test_case
print "\nCounting Sorted List:"
start_time = time.time()
if dialog==1:
    print counting_sort(test_case, min(test_case), max(test_case))
if dialog==2:
    x=counting_sort(test_case, min(test_case), max(test_case))
print("--- %s seconds to sort list with %s items---" % ((time.time() - start_time), len(test_case)))


# TIM Sorting for reference

print "\nTIM Sorted (default python sort for reference):"
start_time = time.time()
if dialog==1:
    print sorted(test_case)
if dialog==2:
    x=sorted(test_case)
print("--- %s seconds to sort list with %s items---" % ((time.time() - start_time), len(test_case)))



