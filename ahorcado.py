import random

print("          _    _  ____  _____   _____          _____   ____  ")
print("    /\   | |  | |/ __ \|  __ \ / ____|   /\   |  __ \ / __ \ ")
print("   /  \  | |__| | |  | | |__) | |       /  \  | |  | | |  | |")
print("  / /\ \ |  __  | |  | |  _  /| |      / /\ \ | |  | | |  | |")
print(" / ____ \| |  | | |__| | | \ \| |____ / ____ \| |__| | |__| |")
print("/_/    \_\_|  |_|\____/|_|  \_\ _____/_/    \_\_____/ \____/ ")
print(" ")
print("                                               Por David Lopez")
print("==============================================================")
print("\n")

def get_word():
    word = random.choice(open("words.txt").readline().split())
    return word.upper()    

def display_hangman(tries):
    stages = [
                """
                   _________
                   |      |
                   |    __0__
                   |      |
                   |     / \ 
                   |     
                """,
                """
                   _________
                   |      |
                   |    __o__
                   |      |
                   |     / 
                   |     
                """,
                """
                   _________
                   |      |
                   |    __o__
                   |      |
                   |     
                   | 
                """,
                """
                    _________
                   |      |
                   |    __o
                   |      |
                   |     
                   |
                """,
                """
                   _________
                   |      |
                   |      o
                   |      |
                   |     
                   |
                """,
                """
                   _________
                   |      |
                   |      o
                   |      
                   |     
                   |
                """,
                """
                   _________
                   |      |
                   |      
                   |      
                   |     
                   |
                """
    ]
    return stages[tries]


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print(f"TU PALABRA TIENE \033[4m\033[1m{len(word)}\033[0m LETRAS")
    print(" ")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    
    while not guessed and tries > 0:
        guess = input("Ingresa una letra o palabra : ").upper()

        # GUESSING FOR A LETTER
        if len(guess) == 1 and guess.isalpha(): # Checks if it is only one character and isalpha() checks if the guess only contains letters
            if guess in guessed_letters: # If the letter has already been tried
                print(f"\033[93mYa habías intentado con {guess}\033[0m")

            elif guess not in word: # If the letter is not in the word
                print("\n")
                print(f"\033[1m\033[91m{guess} no está en la palabra ❌\033[0m")
                tries -= 1
                print("\033[1m\033[95mVidas restantes:\033[0m", tries*"❤️")
                print("\n")

                guessed_letters.append(guess) # Add the letter to the array of used letters

            else: # If the guess is correct
                print(f"\033[1m\033[92mBuen trabajo! {guess} sí está en la palabra 😄\033[0m")
                guessed_letters.append(guess) # Add the letter to the array of used letters

                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion: # If there are no more spaces left, then the word is completed
                    guessed = True


        # GUESSING THE WHOLE WORD
        elif len(guess) == len(word) and guess.isalpha(): # Checks if it is only one character and isalpha() checks if the guess only contains letters
            if guess in guessed_words: # If the word has already been tried
                print(f"\033[93mYa habías intentado con {guess}\033[0m")

            elif guess != word: # If the guessed word does not match with the word
                print(f"\033[1m\033[91m{guess} no está en la palabra ❌\033[0m")
                tries -= 1
                print("\033[1m\033[95mVidas restantes:\033[0m", tries*"❤️")
                guessed_words.append(guess) # Add the word to the array of used words

            else: # If the guess is correct
                guessed = True
                word_completion = word


        # INVALID GUESS
        else:
            print("\033[93mRespuesta no válida, intenta otra vez\033[0m")


        print(display_hangman(tries))
        print(word_completion)
        print("\n")

    # CHECK IF THE USER WON OR LOST    
    if guessed:
        print("\033[1m\033[102m  🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉  \033[0m")
        print("\033[1m\033[92m FELICITACIONES! Adivinaste la palabra      \033[0m")
        print("\033[1m\033[102m  🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉  \033[0m")
    else:
        print(f"\033[101m  Lo siento, se acabaron tus intentos, la palabra era \033[1m{word} \033[0m")



def main():
    word = get_word()
    play(word)
    while input("Quieres jugar otra vez? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)

main()