from linked_list import LinkedList

l1 = LinkedList()
def merge_sort(linked_list):
    if(linked_list.size()<=1):
        return linked_list
    left_array , right_array = split(linked_list)
    
    left = merge_sort(left_array)
    right = merge_sort(right_array)
    return merge(left,right)
    
def split(linked_list):
    if linked_list ==None or linked_list.head == None:
        left_array = linked_list
        right_array = None
    else:
        mid = linked_list.size()//2
        mid_node = linked_list.nodeAtIndex(mid-1)
        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None
        
        
        
    