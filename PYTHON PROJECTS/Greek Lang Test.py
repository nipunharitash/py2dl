import random
import os

os.system("")

# Group of Different functions for different styles
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
print(style.YELLOW + """
WELCOME TO GREEK ALPHABET LEARNING PROGRAM
A simple and easy way to learn Greek Alphabets ( both in upper and lower cases). Greek Alphabets are widely used as 
Engineering Symbols in Electromagnetics, Antennas, Linear Control Systems and Signals/Systems Engineering.
Learn the Symbols and then Take a test to know if recognitions of the symbols is completed.

** This program is free to use, distribute and reprogram !! Enjoy **
"""
+ style.RESET
)

greek_alphabets_upper = {
    "ALPHA" : "\u0391",
    "BETA" : "\u0392",
    "GAMMA" : "\u0393",
    "DELTA" : "\u0394",
    "EPSILON" : "\u0395",
    "ZETA" : "\u0396",
    "ETA" : "\u0397",
    "THETA" : "\u0398",
    "IOTA" : "\u0399",
    "KAPPA": "\u039A",
    "LAMDA": "\u039B",
    "MU": "\u039C",
    "NU": "\u039D",
    "XI": "\u039E",
    "OMICRON": "\u039F",
    "PI": "\u03A0",
    "RHO": "\u03A1",
    "SIGMA": "\u03A3",
    "TAU": "\u03A4",
    "UPSILON": "\u03A5",
    "PHI": "\u03A6",
    "CHI": "\u03A7",
    "PSI": "\u03A8",
    "OMEGA": "\u03A9"
}
new_gul ={

    'Α': 'ALPHA', 'Β': 'BETA', 'Γ': 'GAMMA', 'Δ': 'DELTA', 'Ε': 'EPSILON', 'Ζ': 'ZETA',
    'Η': 'ETA', 'Θ': 'THETA', 'Ι': 'IOTA', 'Κ': 'KAPPA', 'Λ': 'LAMDA', 'Μ': 'MU', 'Ν': 'NU',
    'Ξ': 'XI', 'Ο': 'OMICRON', 'Π': 'PI', 'Ρ': 'RHO', 'Σ': 'SIGMA', 'Τ': 'TAU', 'Υ': 'UPSILON',
    'Φ': 'PHI', 'Χ': 'CHI', 'Ψ': 'PSI', 'Ω': 'OMEGA'
}
greek_alphabets_list = ["\u0391","\u0392","\u0393","\u0394","\u0395","\u0396","\u0397","\u0398","\u0399","\u039A","\u039B","\u039C","\u039D","\u039E","\u039F","\u03A0","\u03A1","\u03A3","\u03A4","\u03A5","\u03A6","\u03A7","\u03A8","\u03A9"]

greek_alphabets_lower = {
    "\u03B1" : "ALPHA",
    "\u03B2" : "BETA",
    "\u03B3" : "GAMMA",
    "\u03B4" : "DELTA",
    "\u03B5" : "EPSILON",
    "\u03B6" : "ZETA",
    "\u03B7" : "ETA",
    "\u03B8" : "THETA",
    "\u03B9" : "IOTA",
    "\u03BA" : "KAPPA",
    "\u03BB" : "LAMDA",
    "\u03BC" : "MU",
    "\u03BD" : "NU",
    "\u03BE" : "XI",
    "\u03BF" : "OMICRON",
    "\u03C0" : "PI",
    "\u03C1" : "RHO",
    "\u03C2" : "SIGMA",
    "\u03C3" : "SIGMA",
    "\u03C4" : "TAU",
    "\u03C5" : "UPSILON",
    "\u03C6" : "PHI",
    "\u03C7" : "CHI",
    "\u03C8" : "PSI",
    "\u03C9" : "OMEGA"

}

def learn_greek_alphabets_upper():
    for k, v in greek_alphabets_upper.items():
        print(v, '      ', k)


def learn_greek_alphabets_lower():
    for k, v in greek_alphabets_lower.items():
        print(k, '      ', v)


def test_greek_alphabets_upper():
    r = 0
    w = 0
    for k, v in greek_alphabets_upper.items():

        print("DO YOU RECOGNIZE THIS SYMBOL, " , v , '?')
        userinput3 = input("Name of the Character is :" )

        if userinput3.upper() == k:
            print('Voila !! YOU HAVE LEARNT THE CHARACTER WELL !!!')
            r = r + 1
        else:
            print("Sorry , Learn the Symbol again")
            w = w + 1
            continue
    print(style.RED + "--------------")
    print(" TEST RESULTS ")
    print("--------------")
    print("CORRECT ANSWERS :", r)
    print("INCORRECT ANSWERS : " + style.RESET, w)

