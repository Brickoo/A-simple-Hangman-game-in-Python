import random
randomzied_words = [
    "fish",
    "fool",
    "jam",
    "sum",
    "zack",
    "invader",
] ## The array that the words are picked from. can be added onto

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
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
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


randomly_picked = random.choice(randomzied_words) ## picks the random word from the randomized_words table

Total_Tries = 0
Max_Tries = 6

Hint = randomly_picked[0] ## prints the first letter of the word


Reversed_Hint = randomly_picked[::-1] ## reverses the word
last_letter_of_word = Reversed_Hint[0] ## then prints the last letter of the word e.g (hello = olleh == o as the last letter)

print()

World_Length = len(randomly_picked) ## checks the length of the word
wordBlank = ['_ ' for char in range(World_Length)] ## turns the word into underscores
print("".join(wordBlank)) ## the word is printed out in blanks when the game starts e.g _ _ _ _

def Comparing_Asnwers(PlayerInput : str, Picked_Word : str, FillingWord : str ): ## comparing player answer to the picked word and seeing if any words are in the same place
    
    filling_list = list(FillingWord) ## turns the filling into a list

    for index , char in enumerate(Picked_Word): ## loops the picked_word position

        if char.lower() in PlayerInput.lower(): ## if the user entered a word in the correct spot then it appears

            filling_list[index] = char ## turns the fillingword into a letter e.g ( _ _ _ _ == F _ _ _)

    return "".join(filling_list) ## returns the new list and turns it into a string

while True:
    PlayerAnswer = str(input("What is the word?")) ## asks the player what is the word

    if PlayerAnswer == randomly_picked:
        print("Correct Awnser the word was : ", randomly_picked)
        print("Game ended")
        break
    else:
        Total_Tries += 1

        print()
        print(HANGMANPICS[Total_Tries])
        print()
        print("Wrong")
        Comparing = Comparing_Asnwers(PlayerAnswer,randomly_picked,wordBlank) ## This part slowly fills out the blanks to show the word
        print(Comparing)
        print("Tries Left: " , (Max_Tries - Total_Tries))

    if Total_Tries == Max_Tries:
        print("YOU LOST")
        break


