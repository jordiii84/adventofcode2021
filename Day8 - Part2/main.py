f = open("input.txt", "r")
lines = f.readlines()

def contains_wires(wires,digit):
    for wire in wires:
        try:
            digit.index(wire)
        except:
            return False
    return True

sum=0
for line in lines:
    conversion_dict={}
    input=line[:-1].split(" | ")[0]
    digits=input.split(" ")
    for digit in digits:
        digit=''.join(sorted(digit))
        if len(digit)==2:
            conversion_dict[digit]=1
        if len(digit)==3:
            conversion_dict[digit]=7
        if len(digit)==4:
            conversion_dict[digit]=4
        if len(digit)==7:
            conversion_dict[digit]=8

    for digit in digits:
        digit=''.join(sorted(digit))
        if len(digit)==6:
            four=list(conversion_dict.keys())[list(conversion_dict.values()).index(4)]
            seven=list(conversion_dict.keys())[list(conversion_dict.values()).index(7)]
            if contains_wires(four,digit):
                conversion_dict[digit]=9
            elif contains_wires(seven,digit):
                conversion_dict[digit]=0
            else:
                conversion_dict[digit]=6
    for digit in digits:
        digit=''.join(sorted(digit))
        if len(digit)==5:
            one=list(conversion_dict.keys())[list(conversion_dict.values()).index(1)]
            six=list(conversion_dict.keys())[list(conversion_dict.values()).index(6)]
            if contains_wires(one,digit):
                conversion_dict[digit]=3
            elif contains_wires(digit,six):
                conversion_dict[digit]=5
            else:
                conversion_dict[digit]=2


    output=line[:-1].split(" | ")[1]
    digit_output=output.split(" ")
    output_0=''.join(sorted(digit_output[0]))
    output_1=''.join(sorted(digit_output[1]))
    output_2=''.join(sorted(digit_output[2]))
    output_3=''.join(sorted(digit_output[3]))
    
    result=1000*conversion_dict[output_0]+100*conversion_dict[output_1]+10*conversion_dict[output_2]+conversion_dict[output_3]
    
    sum+=result
print(f"Total sum is {sum}")