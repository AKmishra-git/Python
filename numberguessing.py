import random

l_bound = 1
h_bound = 100
answer = random.randint(l_bound, h_bound)
guess = 0
is_online = True

print("**WELCOME TO NUMBER GUESSING GAME**")
print(f"Choose the number between {l_bound} and {h_bound}: ")

while is_online:

    choice = int(input("Enter your choice: "))



    if choice < l_bound or choice > h_bound:
        print("Invalid choice")
        print("Kindly Select the number between {l_bound} and {h_bound}")

    elif choice < answer:
        print("TOO LOW")
        

    elif choice>answer:
        print("TOO HIGH")

    else:
        print("CORRECT GUESS")
        print(f"****The answer is {choice}****")


        is_online = False