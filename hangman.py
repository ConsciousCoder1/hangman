import random
import logo

print("\nWelcome to PyHangman!\n")
logo.logoprint()

# --------Selecting game category 

lives_left = 6

game_category = int(input("\nPlease select a game category. Type 1 for Space, 2 for Disney, or 3 for Star Wars: \n"))

game_word = ''

import game_words

if game_category == 1:
    game_word += random.choice(game_words.space)
elif game_category == 2:
    game_word += random.choice(game_words.disney)
else:
    game_word += random.choice(game_words.starwars)

# -------- Producing layout for game word

game_word_length = len(game_word)

letter_display = []

for i in game_word:
    if i == ' ':
        letter_display += ' '
    else:
        letter_display += '_'
print(' '.join(letter_display))

# -------- Gameplay: requesting user input
game_end = False
while not game_end:
    print("\nEnter a letter:\n")
    user_letter = str(input("\n>  ").lower())
    print(f"\nYou chose: {user_letter}\n")
    
    if user_letter in letter_display:
        print("\nYou've already guessed this letter!\n")
    
    for ind in range(game_word_length):
        letter = game_word[ind]
        if letter == user_letter:
            letter_display[ind] = letter
            
    if user_letter not in game_word:
        lives_left -= 1
        if lives_left == 0:
            game_end = True
            print("PyMan is no more. You Lose")
            
    print(' '.join(letter_display))
    print('\n---------------------\n')
  
    if '_' not in letter_display:
        game_end = True
        print("You're a Winner!")
        

    import hangman_art        
    print(hangman_art.hangmen[lives_left])

            
            
