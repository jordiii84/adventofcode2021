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
    if symbol == "]":
        return 57
    if symbol == ")":
        return 3
    if symbol == "}":
        return 1197
    if symbol == ">":
        return 25137
f = open("input.txt", "r")
lines = f.readlines()

corrupt_symbols=[]
for line in lines:
    line=line[:-1]
    corrupt=False 
    end=False
    open_chunks=[]
    
    for i in range(len(line)):
        if not corrupt and not end:
            char = line[i]
            if i==len(line)-1:
                end=True
            if is_open(char):
                open_chunks.append(char)
            elif char!=get_close_symbol(open_chunks[-1]):
                print(f"Found corrupt: {char}")
                corrupt=True
                corrupt_symbols.append(char)
            else:
                open_chunks.pop()

print(f"Total corrupts found {corrupt_symbols}")


result=0
for symbol in corrupt_symbols:
    result+=get_value(symbol)

print(f"Total result {result}")
