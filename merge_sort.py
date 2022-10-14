def merge_sort (array):
    if(len(array)<=1):
        return array
    left_array, right_array = split(array)
    left = merge_sort(left_array)
    right = merge_sort(right_array)
    
    
    return merge(left, right)

def split(array):
    mid = len(array)//2
    return array[:mid], array[mid:]


def merge(left, right):
    result =[]
    left_index = right_index = 0
    
    while left_index<len(left) and right_index<len(right):
        
        if left[left_index]<right[right_index]:
            result.append(left[left_index])
            left_index+=1
        else: 
            result.append(right[right_index])
            right_index+=1
    
    while left_index< len(left):
        
        result.append(left[left_index])
        left_index+=1
    while right_index< len(right):
        
        result.append(right[right_index])
        right_index+=1
    return result

            
    
merged = merge_sort([10,29,32,1,232,212,2,12,2])
print(merged)