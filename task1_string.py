# freq count task
def word_conter(txt):
    wods = txt.lower().split()
    frq = {}
    
    for w in wods:
        if w in frq:
            frq[w] = frq[w] + 1
        else:
            frq[w] = 1
            
    return frq

# checking
tst_str = "Python is easy and Python is powerful"
print(word_conter(tst_str))