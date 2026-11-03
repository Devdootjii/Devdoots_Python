'''
#D1:Basic
marks = {"Riya": 90, "Aman": 65, "Sana": 78}
for name, m in marks.items():
    print(name, "=", m)


#D2:Add/Delete

marks={"Riya":90,"Aman":65,"Sara":78}
marks["Dev"]=88
del marks["Aman"]

for name,m in marks.items():
    print(name,m)

#D3:Max

marks = {"Riya": 90, "Aman": 65, "Sara": 78}

top, best = "", -1
for name, m in marks.items():
    if m > best:
        best, top = m, name

print(top, best)

#D4: Merge

d1 = {"a": 1}
d2 = {"b": 2}

merged = {}
for k, v in d1.items():
    merged[k] = v
for k, v in d2.items():
    merged[k] = v

print(merged)

#Naya concept — Files & JSON

import json

data = {"score": 90, "level": 3}

with open("save.json", "w") as f:
    json.dump(data, f)

with open("save.json", "r") as f:
    back = json.load(f)

print(back["score"])

# Practice 1
import json

students = [{"name": "Riya", "marks": 90}]

def save(data, path):
    with open(path, "w") as f:
        json.dump(data, f)

def load(path):
    with open(path, "r") as f:
        return json.load(f)

save(students, "students.json")
back = load("students.json")
print(back[0]["name"])

#Practice 2

import json

def load_high():
    try:
        with open("high.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return 0

def save_high(score):
    with open("high.json", "w") as f:
        json.dump(score, f)

high = load_high()
print("High score:", high)'''

# PYQ 1
s = "abaca"
freq = {}

for ch in s:
    if ch in freq:
        freq[ch] = freq[ch] + 1
    else:
        freq[ch] = 1

print(freq)

#PYQ:2
d = {"a": 1, "b": 2}

new = {}
for k, v in d.items():
    new[v] = k

print(new) 
