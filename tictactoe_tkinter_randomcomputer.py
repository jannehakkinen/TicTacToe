from tkinter import *
from tkinter import messagebox
from random import *

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
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", w + " wins")
        disable_all_buttons()
        
    elif b4["text"] == b5["text"] == b6["text"] != " ":
        w = b4["text"]
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", w + " wins")
        disable_all_buttons()
    elif b7["text"] == b8["text"] == b9["text"] != " ":
        w = b7["text"]
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", w + " wins")
        disable_all_buttons()
    elif b1["text"] == b4["text"] == b7["text"] != " ":
        w = b1["text"]
        b7.config(bg="red")
        b4.config(bg="red")
        b1.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", w + " wins")
        disable_all_buttons()
    elif b2["text"] == b5["text"] == b8["text"] != " ":
        w = b2["text"]
        b2.config(bg="red")
        b8.config(bg="red")
        b5.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", w + " wins")
        disable_all_buttons()
    elif b3["text"] == b6["text"] == b9["text"] != " ":
        w = b3["text"]
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", w + " wins")
        disable_all_buttons()
    elif b1["text"] == b5["text"] == b9["text"] != " ":
        w = b1["text"]
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", w + " wins")
        disable_all_buttons()
    elif b3["text"] == b5["text"] == b7["text"] != " ":
        w = b3["text"]
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", w + " wins")
        disable_all_buttons()
        

def tie():
    messagebox.showinfo("Tic Tac Toe", " Tie :/")
    disable_all_buttons()

#Computer's turn to make a move

def computer_turn():
    while True:
        move = randint(1, 9)
        if move == 1:
            if b1["text"]== " ":
                b1["text"] = "O"
                break
            else:
                continue
        elif move == 2:
            if b2["text"]== " ":
                b2["text"] = "O"
                break
            else:
                continue
        elif move == 3:
            if b3["text"]== " ":
                b3["text"] = "O"
                break
            else:
                continue
        elif move == 4:
            if b4["text"]== " ":
                b4["text"] = "O"
                break
            else:
                continue
        elif move == 5:
            if b5["text"]== " ":
                b5["text"] = "O"
                break
            else:
                continue
        elif move == 6:
            if b6["text"]== " ":
                b6["text"] = "O"
                break
            else:
                continue
        elif move == 7:
            if b7["text"]== " ":
                b7["text"] = "O"
                break
            else:
                continue
        elif move == 8:
            if b8["text"]== " ":
                b8["text"] = "O"
                break
            else:
                continue
        elif move == 9:
            if b9["text"]== " ":
                b9["text"] = "O"
                break
            else:
                continue
        else:
            messagebox.showerror("Tic Tac Toe", "Error with computer randint")
            
            
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
