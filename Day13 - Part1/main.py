f = open("input.txt", "r")
lines = f.readlines()

points=[]
actions=[]
for line in lines:
    line=line[:-1]
    if line.startswith("fold along "):
        actions.append(line.split("fold along ")[1])
    elif line=="":
        pass
    else:
        coordinate=line.split(",")
        point=(int(coordinate[0]),int(coordinate[1]))
        points.append(point)

action=actions[0].split("=")
value_action=int(action[1])
print(value_action)
axis=action[0]

folded_points=[]
if axis=="x":
    for point in points:
        if point[0]<value_action:
            folded_points.append(point)
        else:
            new_x=value_action-(point[0]-value_action)
            new_point=(new_x,point[1])
            folded_points.append(new_point)

if axis=="y":
    for point in points:
        if point[1]<value_action:
            folded_points.append(point)
        else:
            new_y=value_action-(point[1]-value_action)
            new_point=(point[0],new_y)
            folded_points.append(new_point)

points=set(folded_points)
print(f"There are {len(points)} points")