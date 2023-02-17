import random
random_integer = random.randint(1,3)
print(random_integer)
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
prompt = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors: "))
game_images = [rock, paper, scissors]
print(game_images[prompt-1])
print(game_images[random_integer-1])

if random_integer >=3 or prompt >= 3:
    print("Invalid input")
elif prompt == 0 and random_integer == 2:
    print("You win!")
elif prompt == 2 and random_integer == 0:
    print("Computer wins!")
elif prompt > random_integer:
    print("You win! ")
elif random_integer > prompt:
    print("Computer wins!")
elif random_integer == prompt:
    print("It's a draw")