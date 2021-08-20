import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rps = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice < 3 and user_choice >= 0:
    print(rps[user_choice])

    comp_choice = random.randint(0,2)
    print(f"Computer chose: {rps[comp_choice]}")


    if user_choice == comp_choice:
        print("Match Tied")
    elif (user_choice == 0 and comp_choice == 2) or (user_choice == 2 and comp_choice == 1) or (user_choice == 1 and comp_choice == 0):
        print("You win")
    else:
        print("You lose")
else:
    print("Wrong input")
