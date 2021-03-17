# AI - MASTERMIND
# NAAM: Justin Klein - 1707815
# KLAS: V1B (Projectgroep 1)

# NL: Print statements zijn in het Nederlands, verder is de code in het Engels.
# ENG: Print statements are in Dutch, the remaining code is in English.

import random
import itertools

# ------------------------------------------------------------------------------------------- #
# ---------------------------- Functions (Machine generates the code) ----------------------- #
def generateCode(colorlist, length):
    """
    Creates the code that the player needs to guess.
    @param colorlist: list
    @param length: integer
    @return: list
    """
    generated = []
    for i in range(0,length):
        j = random.choice(colorlist)
        generated.append(j[0])

    return generated


def canBeChecked(generated_code,user_input,colorlist):
    """
    Looks at the user input and determines if the right characters
    are used and if the lists are the same length.
    @param generated_code: list
    @param user_input: list
    @param colorlist: list
    @return: boolean / void
    """
    if len(user_input) > len(generated_code) or len(user_input) < len(generated_code):
        return False
    else:
        for i in user_input:
            if i not in colorlist:
                return False


def checkanswer(generated_code,user_inputlist,colorlist):
    """
    Calculates the black and white pins for the given answer and
    returns values based on if it is correct or not.
    @param generated_code: list
    @param user_inputlist: list
    @param colorlist: list
    @return: boolean / list
    """
    # ------ Checks if code can be checked ------ #
    if canBeChecked(generated_code,user_inputlist,colorlist) == False:
        return False

    # ------ Checks the actual code and calculates pins ------ #
    checklist = user_inputlist.copy()
    blackPin = 0
    whitePin = 0
    pos = 0
    result = []

    for i in user_inputlist:
        if i == generated_code[pos]:
            result.append(i[0])
            blackPin += 1
        else:
            result.append("?")
        pos += 1

    for i in generated_code:
        if i in checklist:
            checklist.remove(i)
            whitePin += 1

    whitePin -= blackPin
    return [result,blackPin,whitePin]


def playgame_VersusAI(colors, length_code):
    """
    This function runs the game where the AI generates the code
    and the player needs to guess.
    @param colors: list
    @param length_code: integer
    """
    generated_code = generateCode(colors,length_code)
    print(f"\nWelkom bij Mastermind!\n"
          f"Raad de code door de voorletters te gebruiken van kleuren. (bijvoorbeeld: RGBZ)\n"
          f"De code bestaat uit {length_code} kleuren die ieder: {colors} kunnen zijn.\n"
          f"Let op: Je hebt maar 8 kansen!\n"
          f"De computer heeft een code gegenereerd! Veel succes!")

    colorlist = []
    for i in colors:
        colorlist.append(i[0])

    gamelength = 0
    while True:
        user_input = input("\nWat denk je dat de code is?: ")
        user_inputlist = []
        for i in user_input:
            user_inputlist.append(i.upper())

        uitkomst = checkanswer(generated_code,user_inputlist,colorlist)
        if uitkomst == False:
            print(f"Deze code is niet valide. Bekijk de lengte of de ingevulde kleuren en probeer het opnieuw!\n")
        else:
            if uitkomst[0] != generated_code and gamelength > 6:
                print("\nHelaas! Je hebt al je beurten verspild. De computer heeft gewonnen!")
                print(f"\nHet antwoord was: {generated_code}")
                break
            # ---------- Shows result (Blackpin, Whitepin) ---------- #
            print(f"- Je hebt er {uitkomst[1]} op de juiste plaats.\n"
                  f"- {uitkomst[2]} goed maar op de verkeerde plaats.")
            # ------------------------------------------------------- #
            if uitkomst[0] == generated_code:
                print(f"\nHet antwoord was: {uitkomst[0]}")
                print("\nJe hebt het geraden! Gefeliciteerd!")
                break
            else:
                gamelength += 1


