import random


class text:
    yellow = '\033[93m'
    red = '\033[91m'
    darkred = '\033[31m'
    green = '\033[92m'
    cyan = '\033[96m'
    purple = '\033[95m'
    END = '\033[0m'


def game():

    word = "Default"
    wordList = ["hello", "world", "angry", "angle", "words", "water", "melon",
                "apple", "mango", "grade", "teams", "peace", "meant", "write",
                "fight", "beach", "adult", "award", "block", "blood", "wrote",
                "bread", "brain", "break", "chain", "chair", "chief", "meter",
                "child", "draft", "drama", "coast", "cover", "crime", "tweak",
                "final", "floor", "force", "frame", "fault", "field", "while",
                "hotel", "house", "green", "group", "index", "input", "motor",
                "issue", "knife", "judge", "lunch", "limit", "speed", "small",
                "light", "heavy", "match", "metal", "march", "model", "large",
                "money", "month", "night", "music", "north", "noise", "glass",
                "offer", "order", "owner", "plant", "plane", "point", "steel",
                "radio", "range", "round", "score", "scale", "share", "april",
                "sense", "shift", "shock", "shirt", "sleep", "sport", "false",
                "staff", "table", "union", "truth", "trust", "value", "start",
                "video", "whole", "class", "close", "wheat", "print", "break",
                "among", "apply", "upper", "lower", "basic", "first"]

    word = random.choice(wordList)
    wordANS = word
    word = list(word)

    gameWon = False
    guess = 5

    running = True
    while running:

        if gameWon == False:

            attempt = input(text.purple + "Enter a 5 letter word: " + text.END)
            guess -= 1

            if attempt.__len__() != 5 and guess >= 1:
                print(text.darkred + "Please enter a valid word!" + text.END)
                print(text.cyan + "You have " + text.yellow + str(guess) +
                      text.cyan + " guesses remaining" + text.END)
                continue

            if attempt == wordANS:
                gameWon = True
                print(text.green + "You Won!" + text.END)
                print(text.green + "Your guess is correct!" + text.END)

                running = False

            if guess <= 0 and gameWon == False:
                print(text.red + "You Lost!" + text.END)
                print(text.red + "You ran out of guesses!" + text.END)
                print(text.purple + "The word was: " +
                      text.yellow + wordANS + text.END)
                running = False
                break

            output = ""

            for i in range(0, 5):
                if attempt[i] == word[i]:
                    output = output + text.green + attempt[i] + text.END
                elif attempt[i] in word:
                    output = output + text.yellow + attempt[i] + text.END
                elif attempt[i]:
                    output = output + text.red + attempt[i] + text.END

            if gameWon == False:
                print(output)
                print(text.cyan + "You have " + text.yellow +
                      str(guess) + text.cyan + " guesses remaining" + text.END)

    while running == False:
        print(text.purple + "Play Again?" + text.END)
        reply = input(text.purple + "Yes or No?" + text.END)
        reply.lower()

        if reply == "yes":
            running = True
            game()
        elif reply == "no":
            print(text.red + "Byeeee!" + text.END)
            break
        else:
            continue


game()
