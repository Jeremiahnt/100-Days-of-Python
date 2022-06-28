import random
from hangman_art import *
from hangman_words import *

lives = int(6)
end_of_game = False

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
guessed_list = []

#Testing code
print(logo)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
print(f"There are {word_length} letters to guess in this word")

while not end_of_game:
    
    print(f"{' '.join(display)}\n")       
    guess = input("Guess a letter: ").lower()
    
    #Checks guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #Checking if the guess matches any letter
        if letter == guess:
            display[position] = letter                 
                                  
    #Checking if the guessed letter was already guessed
    if guess in guessed_list:
        print(f"You already guessed {guess} you were not penalized for this attempt")
        
    #Checking if the guess is not in the word, if it's in the word -1 to life    
    if guess not in chosen_word:
        if guess not in guessed_list:
            lives -= 1
            guessed_list.append(guess)
    
    #Checks if we are out of lives, if we are out of lives, it prints a game over message, the word and exits the game, the exit is not necessary but I left it in here    
    if lives == 0:
        end_of_game = True
        print("You have run out of attempts and have now lost....")
        print(f"The word was: {chosen_word}\n")
        exit()
        
    #Join all the elements in the list and turn it into a String.
    #print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #prints how many lives you have left and the ASCII art correlating with the # of lives left
    print("\n")
    print("------------------------------------")
    print(f"You have {lives} attempts remaining")
    print("------------------------------------")
    print(stages[lives]) 
    
    