# AI - FORMATIEVE OPDRACHT 1A
# NAAM: Justin Klein
# KLAS: 15 - V1B
# Informatie van functies in het engels. Mocht dit niet wenselijk zijn dan hoor ik dat graag.

import random

# ---------------------------------------------- #
# ------------------ OPGAVE 1 ------------------ #
def opgave_1_pyramidFor():
    """
    Prints stars to form a pyramid with the given length of the variable.
    This uses for loops.
    """
    lengte = int(input("Wat is de lengte van de variabele?: "))
    for i in range(0,lengte):
        print(i*"*")
    for i in range(lengte,0,-1):
        print(i*"*")

#opgave_1_pyramidFor()


def opgave_1_pyramidWhile():
    """
    Prints stars to form a pyramid with the given length of the variable.
    This uses while loops.
    """
    lengte = int(input("Wat is de lengte van de variabele?: "))
    x = 1
    while True:
        if x == lengte:
            break
        print(x * "*")
        x += 1
    while True:
        if x == 0:
            break
        print(x * "*")
        x -= 1

#opgave_1_pyramidWhile()


def opgave_1_pyramidReverse():
    """
    Prints stars to form a pyramid with the given length of the variable.
    This version is in reverse.
    """
    lengte = int(input("Wat is de lengte van de variabele?: "))
    for i in range(lengte,1,-1):
        print(i*"*")
    for i in range(1,lengte+1):
        print(i*"*")

#opgave_1_pyramidReverse()


# ---------------------------------------------- #
# ------------------ OPGAVE 2 ------------------ #
def opgave_2_tekstcheck():
    """
    Checks where the strings start to deviate from each other.
    @return: string
    """
    string1 = input("Voer de eerste string in: ")
    string2 = input("Voer de tweede string in: ")
    x = 0
    for i in string1:
        if x != len(string2):
            if i == string2[x]:
                x += 1
            else:
                return f"Het gaat bij index {x} fout!"
        else:
            return f"String2 is korter dan String1. Tot index {x} geen verschil."

    return "De strings zijn gelijk."

#print(opgave_2_tekstcheck())


# ---------------------------------------------- #
# ------------------ OPGAVE 3 ------------------ #
def count(getal, lijst):
    """
    Counts the amount of times a number appears in a list.
    @param getal: int
    @param lijst: list
    @return: int
    """
    aantal = 0
    for i in lijst:
        if i == getal:
            aantal += 1
    return aantal

#lijst = [4,1,7,5,1,0,4,1,4,7,3,1,8,1,3]
#print(count(4,lijst))


def greatestdif(lijst):
    """
    Calculates the differences between each element and returns the highest value.
    @param lijst: list
    @return: int
    """
    x = 1
    differences = []
    for i in lijst:
        if x != len(lijst):
            if i < lijst[x]:
                differences.append(lijst[x] - i)
            elif i > lijst[x]:
                differences.append(i - lijst[x])
            x += 1
    return max(differences)

#lijst = [15,87,32,156,0,15,42,1,2,994]
#print(greatestdif(lijst))


def moreOnesThanZeroes(lijst):
    """
    Uses the count() function to determine if there are more ones than zeroes in a list.
    @param lijst: list
    @return: boolean
    """
    ones = count(1, lijst)
    zeroes = count(0, lijst)
    if ones > zeroes and not zeroes >= 12:
        return True
    elif ones < zeroes and not zeroes >= 12:
        return False

#lijst = [0,1,1,1,1,1,0,1,0,0,0,1,0,1,1,0,1,0,1,0,1]
#print(moreOnesThanZeroes(lijst))


# ---------------------------------------------- #
# ------------------ OPGAVE 4 ------------------ #
def opgave_4_palindroomLib(woord):
    """
    Checks if the given word is the same when reversed. This function uses library functions.
    @param woord: string
    @return: boolean
    """
    return woord == woord[::-1]

#woord = "radar"
#woord = "justin"
#print(opgave_4_palindroomLib(woord))


def opgave_4_palindroomSelf(woord):
    """
    Checks if the given word is the same when reversed. (No library functions)
    @param woord: string
    @return: boolean
    """
    woord2 = ""
    for i in woord:
        woord2 = i + woord2
    if woord2 == woord:
        return True
    else:
        return False

#woord = "radar"
#woord = "justin"
#print(opgave_4_palindroomSelf(woord))


# ---------------------------------------------- #
# ------------------ OPGAVE 5 ------------------ #
def gebruikSimpleSort(lijst):
    """
    Sorts the list with a built-in sort function.
    @param lijst: list
    @return: list
    """
    return sorted(lijst)

#lijst = [1,9,3,6,4,8,5,7,2]
#print(gebruikSimpleSort(lijst))


