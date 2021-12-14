f = open("input_test.txt", "r")
lines = f.readlines()

starting_polymer=lines[0][:-1]
insertions={}
for i in range(2,len(lines)):
    combination = lines[i].split(" -> ")
    insertions[combination[0]]=combination[1][:-1]

window=2
steps=15
for step in range(steps):
    new_polymer=""
    for i in range(len(starting_polymer)-1):
        combination=starting_polymer[i]+starting_polymer[i+1]
        insertion=insertions[combination]
        new_polymer+=combination[0]+insertion
        if i==len(starting_polymer)-2:
            new_polymer+=combination[1]
    starting_polymer=new_polymer
    print(new_polymer)
max_occurrences=0
min_occurrences=0
occurrences={}
for element in set(starting_polymer):
    occurrences[element]=starting_polymer.count(element)

values=occurrences.values()
print(f"Result = {max(values) - min(values)}")
print(occurrences)
print(len(starting_polymer))
print(insertions)