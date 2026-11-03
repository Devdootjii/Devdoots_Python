#Problam=1
#list

N = int(input())
ans = []

for i in range(N):
    command = input()
    val=command.split();
    match val[0]:
        case "insert":
            ans.insert(int(val[1]),int(val[2]))
        case "remove":
            ans.remove(int(val[1]))
        case "append":
            ans.append(int(val[1]))
        case "sort":
            ans.sort()
        case "pop":
            ans.pop()
        case "reverse":
            ans.reverse()
        case "print":
            print(ans)                


#Problam=2
#tuple


n = int(raw_input())
t = tuple(map(int, raw_input().split()))
print(hash(t))


#Problam=3
#swap case

def swap_case(s):
    result = ""
    for ch in s:
        if ch.islower():
            result += ch.upper()
        elif ch.isupper():
            result += ch.lower()
        else:
            result += ch   
    return result


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)