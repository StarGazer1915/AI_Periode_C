# AI - MASTERMIND
# NAAM: Justin Klein - 1707815
# KLAS: V1B (Projectgroep 1)

# Alles is hier in het Engels aangezien ik dat makkelijker vind als ik over code praat.

# ------------------------------------------------------------------------------------------- #
# ---------------------------- Algoritmes (Pseudocode) ----------------------- #
def useAlgorithm_SimpleStrategy(code,colorlist):
    """
    Pseudocode:
        1. Generate a list with all possibilities from colorlist.
        2. Create a second copy of the list so that the .remove() function doesn't overwrite.
        3. As long as possibilities still exist in the list:
                3.1 Take a random guess.
                3.2 Check the black- and whitepins of the guess.
                4. If the blackpins == all correct:
                    ** CODE IS FOUND **
                    break the loop
                5. Loop trough possible solutions and compare them with the guess.
                        ** For loop with this process **
                        5.1 If the sum of black- and whitepins together are not equal to that of the guess:
                            5.1.1 Remove them from all possibilites.

    This goes on until point 4 kicks in and breaks the loop.
    """


def useAlgorithm_WorstCase(code,colorlist):
    """
    Pseudocode:
        1. Generate a list with all possibilities from colorlist.
        2. Create a second copy of the list so that the .remove() function doesn't overwrite.
        3. Take an initial guess.
        4. As long as possibilities still exist in the list:
                4.1 Create/overwrite the temporary answers-list.
                4.2 Check the black- and whitepins of the (initial)guess.
                5 If the blackpins == all correct:
                    ** CODE IS FOUND **
                    break the loop
                6. Loop trough possible solutions and compare them with the guess.
                        ** For loop with this process **
                        6.1 If the of blackpins and whitepins are equal to the black- and whitepins of the guess:
                            6.1.1 Add them to the temporary answers list.
                7. Take a new random guess from the answers list (now it stays randomized)
                8. Make the list of possibilites the temporary answers list.

    This goes on until point 5 kicks in and breaks the loop.
    """


def useAlgorithm_Heuristiek(code,colorlist):
    """
    Pseudocode:
        1. Generate a list with all possibilities from colorlist.
        2. Create a second copy of the list so that the .remove() function doesn't overwrite.
        3. Take 4 initial guesses with all colors included.
        4. As long as there are guesses in the list of initial guesses:
                4.1 Create/overwrite the temporary answers-list.
                4.2 Take the guess from the list of guesses.
                4.3 Check the black- and whitepins of the initial guess.
                5 If the blackpins == all correct:
                    ** CODE IS FOUND **
                    return the function
                6. Loop trough possible solutions and compare them with the guess.
                        ** For loop with this process **
                        6.1 If the of blackpins are equal and the whitepins of the guess are equal:
                            6.1.1 Add them to the temporary answers list.
                7. Make the list of possibilites the temporary answers list.

    This goes on until point 5 kicks in and breaks the loop
    or no answer is found using these guesses and it continues.

        1. Start with a random guess instead of a hardcoded one.
        2. As long as there are guesses in the list of initial guesses:
                2.1 Check the black- and whitepins of the random guess.
                3. If the blackpins == all correct:
                    ** CODE IS FOUND **
                    break the loop
                4. Loop trough possible solutions and compare them with the guess.
                        ** For loop with this process **
                        4.1 If the of blackpins are equal and the whitepins of the guess are equal:
                            4.1.1 Add them to the temporary answers list.
                5. Take a new random guess from the temporary answers list.
                6. Make the list of possibilites the temporary answers list.

    Note: I could place these two loops inside each other, but that would lead to more errors,
    which in turn requires more fixing, which generates more code to fix it, which makes it messy.
    """
