
def word_counter(word):
    l_word=word.lower()
    words_list=l_word.split()
    
    freq={}
    for words in words_list:
        if words in freq:
            freq[words] +=1
        else:
            freq[words] =1
    return freq           


print(word_counter("Python is easy and Python is poerful"))