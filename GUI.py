from random import *
from tkinter import *

player_socre = [0]
npc_socre = [0]
rock = ("       ______\n"
        "------'   ____)\n"
        "         (_____)\n"
        "         (_____)\n"
        "         (____)\n"
        "------.__(___)\n")

rock_npc = ("______       \n"
            "(____   '------\n"
            "(_____)         \n"
            "(_____)         \n"
            " (____)         \n"
            "(___)__.------\n")

paper = ("    _______\n"
         "------'   _____)__\n"
         "          _________)\n"
         "          _________)\n"
         "         _________)\n"
         "------._________)")

paper_npc = ("_______    \n"
             "__(_____   '------\n"
             "(_________          \n"
             "(_________          \n"
             "(_________         \n"
             "(_________.------\n")

scissors = ("   _______\n"
            "------'   ______)___\n"
            "                ________)\n"
            "             __________)\n"
            "            (____)\n"
            "------.__(___)\n")

scissors_npc = ("_______   \n"
                "___(______   '------\n"
                "(________                \n"
                "(__________             \n"
                "(____)            \n"
                "(___)__.------\n")


def rockClick(event):
    player_label.configure(text=rock, font=("Arial", 26), fg="firebrick1")
    roll = randint(1, 3)
    if roll == 1:
        npc_label.configure(text=rock_npc, font=("Arial", 26), fg="firebrick1")
        result = Label(window, text="Draw", font=("Arial", 26), fg="blue", anchor=CENTER)
        result.place(x=355, y=300)
    elif roll == 2:
        npc_label.configure(text=paper_npc, font=("Arial", 26), fg="royalblue3")
        result = Label(window, text="Lose ", font=("Arial", 26), fg="red", anchor=CENTER)
        result.place(x=355, y=300)
        npc_socre.append(1)
        npcScore.configure(text=sum(npc_socre))
    elif roll == 3:
        npc_label.configure(text=scissors_npc, font=("Arial", 26), fg="palegreen4")
        result = Label(window, text=" Win ", font=("Arial", 26), fg="green", anchor=CENTER)
        result.place(x=355, y=300)
        player_socre.append(1)
        playerScore.configure(text=sum(player_socre))


def paperClick(event):
    player_label.configure(text=paper, font=("Arial", 26), fg="royalblue3")
    roll = randint(1, 3)
    if roll == 1:
        npc_label.configure(text=rock_npc, font=("Arial", 26), fg="firebrick1")
        result = Label(window, text=" Win ", font=("Arial", 26), fg="green", anchor=CENTER)
        result.place(x=355, y=300)
        player_socre.append(1)
        playerScore.configure(text=sum(player_socre))
    elif roll == 2:
        npc_label.configure(text=paper_npc, font=("Arial", 26), fg="royalblue3")
        result = Label(window, text="Draw", font=("Arial", 26), fg="blue", anchor=CENTER)
        result.place(x=355, y=300)
    elif roll == 3:
        npc_label.configure(text=scissors_npc, font=("Arial", 26), fg="palegreen4")
        result = Label(window, text="Lose ", font=("Arial", 26), fg="red", anchor=CENTER)
        result.place(x=355, y=300)
        npc_socre.append(1)
        npcScore.configure(text=sum(npc_socre))


def scissorsClick(event):
    player_label.configure(text=scissors, font=("Arial", 26), fg="palegreen4")
    roll = randint(1, 3)
    if roll == 1:
        npc_label.configure(text=rock_npc, font=("Arial", 26), fg="firebrick1")
        result = Label(window, text="Lose ", font=("Arial", 26), fg="red", anchor=CENTER)
        result.place(x=355, y=300)
        npc_socre.append(1)
        npcScore.configure(text=sum(npc_socre))
    elif roll == 2:
        npc_label.configure(text=paper_npc, font=("Arial", 26), fg="royalblue3")
        result = Label(window, text=" Win ", font=("Arial", 26), fg="green", anchor=CENTER)
        result.place(x=355, y=300)
        player_socre.append(1)
        playerScore.configure(text=sum(player_socre))
    elif roll == 3:
        npc_label.configure(text=scissors_npc, font=("Arial", 26), fg="palegreen4")
        result = Label(window, text="Draw", font=("Arial", 26), fg="blue", anchor=CENTER)
        result.place(x=355, y=300)


window = Tk()
window.title("MyFirstGame", )
window.geometry('800x500')

game_title = Label(window, text="Rock, Paper, Scissors Game", font=("Arial", 30), fg="dark goldenrod")
game_title.pack()

label = Label(window, text="Welcome", font=("Arial", 20), fg="goldenrod")
label.pack()

button_rock = Button(window, text="Rock", font=("Arial", 22), bg="firebrick1", fg="red4")
button_rock.place(x=10, y=100, width=266, height=50)
button_rock.bind('<Button-1>', rockClick)

button_paper = Button(window, text="Paper", font=("Arial", 22), bg="royalblue3", fg="blue4")
button_paper.place(x=276, y=100, width=266, height=50)
button_paper.bind('<Button-1>', paperClick)

button_scissors = Button(window, text="Scissor", font=("Arial", 22), bg="palegreen3", fg="Green4")
button_scissors.place(x=542, y=100, width=246, height=50)
button_scissors.bind('<Button-1>', scissorsClick)

player_label = Label(window, bg="gray80")
player_label.place(x=10, y=170, width=380, height=310)

npc_label = Label(window, bg="gray80")
npc_label.place(x=410, y=170, width=380, height=310)

player_name = Label(window, text="PLAYER", bg="gray80", font=("Arial", 22), fg="navy")
player_name.place(x=10, y=440)

playerScore = Label(window, text=player_socre, font=("Arial", 22), bg="gray80", fg="navy")
playerScore.place(x=150, y=440)

npcName = Label(window, text="NPC", bg="gray80", font=("Arial", 22), fg="red2")
npcName.place(x=410, y=440)

npcScore = Label(window, text=npc_socre, font=("Arial", 22), bg="gray80", fg="red2")
npcScore.place(x=500, y=440)

window.mainloop()

# BY PRONPHOL TANGADULRAT