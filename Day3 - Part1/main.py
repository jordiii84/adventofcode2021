def hex_to_dec(hex):
    dec=0
    for x in range(len(hex)):
        dec+=2**(len(hex)-x-1)*hex[x]
    return dec


f = open("input.txt", "r")
lines = f.readlines()

gamma=[]
epsilon=[]
for i in range(len(lines[0])-1):
    sum_column=0
    for j in range(len(lines)):
        sum_column+=int(lines[j][i])
    if sum_column>len(lines)/2:
        gamma.append(1)
        epsilon.append(0)
    else:
        gamma.append(0)
        epsilon.append(1)

gamma_dec=hex_to_dec(gamma)
epsilon_dec=hex_to_dec(epsilon)


print(f"gamma->{gamma}  epsilon->{epsilon}")
print(f"gamma_dec->{gamma_dec}  epsilon_dec->{epsilon_dec}")
print(f"Power consuption = {gamma_dec*epsilon_dec}")