def gebruikQuickSort(lijst):
    """
    Sorts the list by using the quick sort algorithm.
    @param lijst: list
    @return: list
    """
    if len(lijst) <= 1:
        return lijst
    else:
        pivot = lijst.pop()

    groter = []
    lager = []
    for i in lijst:
        if i > pivot:
            groter.append(i)
        elif i < pivot:
            lager.append(i)

    return gebruikQuickSort(lager) + [pivot] + gebruikQuickSort(groter)

#lijst = [1,9,3,6,4,8,5,7,2]
#print(gebruikQuickSort(lijst))


# ---------------------------------------------- #
# ------------------ OPGAVE 6 ------------------ #
def calculateMean(lijst):
    """
    Calculates the mean of the values in the list.
    @param lijst: list
    @return: float
    """
    return sum(lijst) / len(lijst)

#print(calculateMean([56,32,87,21]))


def calculateMultipleMeans(lijsten):
    """
    Calculates the means of the values in the lists.
    @param lijsten: list(s)
    @return: list
    """
    meanlist = []
    for i in lijsten:
        meanlist.append(round(calculateMean(i),2))
    return meanlist

#lijsten = [532,634,135,765,154],[1,9,3,6,4,8,5,7,2],[1,9,55,4,32,56,43,21],[90,776,432,173,252,0]
#print(calculateMultipleMeans(lijsten))


# ---------------------------------------------- #
# ------------------ OPGAVE 7 ------------------ #
def randomGuesser():
    """
    Generates a random number and lets the user try to guess it until it is found.
    """
    cijfer = random.randint(1,10)
    gok = int(input("Welk getal denkt u dat het is? (1-10): "))
    while True:
        gok = int(input("Helaas! Probeer het opnieuw! (tussen 1-10): "))
        if gok == cijfer:
            print("Correct! You did it!")
            break
        else:
            continue

#randomGuesser()


# ---------------------------------------------- #
# ------------------ OPGAVE 8 ------------------ #
def spacekiller(textfile):
    """
    This ominous sounding function destroys all spaces and newlines in the given text.
    @param textfile: string
    @return: string
    """
    result = ""
    with open(textfile, "r") as file:
        text = file.readlines()
    for i in text:
        j = i.replace(" ", "")
        h = j.replace("\n", "")
        result += h
    return f"-- Spacekiller has eliminated it's targets. --\nResult:\n'{result}'"

#print(spacekiller("1a_Textfile"))


# ---------------------------------------------- #
# ------------------ OPGAVE 9 ------------------ #
def cyclischVerschuiven(ch, n):
    """
    Cycles the ones and zeroes to the left if n > 0 and to the right if n < 0.
    @param ch: int
    @param n: int
    @return: list
    """
    waarde = bin(ch)[2:]
    fullbyte = str(waarde).zfill(8)
    lst = []
    for i in fullbyte:
        lst.append(i)
    if n > 0:
        for i in range(0,n):
            lst.append(str(lst[0]))
            lst.pop(0)
    elif n < 0:
        for i in range(n,0):
            lst.insert(0,str(lst[7]))
            lst.pop(8)
    return lst

#print(cyclischVerschuiven(62, 3))
#print(cyclischVerschuiven(62, -4))


# ----------------------------------------------- #
# ------------------ OPGAVE 10 ------------------ #
def opgave_10_fibonacci(n, v0=0, v1=1):
    """
    Builds up for n amount of times and sums itself up with the previous pair of integers.
    0,1 = 1 -> 1,1 -> 2 -> 1,2 -> 3, etc.
    @param n: int
    @param v0: int
    @param v1: int
    @return: int
    """
    return opgave_10_fibonacci(n-1, v1, v0+v1) if n > 1 else (v0, v1)[n]

#print(opgave_10_fibonacci(15))

# ----------------------------------------------- #
# ------------------ OPGAVE 11 ------------------ #
def ceasarCipher():
    """
    Encrypts a message using the ceasar cipher.
    """
    text = input("Geef een tekst: ")
    rotatie = int(input("Geef een rotatie: "))
    abc = "abcdefghijklmnopqrstuvwxyz"
    tekst = text.lower()
    zin = ""
    print(f"Before: {tekst}")

    for item in tekst:
        if item in " ,.?!@#$%^&*(){}[]<>|/":
            zin += item
            continue
        else:
            nieuw = (abc.index(item) + rotatie) % 26
            verandering = item.replace(item, abc[nieuw])
            zin += verandering

    print(f"After: {zin}")

ceasarCipher()


# ----------------------------------------------- #
# ------------------ OPGAVE 12 ------------------ #
def fizzBuzz():
    """
    Prints integers from 0-100 and integers that can be divided by 3,5 or both are printed as
    fizz, buzz or fizzbuzz.
    """
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

#fizzBuzz()

