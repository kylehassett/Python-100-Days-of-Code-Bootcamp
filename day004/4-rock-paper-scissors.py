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

#Write your code below this line 👇
options = [rock, paper, scissors]

print("Welcome to rock, paper, scissors!")
print("Please select your weapon of choice.")

player_choice = int(input("1 = rock, 2 = paper, and 3 = scissors: ")) - 1
computer_choice = random.randint(0, 2)


choice_message = "You chose "
if player_choice == 0:
    choice_message += "rock"
elif player_choice == 1:
    choice_message += "paper"
else:
    choice_message += "scissors"

print(choice_message)
print()
print(options[player_choice])
print()

computer_choice_message = "The computer chose "
if computer_choice == 0:
    computer_choice_message += "rock"
elif computer_choice == 1:
    computer_choice_message += "paper"
else:
    computer_choice_message += "scissors"

print(computer_choice_message)
print()
print(options[computer_choice])
print()

result = "You "

if player_choice == 0:
    if computer_choice == 0:
        result += "tied :-/"
    elif computer_choice == 1:
        result += "lost :-("
    else:
        result += "won :-)"
elif player_choice == 1:
    if computer_choice == 0:
        result += "won :-)"
    elif computer_choice == 1:
        result += "tied :-/"
    else:
        result += "lost :-("
else:
    if computer_choice == 0:
        result += "lost :-("
    elif computer_choice == 1:
        result += "won :-)"
    else:
        result += "tied :-/"

print(result)
