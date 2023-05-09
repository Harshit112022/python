import random
from hangaman_words import word_list
from hangman_art import stages
from hangman_art import logo
chosen_word = random.choice(word_list)

lives = 6
print(logo)
print(f"parse,the solution is {chosen_word}")

display = []
word_length = len(chosen_word)
for _ in chosen_word:
    display += "_"
print(f"have to full Dash of Charector",display)
end_game=True
# print(display)
while end_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        #print(stages[lives])
        if lives == 0:
            end_game=False
            print("You lose.")
            break
    print(display)
    if "_" not in display:
        end_game = False
        print("You win.")
        print(stages[lives])
