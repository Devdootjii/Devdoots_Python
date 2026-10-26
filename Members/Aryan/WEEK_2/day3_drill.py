# P1 - Second largest number

a = [10, 5, 20, 8]

first = a[0]
second = None

for n in a:
    if n > first:
        second = first
        first = n
    elif n != first and (second is None or n > second):
        second = n

print(second)
# P2 - Duplicate check

a = [1, 2, 3, 2]
seen = set()

for n in a:
    if n in seen:
        print(True)
        break
    seen.add(n)
else:
    print(False)
    # P3 - Frequency count

a = [1, 2, 2, 3, 2]
target = 2
count = 0

for n in a:
    if n == target:
        count += 1

print(count)
# P4 - Merge sorted lists

a = [1, 3, 5]
b = [2, 4, 6]

i = 0
j = 0
result = []

while i < len(a) and j < len(b):
    if a[i] < b[j]:
        result.append(a[i])
        i += 1
    else:
        result.append(b[j])
        j += 1

result.extend(a[i:])
result.extend(b[j:])

print(result)
# P5 - Binary search

def binary_search(a, target):
    low = 0
    high = len(a) - 1

    while low <= high:
        mid = (low + high) // 2

        if a[mid] == target:
            return True
        elif a[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return False


a = [10, 20, 30, 40, 50]

print(binary_search(a, 30))
print(binary_search(a, 70))

# P-6 bubble sort in descending
numbers = [5, 1, 4, 2, 8]

for i in range(len(numbers)):
    for j in range(len(numbers) - 1):
        if numbers[j] < numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(numbers)