print("Welcome to the Treasure Island. Your mission is to find the treasure.")

choice1 = input("Which side are you choosing, Left or Right? ").lower()

if choice1 == "left":
    choice2 = input("You are standing on an island. Do you want to wait or swim? ").lower()
    if choice2 == "wait":
        choice3 = input("You are standing in front of three doors. Which door are you choosing: Blue, Red, or Yellow? ").lower()
        if choice3 == "red":
            print("You got burned by the fire. Game Over.")
        elif choice3 == "blue":
            print("You got eaten by beasts. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! Congratulations, you win!")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by trouts. Game Over.")
else:
    print("You fell into a hole. Game Over.")
