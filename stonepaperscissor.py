import random

option = ("Stone", "Paper", "Scissor")
Player = None
is_online = True

while is_online:
    Player = None
    device = random.choice(option)

    while Player not in option:
        Player = input("Enter your choice: ")


    print(f"Your choice: {Player}")
    print(f"device choice: {device}")

    if Player == device:
        print("It's a Draw")

    elif Player=="Stone " and device == "Scissor":
        print("***You Won***")

    elif Player == "Paper" and device=="Stone":
        print("***You Won***")

    elif Player == "Scissor" and device == "Paper":
        print("***You Won***")

    else:
        print("***DEVICE WON***")

    play = input("Do you want to play again(Y/N): ")

    if not play == "Y":
        is_online= False

print("***THANKS FOR PLAYING***")




