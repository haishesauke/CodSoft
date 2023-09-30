import tkinter as  tk
import random

# function that contains the logic for determining the winner
def winner(user_choice, computer_choice):
    if user_choice == computer_choice :
        return "It's a tie !!!"
    
    elif (user_choice == "rock" and computer_choice == "scissors") or \
        (user_choice == "scissors" and computer_choice == "paper") or \
        (user_choice == "paper" and computer_choice == "rock") :
        return "You win ◦'⌣'◦"
    
    else :
        return "You lost ⌣̩̩́_⌣̩̩̀"


# function for game output
def game_output(user_choice):
    choice = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choice)

    result = winner(user_choice, computer_choice)

    user_label.config(text = f"Your Choice : { user_choice}", fg ="blue")
    computer_label.config(text = f"Computer Choice : { computer_choice}", fg ="blue")
    result_label.config(text = result, fg = "green")


# creating the main frame
root = tk.Tk()
root.title("Let's Play Rock! Paper! Scissors!")
instruction_label = tk.Label(root, text = "Choose from Rock, papper or scissors :", font =("Times", 14))
instruction_label.pack()

rock_button = tk.Button(root, text = "Rock" , command= lambda: game_output("rock"), font =("Times", 12))
rock_button.pack()

paper_button = tk.Button(root, text= "Paper", command= lambda : game_output("paper"), font =("Times", 12))
paper_button.pack()

scissors_button = tk.Button(root, text= "scissors", command= lambda : game_output("scissors"), font =("Times", 12))
scissors_button.pack()

user_label = tk.Label(root, text="", font =("Helvetica", 12))
user_label.pack()

computer_label = tk.Label(root, text="", font =("Helvetica", 12))
computer_label.pack()

result_label = tk.Label(root, text="", font =("Helvetica", 16))
result_label.pack()
root.mainloop()