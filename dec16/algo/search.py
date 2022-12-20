def linear_search(list, target):
    """
        Returns the targets position
        if found
    """
    for item in range(0, len(list)):
        if list[item] == target:
            return item
        return None
        
def binary_search(list, target):
    first = list[0]
    last = list[len(target) - 1]
    while first <= last:
        mid = (first+ last)// 2
        if list[mid] == target: 
            return mid
        elif list[mid]  < target:
            first = mid + 1
        else:
            last = mid - 1 
        
    return 'Not found'

def recur_b_search(list,target):
    if len(list) == 0:
        return None
    else: 
        mid = len(list) // 2
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            return recur_b_search(list[mid + 1:], target)
        else:
            return recur_b_search(list[:mid - 1], target)

