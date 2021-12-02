def is_increase(a, b):
    return a<b

f = open("input_test.txt", "r")
lines = f.readlines()

windows=[]
for i in range(len(lines)-2):
    windows.append(int(lines[i])+int(lines[i+1])+int(lines[i+2]))

increases=0
for i in range(len(windows)-1):
    previous=int(windows[i])
    current=int(windows[i+1])
    if is_increase(previous,current):
        increases+=1
    previous=current

print(f"Total increases {increases}")
