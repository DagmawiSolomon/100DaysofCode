import random
name = input("Enter names")
print(name.split(", "))
is_on = True
players = []
while is_on:
    player = input("Enter name: ")
    print("Type 'run' when your done entering names")
    if player == "run":
        is_on = False
    else:
        players.append(player)
random_number = random.randint(0, len(players)-1)
print(f"{players[random_number]} will pay the bill!")




