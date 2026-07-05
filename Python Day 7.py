# Hangman Project
# We will use for loop,while loop,if else,lists,strings,range,modules
import random
from hangman_words_day7 import words
random_word=random.choice(words)
print(random_word)
from hangman_art_day7 import logo
print(logo)
lives=6
display=[]
for letters in random_word:
    display+="_"
print(display)
end_of_game=False
while not end_of_game:
    guess=input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")
    for position in range(len(random_word)):
        letter=random_word[position]
        if letter==guess:
            display[position]=letter
    print(display)
    if guess not in random_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives-=1
        from hangman_art_day7 import stages
        print(stages[lives])
        if lives==0:
            end_of_game = True
            print("You lose")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game=True
        print("You win")


    
    



