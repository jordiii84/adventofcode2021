def sum_element(dict,key,value):
    try:
        dict[key]+=value
    except:
        dict[key]=value
    return dict

f = open("input.txt", "r")
lines = f.readlines()

starting_polymer=lines[0][:-1]
added_letter={}
generate_pairs={}
for i in range(2,len(lines)):
    combination = lines[i].split(" -> ")
    added_letter[combination[0]]=combination[1][:-1]
    generate_pairs[combination[0]]=[combination[0][0]+combination[1][:-1],combination[1][:-1]+combination[0][1]]

occurrences_pairs={}
occurrences_letters={}
for i in range(len(starting_polymer)-1):
    pair=starting_polymer[i:i+2]
    sum_element(occurrences_pairs,pair,1)
for letter in starting_polymer:
    sum_element(occurrences_letters,letter,1)
   
steps=40

for i in range(steps):
    new_ocurrences_pairs={}
    for pair in occurrences_pairs:
        ocurrences_pair=occurrences_pairs[pair]
        new_pairs=generate_pairs[pair]
        for new_pair in new_pairs:
            sum_element(new_ocurrences_pairs,new_pair,ocurrences_pair)
        sum_element(occurrences_letters,added_letter[pair],ocurrences_pair)
    occurrences_pairs=new_ocurrences_pairs.copy()

values=occurrences_letters.values()
print(f"Result = {max(values) - min(values)}")
# print(occurrences_pairs)
# print(occurrences_letters)