# ------------------------------------------------------------------------------------------ #
# --------------------------- Functions (Player generates the code) ------------------------ #
def check_PlayerCode(user_input,colors):
    """
    Looks at the code the user generated and determines if the
    right colors are used.
    @param user_input: list
    @param colors: list
    @return: boolean
    """
    checker = []
    for i in colors:
        checker.append(i[0])
    for i in user_input:
        if i not in checker:
            return False

    return True


def generate_PlayerCode(colors):
    """
    Generates and checks the code that was entered by the player.
    @param: list
    @return: list
    """
    while True:
        code = input("Voer jouw geheime code in: ")
        if len(code) < 4 or len(code) > 4:
            print("Deze code is niet exact 4 letters lang! Probeer het opnieuw.")
        else:
            playercode = []
            for i in code:
                playercode.append(i)
            checked = check_PlayerCode(playercode, colors)
            if checked == True:
                break
            else:
                print("Deze code bevat niet de juiste letters! Probeer het opnieuw.")

    return playercode


def generate_Possibilities(colorlist):
    """
    This function generates all possible combinations
    with the given list of colors.
    @param colorlist: list
    @return: list
    """
    possible = list(itertools.product(colorlist, repeat=4))
    listpossible = []
    for i in possible:
        listpossible.append(list(i))

    return listpossible


def playgame_VersusPlayer(colors):
    """
    This function runs the game where the player generates
    the code and the computer needs to guess.
    @param colors: list
    @return: void
    """
    print(f"\nWelkom bij Mastermind!\n"
          f"De computer zal jouw code raden door de voorletters te gebruiken van kleuren. (bijvoorbeeld: RGBZ)\n"
          f"De code moet bestaan uit minimaal 4 kleuren die ieder: {colors} kunnen zijn.\n"
          f"Let op: Je moet de kleuren als voorletters invoeren\n")

    code = generate_PlayerCode(colors)
    colorlist = []
    for i in colors:
        colorlist.append(i[0])

    print(f"\n1. Simple Strategy (Shapiro, 1983)\n"
          f"2. Worst Case Strategy (Knuth, 1976-1977)\n"
          f"3. Eigen heuristiek (Justin Klein, 2021)")
    while True:
        algorithm = input("Kies een van de bovenstaande algoritmes: ")
        if algorithm == "1":
            useAlgorithm_SimpleStrategy(code,colorlist)
            break
        elif algorithm == "2":
            useAlgorithm_WorstCase(code,colorlist)
            break
        elif algorithm == "3":
            useAlgorithm_Heuristiek(code,colorlist)
            break
        else:
            print("\nVerkeerde invoer, Kies 1,2 of 3 en probeer het opnieuw!\n")

# --------------------------------------------------------------------------- #
# ---------------------------- The 3 Algorithms ----------------------------- #
def useAlgorithm_SimpleStrategy(code,colorlist):
    """
    This function tries to guess the code that the player
    entered using the Simple Strategy Algorithm by Shapiro (1983)
    It will always find the code, but sometimes might not be within 8 guesses.
    @param code: list
    @param colorlist: list
    @return: void
    """
    possible = generate_Possibilities(colorlist)
    possiblesolutions = possible.copy()

    loop = 0
    while len(possiblesolutions) != 1:
        guess = random.choice(possiblesolutions)
        resultguess = checkanswer(code, guess, colorlist)
        if resultguess[1] == 4:
            print(f"\nFound it!\nThe code was: {guess}")
            break
        for i in possiblesolutions:
            comparison = checkanswer(guess, i, colorlist)
            if (comparison[1] + comparison[2]) != (resultguess[1] + resultguess[2]):
                possiblesolutions.remove(i)
        loop += 1

    print(f"\nHet kostte het Simple-Strategy algoritme {loop} gok(ken)!\n")


