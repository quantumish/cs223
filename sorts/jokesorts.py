import random
import time

dialog=input("Mode? 1 for full lists, 2 for times only ")

def stalin_sort(original):
    i=1
    while i < len(original):
        if original[i-1]>original[i]: # check if sorted
            del original[i] # if not, delete
        else:
            i+=1
    return original

def check_sorted(original):
    i=1
    while i < len(original):
        if original[i] < original[i-1]:
            return False
        i+=1
    return True

def bogosort(original):
    unsorted=True
    while unsorted==True:
        random.shuffle(original)
        if check_sorted(original)==True:
            break
    return original

# Generating test case based on mod
x
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

# Stalin sorting
testcase2=test_case[:] # Stalin sort is in-place
print "\nStalin Sort:"
start_time = time.time()
if dialog==1:
    print stalin_sort(test_case)
if dialog==2:
    x=stalin_sort(test_case)
print("--- %s seconds to sort list with %s items---" % ((time.time() - start_time), len(test_case)))

# Bogosorting
testcase3=test_case[:] # Bogo sort is in-place
print "\nBogo Sort:"
start_time = time.time()
if dialog==1:
    print bogosort(testcase2)
if dialog==2:
    x=bogosort(testcase2)
print("--- %s seconds to sort list with %s items---" % ((time.time() - start_time), len(test_case)))
