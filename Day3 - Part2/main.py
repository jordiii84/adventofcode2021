def hex_to_dec(hex):
    dec=0
    for x in range(len(hex)):
        dec+=2**(len(hex)-x-1)*int(hex[x])
    return dec

f = open("input.txt", "r")
lines = f.readlines()
bit_length=len(lines[0])


oxygen_candidates=lines
found=False
i=0
while i<bit_length-1 and not found:
    # print("------------------------------------------------------------------")
    sum_column=0
    for j in range(len(oxygen_candidates)):
        # print(f"lines[{j}][{i}]: {lines[j][i]}")
        sum_column+=int(oxygen_candidates[j][i])
    # print(f"sum_column{i}:{sum_column} - len(lines)/2: {len(oxygen_candidates)/2}")
    most_common=0 if sum_column<len(oxygen_candidates)/2 else 1
    new_oxigen_candidates=[]
    # print(f"most common: {most_common}")
    for k in range(len(oxygen_candidates)):
        # print(f"{oxygen_candidates[k][:-1]} is {oxygen_candidates[k][i]} == {most_common}? {oxygen_candidates[k][i]==most_common}")
        if int(oxygen_candidates[k][i])==most_common:
            new_oxigen_candidates.append(oxygen_candidates[k])

    # if i==1:
    #     found=True
    # print(f"New oxygen candidates: {len(new_oxigen_candidates)}")
    if new_oxigen_candidates == 1:
        found=True
    else:
        oxygen_candidates=new_oxigen_candidates
        i+=1
    
    # print(f"Found? {found} . Remaining candidates {len(oxygen_candidates)}")

print(f"oxygen = {oxygen_candidates[0]}")

oxygen=oxygen_candidates[0][:-1]

co2_candidates=lines
found=False
i=0
while i<bit_length-1 and not found:
    # print("------------------------------------------------------------------")
    sum_column=0
    for j in range(len(co2_candidates)):
        # print(f"lines[{j}][{i}]: {lines[j][i]}")
        sum_column+=int(co2_candidates[j][i])
    # print(f"sum_column{i}:{sum_column} - len(lines)/2: {len(co2_candidates)/2}")
    most_common=1 if sum_column<len(co2_candidates)/2 else 0
    new_co2_candidates=[]
    # print(f"less common: {most_common}")
    for k in range(len(co2_candidates)):
        # print(f"{co2_candidates[k][:-1]} is {co2_candidates[k][i]} == {most_common}? {int(co2_candidates[k][i])==most_common}")
        if int(co2_candidates[k][i])==most_common:
            new_co2_candidates.append(co2_candidates[k])

    # if i==1:
    #     found=True
    # print(f"New oxygen candidates: {len(new_oxigen_candidates)}")
    if len(new_co2_candidates) == 1:
        found=True
    else:
        i+=1
    co2_candidates=new_co2_candidates
    
    # print(f"Found? {found} . Remaining candidates {len(co2_candidates)}")

print(f"co2 = {co2_candidates[0]}")

co2=co2_candidates[0][:-1]

oxygen_dec=hex_to_dec(oxygen)
co2_dec=hex_to_dec(co2)


print(f"oxygen->{oxygen}  co2->{co2}")
print(f"oxygen_dec->{oxygen_dec}  co2_dec->{co2_dec}")
print(f"Power consuption = {oxygen_dec*co2_dec}")