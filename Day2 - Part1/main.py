f = open("input.txt", "r")
lines = f.readlines()

coordinates=[0,0]
aim=0
for i in range(len(lines)):
    command = lines[i].split(" ")
    if command[0] == "forward":
        coordinates[0]+=int(command[1])
    elif command[0] == "up":
        coordinates[1]-=int(command[1])
    elif command[0] == "down":
        coordinates[1]+=int(command[1])

        aim+=int(command[1])
    

print(f"Result = {coordinates[0]} * {coordinates[1]} = {coordinates[0]*coordinates[1]}")
