from tkinter import *
from tkinter import messagebox
import math
import sys

root = Tk()
root.title("Tictactoe")

#disable all buttons
def disable_all_buttons():
    b1.confing(state=DISABLED)
    b2.confing(state=DISABLED)
    b3.confing(state=DISABLED)

    b4.confing(state=DISABLED)
    b5.confing(state=DISABLED)
    b6.confing(state=DISABLED)

    b7.confing(state=DISABLED)
    b8.confing(state=DISABLED)
    b9.confing(state=DISABLED)

#Check to see if someone won

def checkifwon():
    global winner
    winner = False

    if b1["text"] == b2["text"] == b3["text"] != " ":
        w = b1["text"]
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", w + " wins")
        disable_all_buttons()
        
    elif b4["text"] == b5["text"] == b6["text"] != " ":
        w = b4["text"]
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", w + " wins")
        disable_all_buttons()
    elif b7["text"] == b8["text"] == b9["text"] != " ":
        w = b7["text"]
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", w + " wins")
        disable_all_buttons()
    elif b1["text"] == b4["text"] == b7["text"] != " ":
        w = b1["text"]
        b7.config(bg="green")
        b4.config(bg="green")
        b1.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", w + " wins")
        disable_all_buttons()
    elif b2["text"] == b5["text"] == b8["text"] != " ":
        w = b2["text"]
        b2.config(bg="green")
        b8.config(bg="green")
        b5.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", w + " wins")
        disable_all_buttons()
    elif b3["text"] == b6["text"] == b9["text"] != " ":
        w = b3["text"]
        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", w + " wins")
        disable_all_buttons()
    elif b1["text"] == b5["text"] == b9["text"] != " ":
        w = b1["text"]
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", w + " wins")
        disable_all_buttons()
    elif b3["text"] == b5["text"] == b7["text"] != " ":
        w = b3["text"]
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", w + " wins")
        disable_all_buttons()
        

def tie():
    messagebox.showinfo("Tic Tac Toe", " Tie :/")
    disable_all_buttons()

    
#score the move

def checkifover_algorithm(b, lvl):
    if lvl >= 8:
        print("it is full")
        
        return 0
    
    elif b[0] == b[1] == b[2] != " ":
        if b[0] == "O":
            return 1
        else:
            return -1
    elif b[3] == b[4] == b[5] != " ":
        if b[3] == "O":
            return 1
        else:
            return -1
    elif b[6] == b[7] == b[8] != " ":
        if b[6] == "X":
            return 1
        else:
            return -1
    elif b[0] == b[3] == b[6] != " ":
        if b[0] == "X":
            return 1
        else:
            return -1
    elif b[1] == b[4] == b[7] != " ":
        if b[0] == "O":
            return 1
        else:
            return -1
    elif b[2] == b[5] == b[8] != " ":
        if b[0] == "O":
            return 1
        else:
            return -1
    elif b[0] == b[4] == b[8] != " ":
        if b[0] == "O":
            return 1
        else:
            return -1
    elif b[2] == b[4] == b[6] != " ":
        if b[0] == "O":
            return 1
        else:
            return -1
    
    return None
    
#Backtracking algorithm 

def score(board, i, turn, lvl): #turn == True: O's turn, False: X's turn

    if turn == True:
        board[i] = "O"
    else:
        board[i] = "X"

        
    if lvl > 10:
        sys.exit(0)
    result = checkifover_algorithm(board, lvl)

    if result != None:
        
        return result
        
    
    s = 0

    for j in range(len(board)-1):
        if board[j] == " " and turn == True:

            s += score(board, j, False, lvl+1)
        if board[j] == " " and turn == False:

            s += score(board, j, True, lvl+1)
        
        else:
            pass

    return s
                

#Computer's turn to make a move

def computer_turn():

    board = []
    board.append(b1["text"])
    board.append(b2["text"])
    board.append(b3["text"])
    board.append(b4["text"])
    board.append(b5["text"])
    board.append(b6["text"])
    board.append(b7["text"])
    board.append(b8["text"])
    board.append(b9["text"])
    
    highest_score = math.inf * (-1)
    best_option = " "
    print("Here we go, board looks like this")
    print(board)
    print("\n\n")
    s = 0
    
    if b1["text"] == " ":
        s = score(board, 0, True, 1)
        if s > highest_score:
            print(s)
            highest_score = s
            best_option = "b1"
    if b2["text"] == " ":
        s = score(board, 1, True, 1)
        if s > highest_score:
            print(s)
            highest_score = s
            best_option = "b2"
        print(highest_score)
    if b3["text"] == " ":
        s = score(board, 2, True, 1)
        if s > highest_score:
            print(s)
            highest_score = s
            best_option = "b3"
            
    if b4["text"] == " ":
        s = score(board, 3, True, 1)
        if s > highest_score:
            print(s)
            highest_score = s
            best_option = "b4"
            
    if b5["text"] == " ":
        s = score(board, 4, True, 1)
        if s > highest_score:
            print(s)
            highest_score = s
            best_option = "b5"
        print(highest_score)
    if b6["text"] == " ":
        s = score(board, 5, True, 1)
        if s > highest_score:
            print(s)
            highest_score = s
            best_option = "b6"
        print(highest_score)
    if b7["text"] == " ":
        s = score(board, 6, True, 1)
        if s > highest_score:
            print(s)
            highest_score = s
            best_option = "b7"
        print(highest_score)
    if b8["text"] == " ":
        s = score(board, 7, True, 1)
        if s > highest_score:
            print(s)
            highest_score = s
            best_option = "b8"
        print(highest_score)
    if b9["text"] == " ":
        s = score(board, 8, True, 1)
        if s > highest_score:
            print(s)
            highest_score = s
            best_option = "b9"
        
    if best_option == "b1":
        b1["text"] = "O"
    elif best_option == "b2":
        b2["text"] = "O"
    elif best_option == "b3":
        b3["text"] = "O"
    elif best_option == "b4":
        b4["text"] = "O"
    elif best_option == "b5":
        b5["text"] = "O"
    elif best_option == "b6":
        b6["text"] = "O"
    elif best_option == "b7":
        b7["text"] = "O"
    elif best_option == "b8":
        b8["text"] = "O"
    elif best_option == "b9":
        b9["text"] = "O"
    else:
        print("error in picking move")
            
#Button clicked function
def b_click(b):
    global clicked, count

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        checkifwon()
        if count >= 9:
            tie()
            
        computer_turn()
        clicked = True
        count += 1
        checkifwon()
        if count >= 9:
            tie()

    else:
        messagebox.showerror("Tic Tac Toe", "This box is already chosen, pick another one")
        

#Buttons
def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked, count
    clicked = True
    count = 0
    b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b1))
    b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b2))
    b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b3))

    b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b4))
    b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b5))
    b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b6))

    b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b7))
    b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b8))
    b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b9))

    #Grid our buttons to the screen

    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)

#Create menu
my_menu = Menu(root)
root.config(menu=my_menu)

#Create options menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset game", command=reset)


reset()
