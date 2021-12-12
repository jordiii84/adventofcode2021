f = open("input.txt", "r")
lines = f.readlines()
ages=[int(number) for number in lines[0].split(",")]
print(ages)
ages=[5]
for i in range(18):
    fishes_to_append=0
    for j in range(len(ages)):
        if ages[j]==0:
            ages[j]=6
            fishes_to_append+=1
        else:
            ages[j]-=1
    for i in range(fishes_to_append):
        ages.append(8)
    print(ages)

print(f"There are {len(ages)} fishes")
# increases=0
# for i in range(1,len(lines)):
#     current=int(lines[i])
#     if is_increase(previous,current):
#         increases+=1
#     previous=current

# print(f"Total increases {increases}")
