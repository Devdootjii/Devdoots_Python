def bubble_sort(a):
    n = len(a)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:          
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

print(bubble_sort([5, 1, 4, 2, 8]))  

#Practice:1
def bubble_sort(a):
    n = len(a)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if a[j] < a[j + 1]:          
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

print(bubble_sort([5, 1, 4, 2, 8]))  

#Binary Search

def binary_search(a, target):
    low, high = 0, len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == target:
            return mid
        elif a[mid] < target:
            low = mid + 1           
        else:
            high = mid - 1          
    return -1

print(binary_search([1, 2, 4, 5, 8], 5))

#Practice:2

def binary_search(a, target):
    low, high = 0, len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == target:
             return True
        elif a[mid] < target:
            low = mid + 1           
        else:
            high = mid - 1          
    return False   

print(binary_search([1, 2, 4, 5, 8], 5))

#PYQ:1

def second_largest(a):
    first = second = float('-inf')
    for n in a:
        if n > first:
            second = first
            first = n
        elif n > second:
            second = n
    return second

print(second_largest([10, 5, 20, 8]))  

#PYQ:2

def has_duplicate(a):
    seen = set()         
    for n in a:
        if n in seen:    
            return True
        seen.add(n)       
    return False          

print(has_duplicate([1, 2, 3, 2]))  
print(has_duplicate([1, 2, 3])) 

#PYQ:3

def frequency(a, target):
    count = 0
    for n in a:
        if n == target:
            count += 1
    return count

print(frequency([1, 2, 2, 3, 2], 2))

#PYQ:4

def merge(a, b):
    i = j = 0
    result = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])   
    result.extend(b[j:])   
    return result

print(merge([1, 3, 5], [2, 4, 6]))   



 
