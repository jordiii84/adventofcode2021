def is_increase(a, b):
    return a<b

f = open("input.txt", "r")
lines = f.readlines()
previous=int(lines[0])
increases=0
for i in range(1,len(lines)):
    current=int(lines[i])
    if is_increase(previous,current):
        increases+=1
    previous=current

print(f"Total increases {increases}")
