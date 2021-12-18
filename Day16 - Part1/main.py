def to_bin(a):
    if a=="0":
        return "0000"
    if a=="1":
        return "0001"
    if a=="2":
        return "0010"
    if a=="3":
        return "0011"
    if a=="4":
        return "0100"
    if a=="5":
        return "0101"
    if a=="6":
        return "0110"
    if a=="7":
        return "0111"
    if a=="8":
        return "1000"
    if a=="9":
        return "1001"
    if a=="A":
        return "1010"
    if a=="B":
        return "1011"
    if a=="C":
        return "1100"
    if a=="D":
        return "1101"
    if a=="E":
        return "1110"
    if a=="F":
        return "1111"

def to_dec(bin):
    dec=0
    for i in range(len(bin)):
        dec+=int(bin[i])*(2**(len(bin)-i-1))
    return dec

def parse_packet(string,sub_string,total_version):
# HELPER
# literal: VVVTTT

# operator: VVVTTTI if TTT=100
#   TTT==100
#   I=1 -> 11 next bits
#   I=0 -> 15 next bits
    i=0
    print(f"{sub_string}------------------------------------------")
    print(f"{sub_string}Parsing {string}")
    version=string[i:i+3]
    total_version+=to_dec(version)
    i+=3
    print(f"{sub_string}Version: {version} - {to_dec(version)} ")
    type=string[i:i+3]
    i+=3
    type_string = "Operator" if type!="100" else "Literal"
    print(f"{sub_string}Type: {type}({to_dec(type)}) - {type_string}")
    if type!="100":
        print(f"{sub_string}I: {string[i]}")
        length=15 if string[i]=="0" else 11
        i+=1
        value_length=to_dec(string[i:i+length])
        print(f"{sub_string}length: {string[i:i+length]}({value_length})")
        i+=length
        if length==15:
            string_to_parse=string[i:i+value_length]
            j=0
            while len(string_to_parse[j:])>0:
                k,total_version=parse_packet(string_to_parse[j:],"  "+sub_string,total_version)
                j+=k
            i+=value_length
        else:
            for j in range(value_length):
                new_i,total_version=parse_packet(string[i:],"  "+sub_string,total_version)
                i+=new_i
    else:
        last=False
        literal=""
        while not last:
            last=True if string[i] == "0" else False
            i+=1
            literal+=string[i:i+4]
            i+=4
        
        print(f"{sub_string}Literal: {literal}({to_dec(literal)})")

    return i,total_version

f = open("input.txt", "r")
lines = f.readlines()
dec=lines[0]
bin=""
for char in dec:
    bin+=to_bin(char)
i,version=parse_packet(bin,"",0)
print(f"Total versions {version}")

