# Practice
def bobble_sort(a):
    n = len(a)
    for i in range(n-1):
        for j in range(n-1-i):
            if a[j]<a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a
print(bobble_sort([5,1,4,2,8]))

# Practice

def binary_search(a,target):
    low,high=0,len(a)-1
    while low<=high:
        mid=(low+high) // 2
        if a[mid]== target:
            return True
        elif a[mid]<target:
            low = mid +1
        else:
            low = mid-1
    return False
print(binary_search([1,2,3,4,5,8],5))

# PYQ 1
def second_largest(nums):
    first = second = float('-inf')
    for n in nums:
        if n > first:
            second = first
            first = n
        elif n > second and n != first:
            second = n
    return second if second != float('-inf') else None

print(second_largest([10, 5, 20, 8]))  # 10


# PYQ 2
def has_duplicate(nums):
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False

print(has_duplicate([1, 2, 3, 2]))  
print(has_duplicate([1, 2, 3]))     


# PYQ 3
a=[1,2,2,3,2]
count=0
target =2
for i in a:
    if target ==i:
        count+=1
print(count)

# PYQ 4
def merge_sorted(a, b):
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

print(merge_sorted([1, 3, 5], [2, 4, 6]))  
