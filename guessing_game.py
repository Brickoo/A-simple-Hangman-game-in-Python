import random

randomzied_words = [
    "fish",
    "fool",
    "jam",
    "sum",
    "zack",
    "invader",
]

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


randomly_picked = random.choice(randomzied_words)

Total_Tries = 0
Max_Tries = 6

Hint = randomly_picked[0]


Reversed_Hint = randomly_picked[::-1]
last_letter_of_word = Reversed_Hint[0]

print()

World_Length = len(randomly_picked)
wordBlank = ['_ ' for char in range(World_Length)]
print("".join(wordBlank))

while True:
    PlayerAnswer = str(input("What is the word?"))

    if PlayerAnswer == randomly_picked:
        print("Correct Awnser")
        print("Game ended")
        break
    else:
        Total_Tries += 1

        print()
        print(HANGMANPICS[Total_Tries])
        print()
        print("Wrong")
        print("Tries Left: " , (Max_Tries - Total_Tries))

    if Total_Tries == 3:
        F_Hint = str(input("Do you want a hint? Y for Yes, N for No")).lower()

        if F_Hint == "y":
            print("The world starts with an ", Hint)
        elif F_Hint == "n":
            print("Ok")
        else:
            print("You didnt pick  Y or  N  Final Chance")
            F_Hint = str(input("Do you want a hint? Y for Yes, N for No")).lower()
    
    if Total_Tries == 5:
        F_Hint = str(input("Do you want a hint? Y for Yes, N for No")).lower()

        if F_Hint == "y":
            print("The Word Ends with an ", last_letter_of_word)
        elif F_Hint == "n":
            print("Ok")
        else:
            print("You didnt pick  Y or  N  Final Chance")
            F_Hint = str(input("Do you want a hint? Y for Yes, N for No")).lower()
            
    
    if Total_Tries == Max_Tries:
        print("YOU LOST")
        break
