from tkinter import *
from PIL import Image,ImageTk
from random import randint

#main window
root = Tk()
root.title("Rock Paper Scissors")
root.configure(background="azure2")
root.geometry("1200x500")


#picture read
rock_img = ImageTk.PhotoImage(Image.open("rock-user.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper-user.png"))
scissors_img = ImageTk.PhotoImage(Image.open("scissors-user.jpg"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper.png"))
scissors_img_comp = ImageTk.PhotoImage(Image.open("scissors.jpg"))

'''# Background image
background_image = Image.open("bg2.png")
background_photo = ImageTk.PhotoImage(background_image)
background_label = Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)'''



#insert picture
user_label = Label(root,image=scissors_img,bg="azure2")
comp_label = Label(root,image=scissors_img,bg="azure2")
comp_label.grid(row=1,column=0)
user_label.grid(row=1,column=4)


#scores
playerScore = Label(root,text=0,font=100,bg="azure2",fg="black")
computerScore = Label(root,text=0,font=100,bg="azure2",fg="black")
computerScore.grid(row=1,column=1)
playerScore.grid(row=1,column=3)

#indicators
user_indicator = Label(root,font=50,text="USER",bg="azure2",fg="black")
comp_indicator = Label(root,font=50,text="COMPUTER",bg="azure2",fg="black")
user_indicator.grid(row=0,column=3)
comp_indicator.grid(row=0,column=1)
button_indicator = Label(root,font=70,text="Press your choice:",bg="azure2",fg="black")
button_indicator.grid(row=2,column=2)
space_indicator = Label(root,font=70,text="",bg="azure2",fg="black")
space_indicator.grid(row=4,column=2)


#messages
msg = Label(root,font=50,bg="azure2",fg="black",text="YOU LOOSE")
msg.grid(row=5,column=2)

#update message
def updateMessage(x):
    msg['text']= x

#update user score
def updateUserScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score) 

def updateCompScore():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)       

#check winner
def CheckWin(player,computer):
    if player == computer:
        updateMessage("Its a tie!!!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win") 
            updateUserScore()
    elif player == "paper":
        if computer == "scissors":
            updateMessage("You loose") 
            updateCompScore()
        else:
            updateMessage("You Win") 
            updateUserScore()   
    elif player == "scissors":
        if computer == "rock":
            updateMessage("You loose") 
            updateCompScore()
        else:
            updateMessage("You Win") 
            updateUserScore()  
    else:
        pass
                 


#update choices

choices = ["rock","paper","scissors"]
def updateChoice(x):

    #for computer
    compChoice = choices[randint(0,2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissors_img_comp)

    # for user    
    if x=="rock":
        user_label.configure(image=rock_img)
    elif x=="paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissors_img)  

    CheckWin(x,compChoice)      

#buttons
rock = Button(root,width=20,height=2,text="ROCK",bg="gray53",fg="white",command = lambda:updateChoice("rock")).grid(row=3,column=1)
paper = Button(root,width=20,height=2,text="PAPER",bg="gray53",fg="white",command = lambda:updateChoice("paper")).grid(row=3,column=2)
scissors = Button(root,width=20,height=2,text="SCISSORS",bg="gray53",fg="white",command = lambda:updateChoice("scissors")).grid(row=3,column=3)




# Execute tkinter
root.mainloop()

