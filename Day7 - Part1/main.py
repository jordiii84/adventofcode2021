def is_increase(a, b):
    return a<b

f = open("input.txt", "r")
lines = f.readlines()
print(lines[0])
positions=[int(number) for number in lines[0].split(",")]
print(max(positions))
moves_to_position=[]
for position in positions:
    current_moves=0
    for from_position in positions:
        current_moves+=abs(position-from_position)
    moves_to_position.append(current_moves)

print(f"Less movements are {min(moves_to_position)}")

# previous=int(lines[0])
# increases=0
# for i in range(1,len(lines)):
#     current=int(lines[i])
#     if is_increase(previous,current):
#         increases+=1
#     previous=current

# print(f"Total increases {increases}")
