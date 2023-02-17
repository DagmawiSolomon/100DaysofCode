import random
import game_data
import art

# get a random celeb from the game data file
def random_account():
    random_celeb = random.choice(game_data.data)
    return random_celeb

def get_info(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def check_answer(guess,a_follower,b_follower):
    if a_follower > b_follower:
        return guess == "A"
    if b_follower > a_follower:
        return guess == "B"


def game():
    score = 0
    is_playing = True
    account_a = random_account()
    account_b = random_account()
    while is_playing:
        account_a = account_b
        account_b = random_account()
        while account_a == account_b:
            account_b = get_random_account()
        print(art.logo)
        a = get_info(account_a)
        print("Compare A:",)
        print(art.vs)
        print("Compare B:",get_info(account_b))
        guess = input("Who has more followers? Type 'A' or 'B': ")
        a_follower = account_a["follower_count"]
        b_follower = account_b["follower_count"]
        x = check_answer(guess,a_follower,b_follower)
        if x:
            score += 1
            account_a = guess
            print(account_a)
        else:
            print("lose")
            break
        
        


game()
