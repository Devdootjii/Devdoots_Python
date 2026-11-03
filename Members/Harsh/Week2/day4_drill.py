#D1 String:
def is_palindrome(s):     
    left,right=0,len(s)-1

    while left < right:              
        if s[left] != s[right]:      
            return False
            left += 1                
            right -= 1                   

    return True                      

print(is_palindrome("madam"))   
print(is_palindrome("hello")) 

#PYQ:1

def reverse_words(sentence):
    words = sentence.split()           
    reversed_words = words[::-1]        
    return " ".join(reversed_words)     

print(reverse_words("I love Python"))       

#PYQ:2

def is_anagram(a, b):
    if len(a)!=len(b):
         count_a = {}                         
         count_b = {}
    for ch in a:
        count_a[ch] = count_a.get(ch, 0) + 1
    for ch in b:
        count_b[ch] = count_b.get(ch, 0) + 1
        return count_a == count_b  

print(is_anagram("listen", "silent"))    
print(is_anagram("aab", "abb"))         

#PYQ:3
def first_unique(s):
    count = {}                          
    for ch in s:                        
        count[ch] = count.get(ch, 0) + 1

    for ch in s:                        
        if count[ch] == 1:             
            return ch                   

    return -1                          


print(first_unique("swiss"))        
print(first_unique("aabb"))  

#PYQ:4

def has_duplicate(nums):
    seen = set()                 

    for x in nums:               
        if x in seen:             
            return True           
        seen.add(x)               

    return False                  


print(has_duplicate([1, 2, 3, 2]))    
print(has_duplicate([1, 2, 3]))  

#PYQ:5

def most_common_char(s):
    count = {}                          

    for ch in s:                       
        count[ch] = count.get(ch, 0) + 1

    return max(count, key=count.get)    


print(most_common_char("aabbbcc"))    
print(most_common_char("a"))    
