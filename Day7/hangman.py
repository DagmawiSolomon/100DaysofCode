import random
import hangman_words
import  hangman_art
playing = True
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives = 6
display = []
print(hangman_art.logo)
for _ in range(word_length):
    display += ("_")
while playing:
    guess = input("Guess a letter: ").lower()
    for i in range(word_length):
        letter = chosen_word[i]
        if letter == guess:
            display[i] = letter
    if guess not in chosen_word:
        print(stages[lives])
        lives -= 1
        if lives <= 0:
            playing = False
            print(f"YOU LOSE, the word was {chosen_word}")

    print(display)
    if "_" not in display:
        playing = False
        print("YOU WIN 🏆")

    print(hangman_art.stages[lives])


