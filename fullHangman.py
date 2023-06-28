import random


def hangmanGame():
    def hangman7():
        print("__________________")
        print("--------")
        print("|      |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("_")

    def hangman6():
        print("__________________")
        print("--------")
        print("|      O")
        print("|")
        print("|")
        print("|")
        print("|")
        print("_")

    def hangman5():
        print("__________________")
        print("--------")
        print("|      O")
        print("|      |")
        print("|")
        print("|")
        print("|")
        print("_")
    
    def hangman4():
        print("__________________")
        print("--------")
        print("|      O")
        print("|      |")
        print("|      |")
        print("|")
        print("|")
        print("_")
    def hangman3():
        print("__________________")
        print("--------")
        print("|      O")
        print("|     \|")
        print("|      |")
        print("|")
        print("|")
        print("_")

    def hangman2():
        print("__________________")
        print("--------")
        print("|      O")
        print("|     \|/")
        print("|      |")
        print("|")
        print("|")
        print("_")
    def hangman1():
        print("__________________")
        print("--------")
        print("|      O")
        print("|     \|/")
        print("|      |")
        print("|     /")
        print("|")
        print("_")
    def hangman0():        
        print("__________________")
        print("--------")
        print("|      O")
        print("|     \|/")
        print("|      |")
        print("|     / \\")
        print("|")
        print("_")
        
    def draw_picture():
        picture = """
                                                .''.       
       .''.      .        *''*    :_\/_:     . 
      :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-
 :_\/_:'.:::.    ' *''*    * '.\'/.' _\(/_'.':'.'
 : /\ : :::::     *_\/_*     -= o =-  /)\    '  *
  '..'  ':::'     * /\ *     .'/.\'.   '
      *            *..*         :
        *
        *
             """
        print(picture)

  
                                                
    hangmanWordList = [
    "apple",
    "banana",
    "orange",
    "mango",
    "strawberry",
    "watermelon",
    "pineapple",
    "grapefruit",
    "kiwi",
    "peach",
    "pear",
    "plum",
    "blueberry",
    "raspberry",
    "blackberry",
    "avocado",
    "cherry",
    "coconut",
    "lemon",
    "lime",
    "melon",
    "papaya",
    "fig",
    "apricot",
    "guava",
    "passionfruit",
    "cranberry",
    "pomegranate",
    "dragonfruit",
    "starfruit",
    "lychee",
    "persimmon",
    "quince",
    "nectarine",
    "grape",
    "kiwifruit",
    "tangerine",
    "tomato",
    "cantaloupe",
    "honeydew",
    "boysenberry",
    "loganberry",
    "mulberry",
    "olive",
    "date",
    "elderberry",
    "pawpaw",
    "plantain",
    "rhubarb",
    "elephant",
    "giraffe",
    "lion",
    "tiger",
    "zebra",
    "cheetah",
    "rhinoceros",
    "hippopotamus",
    "kangaroo",
    "koala",
    "panda",
    "gorilla",
    "monkey",
    "crocodile",
    "alligator",
    "dolphin",
    "whale",
    "shark",
    "octopus",
    "starfish",
    "seahorse",
    "butterfly",
    "beetle",
    "ladybug",
    "dragonfly",
    "spider",
    "snail",
    "hedgehog",
    "owl",
    "eagle",
    "peacock",
    "parrot",
    "flamingo"
]  
    hangmanWord = random.choice(hangmanWordList)
    linesOfChar = ""
    for char in hangmanWord:
        linesOfChar += "_ "

    triesLeft = 7
    guessedLetters = []

    print(f"Let's play Hangman! Guess the word:{linesOfChar}")
    print(f"Tries left: {triesLeft}")
    hangman7()
    def rightHangman(triesLeft):
        if triesLeft == 0:
            hangman0()
        if triesLeft == 1:
            hangman1()       
        if triesLeft == 2:
            hangman2()
        if triesLeft == 3:
            hangman3()
        if triesLeft == 4:
            hangman4()
        if triesLeft == 5:
            hangman5()
        if triesLeft == 6:
            hangman6()
        if triesLeft == 7:
            hangman7()  
    while triesLeft > 0:
        #Take an input letter and convert it to lowercase
        guessedLetter = input('Guess a letter: ').lower()
  
        if guessedLetter in guessedLetters:
            print("You already guessed that letter!")
            rightHangman(triesLeft)
        elif guessedLetter in hangmanWord:
            print("Good guess!")
            rightHangman(triesLeft)
            guessedLetters.append(guessedLetter)
        else:
            print("Wrong guess!")
            triesLeft -= 1
            rightHangman(triesLeft)
        showWord = ""
        for char in hangmanWord:
            if char in guessedLetters:
                showWord += char + " "
            else:
                showWord += "_ "

        print(showWord)

        if all(char in guessedLetters for char in hangmanWord):
            print("Congratulations! You won!")
           

# Call the function to draw the picture
            draw_picture()
            break

        print("Tries left:", triesLeft)

    else:
        hangman0()
        print("You lost! The word was:", hangmanWord)
    if triesLeft == 1:
        hangman1()
    if triesLeft == 6:
        hangman6()

hangmanGame()

 