print("""
    Welcome to Virtual Tibetan Wheel Program. This program takes a mantra of your choice and 
    recites ** (saves as a text file) 1008 Times for each rotation of the wheel. You will specify 
    the number of times you want to turn the wheel. The text file with recited mantra in multiples 
    of 1008 is saved in the current directory as MantraChant.txt. Avoid specifying excessively big
    number in turns as it may result in an excessively large file being produced.
    """
)

from tqdm import tqdm
from art import *
chant = input("     Which mantra do you want to chant: ")
f = open("MantraChant.txt" , 'w')
chantlist = chant.split(" ")
twowords = (chantlist[:3])
twowords = ' '.join(twowords)

spin = int(input("     How many times do you want to spin the TIBETAN WHEEL: "))
mantra = text2art(twowords)
print(mantra)
for num1 in tqdm(range(1008)):
    for num2 in (range(spin+1)):
        #print(chant)
        f.write(chant + "\n")
f.close()
print("""
    Thank you for spinning the Virtual Tibetan Wheel. The recited mantra is saved as txt file in
    the current directory. Run the program again to spin the wheel. 


""")