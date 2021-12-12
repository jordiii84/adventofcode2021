def is_open(symbol):
    is_open_symbol=False
    if symbol in ("(","[","<","{"):
        is_open_symbol=True
    return is_open_symbol

def get_close_symbol(symbol):
    if symbol == "[":
        return "]"
    if symbol == "(":
        return ")"
    if symbol == "{":
        return "}"
    if symbol == "<":
        return ">"

def get_value(symbol):
    if symbol == ")":
        return 1
    if symbol == "]":
        return 2
    if symbol == "}":
        return 3
    if symbol == ">":
        return 4

def calculate_remaining_close(symbols):
    res=0
    print(f"Symbols: {symbols}")
    while len(symbols)>0:
        char=symbols.pop()
        res*=5
        res+=get_value(get_close_symbol(char))
    
    print(f"Result= {res}")
    return res

f = open("input.txt", "r")
lines = f.readlines()

results=[]
for line in lines:
    print(f"--------------------------- line {line}")
    line=line[:-1]
    corrupt=False 
    end=False
    open_chunks=[]
    
    for i in range(len(line)):
        if not corrupt and not end:
            char = line[i]
            if i==len(line)-1:
                end=True

                # print(f"{char} is open char? {is_open(char)}")
                if is_open(char):
                    open_chunks.append(char)

                if char==get_close_symbol(open_chunks[-1]):
                    open_chunks.pop()
                results.append(calculate_remaining_close(open_chunks))
            elif is_open(char):
                open_chunks.append(char)
            elif char!=get_close_symbol(open_chunks[-1]):
                print(f"Found corrupt: {char}")
                corrupt=True
            else:
                open_chunks.pop()


sort_res=sorted(results)

print(f"Middle position is {len(sort_res)//2}")
print(f"Total result {sort_res[(len(sort_res)//2)]}")
