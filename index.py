
import random
import hangman_words

chosen_word = random.choice(hangman_words.word_list)
lives = 6
display = []

#print(chosen_word)

for _ in chosen_word: #I could have done it with range, for _ in range (len(chosen_word)
    display += "_"

print(display)

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives = lives - 1
        if lives == 0:
            end_of_game = True
            print("You losstttttt")



    print(display)
    print(lives)

    if "_" not in display:
        end_of_game = True
        print("You wiiiiin")
    
    from hangman_art import stages
    print(stages[lives])