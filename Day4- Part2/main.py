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

def print_board(board, marked_board):
    print("----------------------------------------")
    for i in range(len(board)):
        print(f"{board[i]} | {marked_board[i]}")
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
boards_to_check=[]
for i in range(len(lines)):
    if i==0:
        numbers=[int(number_s) for number_s in lines[0].split(",")]
    elif len(lines[i])==0:
        boards.append([])
        checked_boards.append([])
        boards_to_check.append(len(boards_to_check))
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
for number in numbers:
    print(f"----------------------------------------------------------Starting number{number}------------------------------------------")
    i=0
    if not found:
        for board_index in boards_to_check:
            board=boards[board_index]
            if number==13:
                print(f"Jordi{board[1]}")
            position = check_board_number(board,number)
            if position != [-1,-1]:
                checked_boards[board_index][position[0]][position[1]]="X"
                print(f"Jordi{checked_boards[board_index][1]}")
            i+=1

        boards_to_remove=[]
        for board_index in boards_to_check:
            sum_unmarked_numbers=0
            print(f"Validating board {board_index} - Number {number}" )
            if number==13:
                print(f"line")
                print()
                print()
            validation = validate_board(boards[board_index],checked_boards[board_index])
            print_board(boards[board_index], checked_boards[board_index])
            print(f"{validation}")
            if validation:
                for k in range(len(validation)):
                    sum_unmarked_numbers+=validation[k]
                print(f"Board {board_index} is a winner. Removed from list")
                boards_to_remove.append(board_index)
                # print(validation)
                print(len(boards_to_check))

        for board_index in boards_to_remove:
            boards_to_check.remove(board_index)
        if len(boards_to_check)==0:
            found=True
        last_number=number
    print(f"----------------------------------------------------------Ending number{number}------------------------------------------")
print(f"***{found}")
# print(validation)
# for number in validation:
#     result+=number

print(f"last number: {last_number}")
print(f"Sum unmarked numbers {sum_unmarked_numbers}")
print(f"Final result: {sum_unmarked_numbers*last_number}")
