f = open("input.txt", "r")
lines = f.readlines()
fishes=[int(number) for number in lines[0].split(",")]
days = 256
fishes_dict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}

for i in fishes:
    fishes_dict[int(i)] += 1

for i in range(days):
    old_fishes = fishes_dict[0]
    for j in range(8):
        fishes_dict[j] = fishes_dict[j+1]
    fishes_dict[7] = fishes_dict[8]
    fishes_dict[6] += old_fishes
    fishes_dict[8] = old_fishes

total_fishes = 0
for fish in fishes_dict.items():
    total_fishes += fish[1]

print(f"There are {total_fishes} fishes after {days} days")