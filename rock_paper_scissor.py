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
human = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors\n"))
if human >= 3 or human <0:
    print("Invalid")
choices = [rock,paper,scissors]
print(choices[human])
computer = random.randint(0,2)
print("Computer chose:\n")
print(choices[computer])

if human == 0 and computer == 2:
    print("You win!")
elif human == 0 and computer == 1:
    print("You lose")
elif human == 1 and computer == 0:
    print("You win!")
elif human == 1 and computer == 2:
    print("You lose")
elif human == 2 and computer == 0:
    print("You lose")
elif human == 2 and computer == 1:
    print("You win!")
else :
    print("It's a draw")