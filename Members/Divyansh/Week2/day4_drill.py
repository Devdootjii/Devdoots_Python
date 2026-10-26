# D1
def is_palindrome(st):
    st=st.lower()
    left ,right =0,len(st)-1
    while left < right:
        if st[left]!=st[right]:
            return False
        left +=1
        right -=1
    return True
print(is_palindrome("Madam"))
print(is_palindrome("hello"))

# D2
def count_vowel(s):
    a=set("aeiou")
    s=s.lower()
    count=0
    for i in s:
        if i in a:
            count+=1
    return count
print(count_vowel("Apple"))

# D3
def first_unique(s):
    count={}
    for ch in s:
        count[ch ]= count.get(ch,0)+1

    for ch in s:
        if count[ch]==1:
            return ch
    return -1
print(first_unique("swiss"))

# D4
def remove_duplicate(l):
    s=set()
    result=[]
    for i in l:
        if i not in s:
            s.add(i)
            result.append(i)
    return result
print(remove_duplicate([3,1,3,2,1]))

# D5

def is_anagram(s1,s2):
    if len(s1)!=len(s2):
        return False
    cs1,cs2={},{}
    for ch in s1:
        cs1[ch] = cs1.get(ch,0)+1
    for ch in s2:
        cs2[ch] = cs2.get(ch,0)+1
    return cs1 ==cs2
print(is_anagram("listen", "silent"))  
print(is_anagram("aab", "abb")) 

# D6

def max_word(s):
    s=s.split()
    best_word = ""
    for i in s:
        if len(i)>len(best_word):
            best_word=i
    return best_word
print(max_word("I am learning Python"))

# PYQ1

def reverse(s):
    s=s.split()
    words=[]
    for w in s:
        words.append(w)
    r_words=words[::-1]
    return " ".join(r_words)
print(reverse("I love Python"))

# PYQ2
def valid_anagram(a,b):
    if len(a)!=len(b):
        return False
    ca,cb ={},{}
    for ch in a:
        ca[ch]=ca.get(ch,0)+1
    for ch in b:
        cb[ch]=cb.get(ch,0)+1
    return ca==cb
print(valid_anagram("Madam", "damma"))
print(is_anagram("listen", "silent"))