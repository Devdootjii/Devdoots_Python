def word_counter(word):
    list_word = word.lower() and word.split() 
    freq = {}
    for words in list_word: 
        if words in freq: 
            freq[words] = freq[words] + 1 
        else:
            freq[words] = 1 
    return freq 
word = "Python is easy and Python is powerful" 
print(word_counter(word))
