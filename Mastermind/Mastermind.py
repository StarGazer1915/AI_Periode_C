# AI - MASTERMIND
# NAAM: Justin Klein - 1707815
# KLAS: V1B

# NL: Print statements zijn in het Nederlands, verder is de code in het Engels.
# ENG: Print statements are in Dutch, the remaining code is in English.

import random

# ------------------------------- #
# ---------- Functions ---------- #
def generateCode(colors, length):
    """
    Creates the code that the player needs to guess.
    @param colors: list
    @param length: integer
    @return: list
    """
    generated = []
    for i in range(0,length):
        j = random.choice(colors)
        generated.append(j[0])

    return generated


def canBeChecked(generated_code,user_input,colors):
    """
    Looks at the user input and determines if the right characters
    are used and if the lists are the same length.
    @param generated_code: list
    @param user_input: list
    @return: boolean / list
    """
    checker = []
    pos = 0
    for i in colors:
        checker.append(i[0])
        pos += 1

    if len(user_input) > len(generated_code) or len(user_input) < len(generated_code):
        return False
    else:
        for i in user_input:
            if i not in checker:
                return False


def checkanswer(generated_code,user_input,colors):
    """
    Checks if the given answer is correct (or almost correct).
    @param generated_code: list
    @param user_input: string
    @param colors: list
    @return: boolean / list
    """
    inputlist = []
    for i in user_input:
        inputlist.append(i.upper())

    # ------ Checks if code can be checked ------ #
    if canBeChecked(generated_code,inputlist,colors) == False:
        return False

    # ------ Checks the actual code ------ #
    checklist = inputlist
    blackPin = 0
    whitePin = 0
    pos = 0
    result = []

    for i in inputlist:
        if i == generated_code[pos]:
            result.append(i)
            blackPin += 1
        else:
            result.append("?")
        pos += 1

    for i in generated_code:
        if i in checklist:
            checklist.remove(i)
            whitePin += 1

    whitePin -= blackPin
    print(f"Je hebt er {blackPin} op de juiste plaats.\n"
          f"{whitePin} goed maar op de verkeerde plaats.")

    return result


def playgame(colors, length_code):
    """
    This function runs the game.
    @param colors: list
    @param length_code: integer
    """
    code_start = []
    for i in range(0,length_code):
        code_start.append("?")

    generated_code = generateCode(colors,length_code)
    print(f"Welkom bij Mastermind!\n"
          f"Raad de code door de voorletters te gebruiken van kleuren. (bijvoorbeeld: RGBZ)\n"
          f"De code bestaat uit {length_code} kleuren die ieder: {colors} kunnen zijn.\n"
          f"Let op: Je hebt maar 8 kansen!\n"
          f"De computer heeft een code gegenereerd! Veel succes!")
    print(f"\n{code_start}")

    gamelength = 0
    while True:
        user_input = input("Wat denk je dat de code is?: ")
        uitkomst = checkanswer(generated_code,user_input,colors)
        if uitkomst == False:
            print(f"Deze code is niet valide. Bekijk de lengte of de ingevulde kleuren en probeer het opnieuw!\n")
        else:
            if uitkomst != generated_code and gamelength > 6:
                print("\nHelaas! Je hebt al je beurten verspild. De computer heeft gewonnen!")
                print(f"\nHet antwoord was: {uitkomst}")
                break
            elif uitkomst == generated_code:
                print(f"\nHet antwoord was: {uitkomst}")
                print("\nJe hebt het geraden! Gefeliciteerd!")
                break
            else:
                print(f"\n{uitkomst}")
        gamelength += 1


# ------------------------------- #
# ---------- Execution ---------- #
colors = ["Rood","Groen","Blauw","Oranje","Zwart","Wit"]
length_code = 4
playgame(colors,length_code)