def test_greek_alphabets_lower():
    r = 0
    w = 0
    for k, v in greek_alphabets_lower.items():

        print("DO YOU RECOGNIZE THIS SYMBOL, " , k , '?')
        userinput3 = input("Name of the Character is :" )

        if userinput3.upper() == v:
            print('Voila !! YOU HAVE LEARNT THE CHARACTER WELL !!!')
            r = r + 1
        else:
            print("Sorry , Learn the Symbol again")
            w = w + 1
            continue
    print(style.RED + "--------------")
    print(" TEST RESULTS ")
    print("--------------")
    print("CORRECT ANSWERS :", r)
    print("INCORRECT ANSWERS : " + style.RESET , w )



def random_test_greek_alphabets_upper():
    r = 0
    w = 0
    for k, v in new_gul.items():

        letter , name = random.choice(list(new_gul.items()))
        print("Recognize This letter: " , letter)
        answer = input(" Enter Your answer: ")

        if answer.upper() == name:
            print("Voila !! YOU HAVE LEARNT THE CHARACTER WELL !!!")
            r = r + 1
        else:
            print("Sorry , Learn the Symbol again")
            w = w + 1
        continue
    print(style.RED + "--------------")
    print(" TEST RESULTS ")
    print("--------------")
    print("CORRECT ANSWERS :", r)
    print("INCORRECT ANSWERS : " + style.RESET, w)


def random_test_greek_alphabets_lower():
    r = 0
    w = 0
    for k, v in greek_alphabets_lower.items():

        letter , name = random.choice(list(greek_alphabets_lower.items()))
        print("Recognize this letter" , letter)
        answer = input(" Enter Your answer: ")

        if answer.upper() == name:
            print("Voila !! YOU HAVE LEARNT THE CHARACTER WELL !!!")
            r = r + 1
        else:
            print("Sorry , Learn the Symbol again")
            w = w + 1
        continue
    print(style.RED + "--------------")
    print(" TEST RESULTS ")
    print("--------------")
    print("CORRECT ANSWERS :", r)
    print("INCORRECT ANSWERS : " + style.RESET, w)

# THIS IS THE BODY OF THE MAIN PROGRAM WHICH PERFORMS 4 FUNCTIONS VIZ LEARNING ( UPPER AND LOWER )
# TESTING (RANDOM AND SEQUENTIAL)
i = 0
while i == 0:
    print(style.CYAN +" EMBARKING ON GREEK ALPHABET LEARNING JOURNEY")

    userinput1 = input(" Do you wish to learn alphabets (l) or test your skills (t) or quit (q) : " + style.RESET)
    if userinput1.lower() == "l":
        userinput2 = input(" Greek Alphabets has 2 Sets. Do you wish to learn Capitals (C) or Lower (L) or Quit (Q) : ")
        if userinput2.lower() == "c":
            learn_greek_alphabets_upper()
        elif userinput2.lower() == "l":
            learn_greek_alphabets_lower()
        elif userinput2.lower() == "q":
            print(" Thank YOU for using the program !! Have a Nice Day !!")
            break

        else:
            print("Please Select a Valid Option")



    elif userinput1.lower() == "q":
        print(" Thank YOU for using the program !! Have a Nice Day !!")
        break

    elif userinput1.lower() == "t":
        userinput5 = input(" Do You Wish to take Test of Capital Letters  (C) or Small Letters (L) or Quit (Q) : ")
        if userinput5.lower() == "c":
            testchoice1 = input("RANDOM Letters (R) or SEQUENTIAL Letters (S) or QUIT (Q) : ")
            if testchoice1.lower() == "r":
                random_test_greek_alphabets_upper()
            elif testchoice1.lower() == "s":
                test_greek_alphabets_upper()
            elif testchoice1.lower() == "q":
                print(" Thank YOU for using the program !! Have a Nice Day !!")
                break
            else:
                print("Please Select a Valid Option")
        elif userinput5.lower() == "l":
            testchoice2 = input("RANDOM Letters (R) or SEQUENTIAL Letters (S) or QUIT (Q) : ")
            if testchoice2.lower() == "r":
                random_test_greek_alphabets_lower()
            elif testchoice2.lower() == "s":
                test_greek_alphabets_lower()
            elif testchoice2.lower() == "q":
                print(" Thank YOU for using the program !! Have a Nice Day !!")
                break
            else:
                print("Please Select a Valid Option")
        elif userinput5.lower() == "q":
            print(" Thank YOU for using the program !! Have a Nice Day !!")
            break
        else:
            print("Please Select a Valid Option")

    else:
        print("Please Select a Valid Option")