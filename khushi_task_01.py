def word_counter(text):
    words = text.lower().split()
    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency

sample_text = "python  is easy and python is powerful"
result = word_counter(sample_text)
print(result)