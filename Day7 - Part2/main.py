def calculate_fuel(num):
    result=0
    i=num
    while i>0:
        result+=i
        i-=1
    # print(result)
    return result


f = open("input.txt", "r")
lines = f.readlines()
positions=[int(number) for number in lines[0].split(",")]
print(positions)
moves_to_position=[]
for position in range(max(positions)):
    current_moves=0
    for from_position in positions:
        # print(f"From {from_position} to {position}")
        current_moves+=calculate_fuel(abs(position-from_position))
    moves_to_position.append(current_moves)

print(moves_to_position)
print(f"Less movements are {min(moves_to_position)}")


