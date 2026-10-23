# day 12
# Name: Divyansh
# what i learn : dry run
# where i stuck : wiritnig the pure logic of progarm

"""
Scenario 1: [10,20,60]
Scenario 2: Empty
Scenario 3: [5,"10","10"]
"""

def process_records(input_filepath,out_filepath):
    summary={}
    try:
        with open(input_filepath,"r") as f:
            for line in f:
                try:
                    parts=line.strip().split(",")
                    name=parts[0]
                    hours=int(parts[1])
                    rate=int(parts[2])
                    if hours<0 or rate <0:
                        continue
                    payout=int(hours)*float(rate)
                    summary[name]=summary.get(name,0)+payout
                except ValueError:
                    print("Invalid number, skip:", line.strip())
                    continue
                except IndexError:
                    print("Missing field, skip:", line.strip())
                    continue
    except FileNotFoundError:
        print("Input file is not avelible!")        
        return
    with open(out_filepath,"w") as f:
        for name,total in summary.items():
            f.write(f"{name}:Rs{total}\n")    

process_records("pome.txt","pome_summry.txt")