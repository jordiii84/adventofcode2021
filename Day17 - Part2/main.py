def draw_positions(map):
    min_x=5000
    max_x=-5000
    min_y=5000
    max_y=-5000
    for position in map:
        if position[0]>max_x:
            max_x=position[0]
        if position[1]>max_y:
            max_y=position[1]
        if position[0]<min_x:
            min_x=position[0]
        if position[1]<min_y:
            min_y=position[1]
    for j in range(min_x,max_x+1):
        print(f" Min {min_x} Max {max_x}")
        row=[]
        for i in range(min_y, max_y):
            if (j,i) in map:
                row.append("T")
            else:
                row.append("*")
        print(row)
f = open("input.txt", "r")
lines = f.readlines()

target_coordinates={}
coordinates=lines[0].split("target area: ")
coordinates=coordinates[1].split(", ")
coordinates_x=coordinates[0].split("x=")
coordinates_y=coordinates[1].split("y=")
range_x=coordinates_x[1].split("..")
range_y=coordinates_y[1].split("..")
target_coordinates["x"]=(int(range_x[0]),int(range_x[1]))
target_coordinates["y"]=(int(range_y[0]),int(range_y[1]))

range_x_speed=[]
range_y_speed=[]

x_range_found=False
for i in range(target_coordinates["x"][1]+1):
    exceeded_or_not_enough_or_found=False
    speed=i
    steps=0
    print(speed)
    position=0
    while not exceeded_or_not_enough_or_found:
        if i==8:
            print(f"--pos:{position} Speed:{speed}")
            print(f"Position {position} in range? {position in range(target_coordinates['x'][0], target_coordinates['x'][1]+2)}")
        if speed==0 and (position>=target_coordinates["x"][1] or position<=target_coordinates["x"][0]):
            exceeded_or_not_enough_or_found=True
        if position in range(target_coordinates["x"][0], target_coordinates["x"][1]+2):
            range_x_speed.append(i)
            exceeded_or_not_enough_or_found=True
        else:
            position+=speed
            speed-=1

x_range_found=False
for i in range(abs(target_coordinates["y"][0])+1):
    print(f"{i} de y")
    exceeded_or_found=False
    speed=i
    position=0
    while not exceeded_or_found:
        if i==69:
            print(f"--pos:{position} Speed:{speed}")
        if position>abs(target_coordinates["y"][1]):
            exceeded_or_found=True
        if position in range(abs(target_coordinates["y"][1]), abs(target_coordinates["y"][0])+2):
            # print(f"Appending {i} and {-i}")
            if i!=0:
                range_y_speed.append(-i)
            range_y_speed.append(i)
            exceeded_or_found=True
        else:
            position+=speed
            speed+=1

print(range_x_speed)
print(range_y_speed)

targeted_y_speeds=[]
targeted_vectors=[]
positions_targeted=[]
for y_speed in reversed(range_y_speed):
    start_position=(0,0)
    for x_speed in range_x_speed:
        exceeded=False
        found=False
        current_x_speed=x_speed
        current_y_speed=y_speed
        current_position=start_position
        array_positions=[]
        while not exceeded and not found:
            next_step=(current_position[0]+current_x_speed,current_position[1]+current_y_speed)
            array_positions.append(next_step)
            # print(f"-- {next_step}")
            x_in_boundaries=next_step[0]>=target_coordinates["x"][0]and next_step[0]<=target_coordinates["x"][1]
            y_in_boundaries=next_step[1]>=target_coordinates["y"][0]and next_step[1]<=target_coordinates["y"][1]
            if x_in_boundaries and y_in_boundaries:
                # print(f"{next_step} in boundaries - vector:({x_speed},{y_speed})")
                # print(f"{x_in_boundaries} - {y_in_boundaries}")
                targeted_y_speeds.append(y_speed)
                # print(f"Adding ({x_speed},{y_speed}) to target. Next_step= {next_step}. Positions: {array_positions}")
                targeted_vectors.append((x_speed,y_speed))
                positions_targeted.append(next_step)
                found=True
            if next_step[0]>target_coordinates["x"][1] or next_step[1]<target_coordinates['y'][0]:
                exceeded=True
            else:
                current_position=(current_position[0]+current_x_speed,current_position[1]+current_y_speed)
                current_x_speed-=1 if current_x_speed!=0 else 0
                current_y_speed-=1

result=0
for i in range(max(targeted_y_speeds)+1):
    result+=i

# draw_positions(positions_targeted)
# print(len(positions_targeted))
targeted_vectors_v1=targeted_vectors.copy()

targeted_y_speeds=[]
targeted_vectors=[]
positions_targeted=[]
max_y_speed=130
max_x_speed=172
for y_speed in range(-max_y_speed, max_y_speed):
    start_position=(0,0)
    for x_speed in range(-1,max_x_speed):
        exceeded=False
        found=False
        current_x_speed=x_speed
        current_y_speed=y_speed
        current_position=start_position
        array_positions=[]
        while not exceeded and not found:
            next_step=(current_position[0]+current_x_speed,current_position[1]+current_y_speed)
            array_positions.append(next_step)
            # print(f"-- {next_step}")
            x_in_boundaries=next_step[0]>=target_coordinates["x"][0]and next_step[0]<=target_coordinates["x"][1]
            y_in_boundaries=next_step[1]>=target_coordinates["y"][0]and next_step[1]<=target_coordinates["y"][1]
            if x_in_boundaries and y_in_boundaries:
                # print(f"{next_step} in boundaries - vector:({x_speed},{y_speed})")
                # print(f"{x_in_boundaries} - {y_in_boundaries}")
                targeted_y_speeds.append(y_speed)
                # print(f"Adding ({x_speed},{y_speed}) to target. Next_step= {next_step}. Positions: {array_positions}")
                targeted_vectors.append((x_speed,y_speed))
                positions_targeted.append(next_step)
                found=True
            if next_step[0]>target_coordinates["x"][1] or next_step[1]<target_coordinates['y'][0]:
                exceeded=True
            else:
                current_position=(current_position[0]+current_x_speed,current_position[1]+current_y_speed)
                current_x_speed-=1 if current_x_speed!=0 else 0
                current_y_speed-=1

result=0
for i in range(max(targeted_y_speeds)+1):
    result+=i

# draw_positions(positions_targeted)
print(len(positions_targeted))
targeted_vectors_v2=targeted_vectors.copy()
list_difference=[]
for item in targeted_vectors_v2:
  if item not in targeted_vectors_v1:
    list_difference.append(item)
print(list_difference)
# print("------------")
# print(sorted(set(targeted_vectors)))
# print("-------------")
# print(sorted(targeted_vectors))
# print(f"There are {len(set(targeted_vectors))} targeted_vectors")
print(f"There are {len(targeted_vectors)} targeted_vectors")
