# AI - MASTERMIND # NAAM: Justin Klein - 1707815 # KLAS: V1B

import random

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

def checkanswer(generated_code,user_input,colors):
    """
    Checks if the given answer is correct (or almost correct).
    @param generated_code: list
    @param user_input: string
    @param colors: list
    @return: list
    """
    user_input = user_input.upper()
    checker = []
    # --- Checks if code can be checked --- #
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

    # --- Checks the code --- #
    pos = 0
    resultaat = []
    goed_bijna_fout = [0,0,0]
    for i in user_input:
        if i == generated_code[pos]:
            resultaat.append(i)
            goed_bijna_fout[0] += 1
        elif i != generated_code[pos] and i in generated_code[:1]:
            resultaat.append("?")
            goed_bijna_fout[1] += 1
        else:
            resultaat.append("?")
            goed_bijna_fout[2] += 1
        pos += 1

    print(f"Je hebt er {goed_bijna_fout[0]} goed, "
          f"{goed_bijna_fout[1]} op de verkeerde plaats en "
          f"{goed_bijna_fout[2]} fout!")

    return resultaat

def playgame(colors, length_code):
    """
    This function runs the game.
    @param colors: list
    @param length_code: integer
    """
    code_begin = []
    for i in range(0,length_code):
        code_begin.append("?")

    generated_code = generateCode(colors,length_code)
    print(f"Welkom bij Mastermind!\n"
          f"Raad de code door de voorletters te gebruiken van kleuren. (bijvoorbeeld: RGBZ)\n"
          f"De code bestaat uit {length_code} kleuren die ieder: {colors} kunnen zijn.\n"
          f"De computer heeft een code gegenereerd! Veel succes!")
    print(f"\n{code_begin}")

    while True:
        user_input = input("Wat denk je dat de code is?: ")
        uitkomst = checkanswer(generated_code,user_input,colors)
        if uitkomst == False:
            print(f"Deze code is niet valide. Bekijk de lengte of de ingevulde kleuren en probeer het opnieuw!\n")
        else:
            if uitkomst == generated_code:
                print("\nJe hebt het geraden! Gefeliciteerd!")
                break
            print(f"\n{uitkomst}")


# ---------- Execution ---------- #
colors = ["Rood","Groen","Blauw","Wit","Zwart"]
length_code = 4
playgame(colors,length_code)