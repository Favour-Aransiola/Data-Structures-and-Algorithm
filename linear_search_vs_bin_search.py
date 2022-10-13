testArray = [x for x in range(100,300,2)]
targetValue = 150

def linear_search(array, n):
    assert(array!=None and type(array)==list)
        
    for i in range(len(array)):
        # loops through the array to find match
        assert(array!=None)
        if array[i]==n:
            return i
            
    return None
print('Linear Search produces result in O(n) tries. Position:',linear_search(testArray, targetValue))


# Method 1
def binary_search(array,target):
    assert(array!=None and type(array)==list)
    start =0
    end = len(array)-1
    
    while end>=start:
        # calculates the mid point between first and last
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif array[mid]>target:
            end= mid-1
            # sets a new endpoint while keeping the start.
        elif array[mid]<target:
            start = mid +1
            # sets a new start while keeping the end.
        
    return None


print('Binary Search produces result in O(Log n) tries. Position:',binary_search(testArray, targetValue))



# Method 2
def recursive_binary_search(array, target):
    assert(array!=None and type(array)==list)
    if len(array)==0:
        return None
    midpoint = len(array)//2
    if(array[midpoint]==target):
        return midpoint
    elif (array[midpoint]>target):
        return recursive_binary_search(array[:midpoint], target)
    else:
        return recursive_binary_search(array[midpoint+1:], target)

    
print('Recursive Binary Search produces result in O(Log n) tries. Position',recursive_binary_search(testArray, targetValue)) 
'''
Conclusion:
Binary Search performs better than Linear Search for conditions where:
    i. The data type is an array of numbers
    ii. The array is sorted
'''