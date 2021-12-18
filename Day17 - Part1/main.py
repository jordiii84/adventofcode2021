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
    while not exceeded_or_not_enough_or_found:
        position=speed*steps
        if speed==0 and (position>target_coordinates["x"][1] or position<target_coordinates["x"][0]):
            exceeded_or_not_enough_or_found=True
        if position in range(target_coordinates["x"][0], target_coordinates["x"][1]+1):
            range_x_speed.append(speed)
            exceeded_or_not_enough_or_found=True
        else:
            speed-=1
            steps+=1

x_range_found=False
for i in range(abs(target_coordinates["y"][0])+1):
    exceeded_or_found=False
    speed=i
    position=0
    while not exceeded_or_found:
        if position>abs(target_coordinates["y"][1]):
            exceeded_or_found=True
        if position in range(abs(target_coordinates["y"][1]), abs(target_coordinates["y"][0])+1):
            range_y_speed.append(i)
            exceeded_or_found=True
        else:
            position+=speed
            speed+=1

print(range_x_speed)
print(range_y_speed)

targeted_y_speeds=[]
targeted_vectors=[]
for y_speed in reversed(range_y_speed):
    start_position=(0,0)
    for x_speed in range_x_speed:
        exceeded=False
        print(f"Trying vector ({x_speed},{y_speed})")
        current_x_speed=x_speed
        current_y_speed=y_speed
        current_position=start_position
        while not exceeded:
            next_step=(current_position[0]+current_x_speed,current_position[1]+current_y_speed)
            print(f"-- {next_step}")
            x_in_boundaries=next_step[0]>=target_coordinates["x"][0]and next_step[0]<=target_coordinates["x"][1]
            y_in_boundaries=next_step[1]>=target_coordinates["y"][0]and next_step[1]<=target_coordinates["y"][1]
            if x_in_boundaries and y_in_boundaries:
                print(f"{next_step} in boundaries - vector:({x_speed},{y_speed})")
                print(f"{x_in_boundaries} - {y_in_boundaries}")
                targeted_y_speeds.append(y_speed)
            if next_step[0]>target_coordinates["x"][1] or next_step[1]<target_coordinates['y'][0]:
                exceeded=True
            else:
                current_position=(current_position[0]+current_x_speed,current_position[1]+current_y_speed)
                current_x_speed-=1 if current_x_speed!=0 else 0
                current_y_speed-=1

print(targeted_y_speeds)

result=0
for i in range(max(targeted_y_speeds)+1):
    result+=i

print(result)