def useAlgorithm_WorstCase(code,colorlist):
    """
    This function tries to guess the code that the player
    entered using the Worst-Case Strategy by Knuth (1976-1977)
    It will always find the code, uses "AABB" method as initial guess.
    @param code: list
    @param colorlist: list
    @return: void
    """
    possible = generate_Possibilities(colorlist)
    possiblesolutions = possible.copy()

    guess = ["R","R","G","G"]

    loop = 0
    while len(possiblesolutions) != 1:
        answers = []
        result = checkanswer(code, guess, colorlist)
        if result[1] == 4:
            print(f"\nFound it!\nThe code was: {guess}")
            break
        for i in possiblesolutions:
            comparison = checkanswer(guess, i, colorlist)
            if comparison[1] == result[1] and comparison[2] == result[2]:
                answers.append(i)
        guess = random.choice(answers)
        possiblesolutions = answers.copy()
        loop += 1

    print(f"\nHet kostte het Worst-Case algoritme {loop} gok(ken)!\n")


def useAlgorithm_Heuristiek(code,colorlist):
    """
    This function tries to guess the code that the player
    entered using my own heuristic Strategy (Justin Klein, 2021).
    It will always find the code, and it will always be within 8 guesses.
    @param code: list
    @param colorlist: list
    @return: void
    """
    possible = generate_Possibilities(colorlist)
    possiblesolutions = possible.copy()

    guesses = [
        ["R", "B", "G", "O"],
        ["Z", "R", "B", "G"],
        ["W", "Z", "R", "B"],
        ["O", "W", "Z", "R"]]

    pos = 0
    while pos != (len(guesses)):
        answers = []
        guess = guesses[pos]
        result = checkanswer(code, guess, colorlist)
        if result[1] == 4:
            print(f"\nFound it!\nThe code was: {guess}")
            print(f"\nHet kostte mijn eigen heuristiek {pos+1} gok(ken)!")
            return
        for i in possiblesolutions:
            comparison = checkanswer(guess, i, colorlist)
            if comparison[1] == result[1] and comparison[2] == result[2]:
                answers.append(i)
        possiblesolutions = answers.copy()
        pos += 1

    # ------ This makes sure unnecessary calculation is halted ------ #
    if len(answers) == 1 and answers[0] == code:
        print(f"\nFound it!\nThe code was: {answers[0]}")
        print(f"\nHet kostte mijn eigen heuristiek {pos} gok(ken)!")
        return
    # --------------------------------------------------------------- #
    else:
        guess = random.choice(answers)
        while len(possiblesolutions) != 1:
            result = checkanswer(code, guess, colorlist)
            if result[1] == 4:
                print(f"\nFound it!\nThe code was: {guess}")
                break
            for i in possiblesolutions:
                comparison = checkanswer(guess, i, colorlist)
                if comparison[1] == result[1] and comparison[2] == result[2]:
                    answers.append(i)
            guess = random.choice(answers)
            possiblesolutions = answers.copy()
            pos += 1

    print(f"\nHet kostte mijn eigen heuristiek {pos} gok(ken)!")


# ------------------------------------------------------------------------------------------- #
# -------------------------------------- Start Game ----------------------------------------- #
def Start_Mastermind(colors, length_code):
    """
    Starts the mastermind game.
    @param colors: list
    @param length_code: integer
    @return: void
    """
    print("1. Computer maakt de code, speler raad.\n2. Speler maakt de code, computer raad.")
    while True:
        game_chooser = input("Kies een spelmodus: ")
        if game_chooser == "1":
            playgame_VersusAI(colors, length_code)
            break
        elif game_chooser == "2":
            playgame_VersusPlayer(colors)
            break
        else:
            print("Verkeerde invoer, Kies 1 of 2 en probeer het opnieuw!")


# ----------------------------------------------------------------------------------------- #
# -------------------------------------- Execution ---------------------------------------- #
colors = ["Rood","Groen","Blauw","Oranje","Zwart","Wit"]

length_code = 4
# NOTE: Length_code applies only when the computer generates the code!

Start_Mastermind(colors, length_code)
