import math
def make_addition(value1,value2):
    result=[]
    result.append("[")
    for value in value1:
        result.append(value)
    result.append(",")
    for value in value2:
        result.append(value)
    result.append("]")
    return result

def print_int(value):
    result=""
    for element in value:
        result+=str(element)

    print(result)

def get_explodable_index(number):
    nested_pairs=0
    i=0
    found=False
    while i<len(number) and not found:
        if number[i]=="[":
            nested_pairs+=1
        elif number[i]=="]":
            nested_pairs-=1
        if nested_pairs>4:
            last_open=i
            while number[i+1]!="]":
                if number[i+1]=="[":
                    last_open=i+1
                i+=1
            i=last_open
            found=True
        i+=1
    return i if found else -1

def get_splitable_index(number):
    i=0
    found=False
    while i<len(number) and not found:
        try:
            int(number[i])
            if number[i]>9:
                return i
            i+=1
        except:
            i+=1
    return -1

def explode_number(number,index):
    previous_int_index=get_previous_int(number,index-1)
    next_int_index=get_next_int(number,index+3)
    left_element=number[index]
    right_element=number[index+2]
    if previous_int_index!=-1:
        number[previous_int_index]+=left_element
    if next_int_index!=-1:
        number[next_int_index]+=right_element
    
    new_number=[]
    for element in range(index-1):
        new_number.append(number[element])
    new_number.append(0)
    for element in range(index+4,len(number)):
        new_number.append(number[element])
    return new_number

def split_number(number,index):
    new_number=[]
    for element in range(index):
        new_number.append(number[element])
    new_number.append("[")
    new_number.append(math.floor(number[index]/2))
    new_number.append(",")
    new_number.append(math.ceil(number[index]/2))
    new_number.append("]")
    for element in range(index+1,len(number)):
        new_number.append(number[element])
    return new_number

def get_previous_int(number,index):
    for i in reversed(range(index+1)):
        try:
            int(number[i])
            return i
        except:
            pass
    return -1

def calculate_magnitude(value1,value2):
    return 3*value1+2*value2

def get_magnitude(addition):
    found=False
    while not found:
        i=0
        new_addition=[]
        while i < len(addition):
            if addition[i]=="[" and addition[i+2] == "," and addition [i+4]=="]":
                new_addition.append(calculate_magnitude(addition[i+1],addition[i+3]))
                i+=4
            else:
                new_addition.append(addition[i])
            i+=1
        if addition==new_addition:
            found=True
        else:
            addition=new_addition.copy()
        print(addition)
    return new_addition


f = open("input.txt", "r")
lines = f.readlines()

def get_next_int(number,index):
    for i in range(index,len(number)):
        try:
            int(number[i])
            return i
        except:
            pass
    return -1

lines_int=[]
for line in lines:
    new_line=[]
    for element in line[:-1]:
        if element in ["[","]",","]:
            new_line.append(element)
        else:
            new_line.append(int(element))
    lines_int.append(new_line)

addition=lines_int[0]
print("New number")
print_int(addition)
for i in range(1,len(lines)):
    print(f"Adding")
    print_int(lines_int[i])
    addition=make_addition(addition,lines_int[i])
    print("Added")
    print_int(addition)
    reduced=False
    while not reduced:
        explodable_index=get_explodable_index(addition)
        splittable_index=get_splitable_index(addition)
        if explodable_index==-1 and splittable_index==-1:
            reduced=True
        elif explodable_index!=-1:
            # print(f"Exploding {addition[explodable_index]}{addition[explodable_index+1]}{addition[explodable_index+2]}")
            addition=explode_number(addition,explodable_index)
        elif splittable_index!=-1:
            # print(f"Splitting {addition[splittable_index]}")
            addition=split_number(addition,splittable_index)
        # print("---Reducing")
        # print_int(addition)
    print("Reduced")
    print_int(addition)

magnitude=get_magnitude(addition)
print(magnitude)
