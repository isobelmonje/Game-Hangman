#Step 5
#importamos random para poder usar dicha funcion
import random

#importamos clear, de replit para poder usar la función clear y que se limpie la pantalla después de cada elección de letra.
from replit import clear

#importamos la lista de palabras de la hoja hangman_words
from hangman_words import word_list

# El programa seleciona una palabra al azar de la lista  y la almacena en la variable chosen_word. Después con la función len() cuenta las letras de la palabra y las almacena en la variable word lenght().
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Establecemos que el numero de vidas es 6. 
end_of_game = False
lives = 6

# importamos el logo y las fases del ahorcado de la hoja hangman_art
from hangman_art import logo, stages
print(logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
#Mientras que el juego no acabe pide al jugador una letra.Y ejecuta la limpieza de la consola después.
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    if guess in display:
        print(f"You've already guessed {guess}.")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
        
    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that' s not in the word. You lose a life.")
        print()
        #If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #Imprime las vidas que quedan de stages.
    print(stages[lives])