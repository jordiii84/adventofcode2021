def check_board_number(board,element):
    for i in range(len(board)):
        try:
            index=board[i].index(element)
            return [i,index]
        except:
            pass

    return[-1,-1]
def get_unmarked_numbers(board,marked_board):
    unmarked_numbers=[]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if marked_board[i][j]=="O":
                unmarked_numbers.append(board[i][j])
    return unmarked_numbers

def validate_board(board,marked_board):
    for i in range(len(marked_board)):
        try:
            marked_board[i].index("O")
        except:
            return get_unmarked_numbers(board,marked_board)
    for i in range(len(marked_board[0])):
        column=[row[i] for row in marked_board]
        try:
            column.index("O")
        except:
            return get_unmarked_numbers(board,marked_board)

    return None

def print_board(board):
    print("----------------------------------------")
    for line in board:
        print(line)
    print("----------------------------------------")


f = open("input.txt", "r")
lines = f.readlines()
clean_lines=[]

for line in lines:
    clean_lines.append(line[:-1])
lines=clean_lines


boards=[]
checked_boards=[]
num_board=-1
for i in range(len(lines)):
    if i==0:
        numbers=[int(number_s) for number_s in lines[0].split(",")]
    elif len(lines[i])==0:
        boards.append([])
        checked_boards.append([])
        num_board+=1
    else:
        line=lines[i].split(" ")
        line_int=[]
        empty_line=[]
        for element in line:
            try:
                line_int.append(int(element))
                empty_line.append("O")
            except:
                pass
        boards[num_board].append(line_int)
        checked_boards[num_board].append(empty_line)

found=False
last_number=-1
sum_unmarked_numbers=0
for number in numbers:
    i=0
    if not found:
        for board in boards:
            position = check_board_number(board,number)
            # print(f" Board {board} - number {number} - position {position}")
            if position != [-1,-1]:
                checked_boards[i][position[0]][position[1]]="X"
            # print(checked_boards[i])
            i+=1


        for i in range(len(checked_boards)):
            validation = validate_board(boards[i],checked_boards[i])
            if validation:
                for i in range(len(validation)):
                    sum_unmarked_numbers+=validation[i]
                print(validation)
                found=True
        last_number=number

result=0
print(validation)
# for number in validation:
#     result+=number

print(f"last number: {last_number}")
print(f"Sum unmarked numbers {sum_unmarked_numbers}")
print(f"Final result: {sum_unmarked_numbers*last_number}")
