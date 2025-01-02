#ROCK PAPER SCISSOR GAME IN PYTHON ##
import random
def rock_paper_scissor():
    choices=("rock","paper","scissor")
    print("welocme to game ")
    while True:
        user=input("Enter any of this from : or quit").lower()
        if user==quit:
            print("Thank you for coming")
            break
        if user not in choices:
            print("Invalid plz enter other")
            continue

        computer_choice=random.choice(choices)
        print(f'computer choose {computer_choice}')

        if user==computer_choice:
            print("Its tie ")
        elif (user=="rock" and computer_choice=="scissor") or \
                (user == "paper" and computer_choice == "rock") or \
                (user == "scissor" and computer_choice == "paper"):
            print("You win!!!!")
        else:
            print("You lose")

if __name__=='__main__':
    rock_paper_scissor()