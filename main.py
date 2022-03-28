import random


class text:
    yellow = '\033[93m'
    red = '\033[91m'
    darkred = '\033[31m'
    green = '\033[92m'
    cyan = '\033[96m'
    purple = '\033[95m'
    END = '\033[0m'


def chooseDifficulty():
    global GameDifficulty

    print(text.purple + "Choose the difficulty." + text.END)
    print(text.purple + "B or Beginner / I or Intermediate / E or Expert" + text.END)
    difficultyInput = input(
        text.yellow + "Type the correct spelling/number too! " + text.END)
    if difficultyInput.isalpha():
        difficultyInput = difficultyInput.lower()

        if difficultyInput == "beginner" or difficultyInput == "b":
            GameDifficulty = "beginner"
        elif difficultyInput == "intermediate" or difficultyInput == "i":
            GameDifficulty = "intermediate"
        elif difficultyInput == "expert" or difficultyInput == "e":
            GameDifficulty = "expert"
        else:
            print(text.darkred + "Please enter a valid choice!" + text.END)
            chooseDifficulty()

    else:
        print(text.darkred + "Please enter a valid choice!" + text.END)
        chooseDifficulty()


def game():
    word = "Default"

    if GameDifficulty == "beginner":
        wordListBeginner = ["word", "test", "bowl", "also", "able", "blue", "bomb",
                            "belt", "bank", "bone", "camp", "case", "cell", "cash",
                            "card", "tent", "city", "came", "cast", "crop", "dark",
                            "deny", "deal", "desk", "done", "drop", "duty", "dual",
                            "draw", "earn", "ever", "fair", "evil", "feed", "farm",
                            "fail", "five", "fire", "food", "flow", "flat", "fund",
                            "gate", "gain", "gave", "grow", "hall", "harm", "hard",
                            "hill", "here", "keep", "king", "know", "lane", "loan",
                            "mass", "make", "male", "most", "make", "more", "moon",
                            "navy", "need", "name", "nice", "else", "game", "list",
                            "text", "page", "paid", "pain", "pack", "past", "park",
                            "pass", "part", "plot", "pipe", "pick", "pure", "port",
                            "rent", "roof", "rush", "said", "sake", "sail", "seed",
                            "seed", "save", "seek", "show", "ship", "tour", "unit",
                            "vote", "very", "walk", "wish", "year", "zone", "zero"]
        word = random.choice(wordListBeginner)
        wordANS = word
        word = list(word)
        print(text.purple + "You have to guess a " + text.yellow +
              "4" + text.purple + " letter word" + text.END)

    elif GameDifficulty == "intermediate":

        wordListIntermediate = ["hello", "world", "angry", "angle", "words", "water", "melon",
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

        word = random.choice(wordListIntermediate)
        wordANS = word
        word = list(word)
        print(text.purple + "You have to guess a " + text.yellow +
              "5" + text.purple + " letter word" + text.END)

    elif GameDifficulty == "expert":
        wordListExpert = ["expert", "anyone", "answer", "appeal", "afford", "arrive", "attack", "almost",
                          "purple", "annual", "battle", "behind", "belive", "belief", "bright", "belong",
                          "yellow", "broken", "breath", "button", "camers", "circle", "client", "closed",
                          "orange", "danger", "coffee", "dealer", "custom", "debate", "defeat", "desire",
                          "choice", "detail", "dinner", "doctor", "during", "eating", "eaisly", "ensure",
                          "random", "eidtor", "except", "escape", "export", "expand", "flight", "forced",
                          "golden", "ground", "global", "health", "hidden", "impact", "honest", "injury",
                          "junior", "latest", "lawyer", "losing", "making", "mainly", "luxury", "manage",
                          "mature", "mental", "medium", "mostly", "mutual", "mostly", "palace", "planet",
                          "person", "permit", "patent", "player", "police", "prefer", "pocket", "please",
                          "proper", "proven", "raised", "public", "random", "rather", "region", "regard",
                          "remote", "remove", "result", "resort", "sample", "salary", "source", "simply",
                          "stable", "sprint", "summit", "sudden", "system", "talent", "target", "though"]

        word = random.choice(wordListExpert)
        wordANS = word
        word = list(word)
        print(text.purple + "You have to guess a " + text.yellow +
              "6" + text.purple + " letter word" + text.END)
    else:
        print(text.red + "If you are reading this then a error has occured, somehow the difficulty check has failed.")

    gameWon = False
    guess = 5

    running = True
    while running:

        if gameWon == False:

            attempt = input(text.purple + "Enter your guess: " + text.END)
            guess -= 1

            if attempt.__len__() != 5 and guess >= 1 and GameDifficulty == "intermediate":
                print(text.darkred + "Please enter a valid word!" + text.END)
                print(text.cyan + "You have " + text.yellow + str(guess) +
                      text.cyan + " guesses remaining" + text.END)
                continue
            elif attempt.__len__() != 4 and guess >= 1 and GameDifficulty == "beginner":
                print(text.darkred + "Please enter a valid word!" + text.END)
                print(text.cyan + "You have " + text.yellow + str(guess) +
                      text.cyan + " guesses remaining" + text.END)
                continue

            elif attempt.__len__() != 6 and guess >= 1 and GameDifficulty == "expert":
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

            if GameDifficulty == "intermediate":
                for i in range(0, 5):
                    if attempt[i] == word[i]:
                        output = output + text.green + attempt[i] + text.END
                    elif attempt[i] in word:
                        output = output + text.yellow + attempt[i] + text.END
                    elif attempt[i]:
                        output = output + text.red + attempt[i] + text.END

            if GameDifficulty == "beginner":
                for i in range(0, 4):
                    if attempt[i] == word[i]:
                        output = output + text.green + attempt[i] + text.END
                    elif attempt[i] in word:
                        output = output + text.yellow + attempt[i] + text.END
                    elif attempt[i]:
                        output = output + text.red + attempt[i] + text.END

            if GameDifficulty == "expert":
                for i in range(0, 6):
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

        if reply == "yes" or reply == "y":
            running = True
            chooseDifficulty()
            game()
        elif reply == "no" or reply == "n":
            print(text.red + "Byeeee!" + text.END)
            break
        else:
            continue


chooseDifficulty()
print(text.purple + "You selected the " + text.yellow +
      GameDifficulty + text.purple + " difficulty" + text.END)
game()
