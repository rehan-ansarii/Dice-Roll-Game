import random

user_score  = 0
computer_score = 0

while user_score < 5 and computer_score < 5:
    input("Press enter to roll the dice")

    user = random.randint(1, 6)
    computer = random.randint(1, 6)

    print("You Roll:",user)
    print("Computere Roll:",computer)

    if user > computer:
        user_score += 1
        print("You Win.")

    elif computer > user:
        computer_score += 1
        print("Computer Win.")

    else:
        print("Draw.")

    print(f"Score -- You: {user_score}\t Compter: {computer_score}\n")
    
if user_score == 5:
    print("Congratulation You win this Round.")

else:
    print("Computer Win this Round.")