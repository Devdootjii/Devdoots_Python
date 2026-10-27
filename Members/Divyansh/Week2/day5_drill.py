import json
# d1
marks ={"Riya":90,"Aman":65,"Sara":78}
for name,m in marks.items():
    print(name,m)

# d2

marks["Dev"]=68
del marks["Aman"]
print(marks)

# d3
top,best ="",-1
for name,m in marks.items():
    if m >best:
        best,top=m,name

print(top,best)

# d4
def merge(d1,d2):
    out ={}
    for k,v in d1.items(): out[k]=v
    for k,v in d2.items(): out[k]=v
    return out

# d5
d = {"a": 1}
print(d.get("b",0))

# PYQ 1 
def freq(words):
    d = {}
    for w in words:
        d[w] = d.get(w, 0) + 1
    return d
print(freq("Rhohan3"))
# PYQ 2 
def invert(d):
    return {v: k for k, v in d.items()}

# PYQ 3 
def merge_sum(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, 0) + v
    return out

# PYQ 4 
with open("student.json","r") as f:
    students = json.load(f)
top = students[0]
for s in students:
    if s["marks"] > top["marks"]:
        top = s
print(top["name"])