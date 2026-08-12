def word_counter(text):
    word= text.lower().split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] +=1
        else:
            freq[word]=1
            return freq
            
