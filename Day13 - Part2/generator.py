lines=[]
lines.append("░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄")
lines.append("░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄")
lines.append("░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░█")
lines.append("░▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░█")
lines.append("█▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒█")
lines.append("█▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█")
lines.append("░█▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█")
lines.append("░░█░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█")
lines.append("░░░█░░██░░▀█▄▄▄█▄▄█▄████░█")
lines.append("░░░░█░░░▀▀▄░█░░░█░███████░█")
lines.append("░░░░░▀▄░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█")
lines.append("░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░█")
lines.append("░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░█")
lines.append("░░░░░░░░░░░░░░▀▄▄▄▄▄▄▄▄▄▄█")

lines=[]

lines.append("")
import random
points=[]
input_array=[]
# for line in lines:
#     print("a")
for line in lines:
    input_line1=[]
    input_line2=[]
    for element in line:
        if element == "▄":
            input_line1.append(" ")
            input_line2.append("#")
        elif element=="▀":
            input_line1.append("#")
            input_line2.append(" ")
        elif element=="█":
            input_line1.append("#")
            input_line2.append("#")
        else:
            input_line1.append(" ")
            input_line2.append(" ")
        
    input_array.append(input_line1)
    input_array.append(input_line2)

lines=input_array.copy()
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j]=="#":
            point=(j,i)
            points.append(point)

# print(points)
# for line in input_array:
#     row=""
#     for element in line:
#         row+=element
    # print(row)

unfolds=8

type_of_folds=("vertical","horizontal")
unfold_duplicate=("one","one","one","two","two","two","both")
# unfold_duplicate=(["two"])
list_of_unfolds=[]
for i in range(unfolds):
    new_points=[]
    type_of_fold=random.choice(type_of_folds)
    # print(f"Type of fold {type_of_fold}")
    fold_along="x" if type_of_fold=="vertical" else "y"
    max_x=0
    max_y=0
    for point in points:
        if point[0]>max_x:
            max_x=point[0]
        if point[1]>max_y:
            max_y=point[1]
    print(f"Type of fold: {type_of_fold}")
    print(f"-Max_x = {max_x}")
    print(f"-Max_y = {max_y}")
    # print(f"Before: {points}")
    list_of_unfolds.append(f"fold along {fold_along}={(max_x+1) if fold_along=='x' else (max_y+1)}")
    if type_of_fold=="vertical":
        for point in points:
            duplicate_mode=random.choice(unfold_duplicate)
            if duplicate_mode=="one":
                new_points.append(point)
            elif duplicate_mode=="two":
                new_point=((max_x+2)+(max_x-point[0]),point[1])
                new_points.append(new_point)
            elif duplicate_mode=="both":
                new_points.append(point)
                new_point=((max_x+2)+(max_x-point[0]),point[1])
                new_points.append(new_point)
    elif type_of_fold=="horizontal":
        for point in points:
            # print(f"Point {point}")
            duplicate_mode=random.choice(unfold_duplicate)
            if duplicate_mode=="one":
                new_points.append(point)
            elif duplicate_mode=="two":
                new_point=(point[0],(max_y+2)+(max_y-point[1]))
                # print(f"Point {point} -- New point {new_point}")
                new_points.append(new_point)
            elif duplicate_mode=="both":
                new_points.append(point)
                new_point=(point[0],(max_y+2)+(max_y-point[1]))
                new_points.append(new_point)

    # print(f"---------------points {points}")
    points=new_points.copy()
    # print(f"---------------points {points}")
    # print(f"After: {points}")

for point in set(points):
    print(f"{point[0]},{point[1]}")

print("")
# for i in range(len(list_of_unfolds)):

#     print(list_of_unfolds[len(list_of_unfolds)-i])
for unfold in list_of_unfolds:
    print(unfold)
    