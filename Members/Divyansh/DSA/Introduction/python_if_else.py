# Problem : if else  (Introduction)
# Link    : hackerrank.com/challenges/python
# Approach: if else elif
# Time O(n) · Space O(1) · Accepted
n = int(input().strip())


if n % 2 != 0:
    print("Weird")
else:
    if n >= 2 and n <= 5:
        print("Not Weird")
    elif n >= 6 and n <= 20:
        print("Weird")
    elif n > 20:
        print("Not Weird")