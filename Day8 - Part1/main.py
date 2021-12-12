f = open("input.txt", "r")
lines = f.readlines()

counter=0
for line in lines:
    output=line[:-1].split(" | ")[1]
    digits=output.split(" ")
    for digit in digits:
        
        if len(digit)!=5 and len(digit)!=6:
            counter+=1

print(f"Total apparences of 1, 4, 7 or 8 is {counter}")