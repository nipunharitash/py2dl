import math
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

    #############
    # SECTION 1 OF THE PROGRAM FOR GENERATING ADDRESS LOCATIONS.
    #############
print("")
print("MEMORY ADDRESS MAPPING TOOL FOR MICROPROCESSORS AND MICROCONTROLLERS")
print('''   
This tool lets you calculate the total number of address locations [in hexadecimals], "
in the memory of a specific size with a specific register size. This tool can be used as
a building block for creating memory segmentation and multiple RAM/ROM implementations''')
while True:
    print("")
    print(style.YELLOW + " WELCOME TO MEMORY MAPPING TOOL FOR MICROPROCESSORS AND MICROCONTROLLERS" + style.RESET)

    try:

        n = int(input(style.CYAN + " Enter Memory Size (preferably an integer in multiples of power of 2) : " + style.RESET))
    except ValueError:
        print("Enter Valid Input Please")
        break

    m = (input(style.CYAN +" Enter Memory Multiplier [(B)yte, (k)ilobyte, (M)egabyte, (G)igabyte, (T)erabyte )] or (Q)uit: " + style.RESET))
    #memorysize(n,m)
    if m.lower() == "k":
        s = n * 1024
        t = math.log2(s)
        sizeinbytes = int(2 ** t)
        print(" Total Memory Size in Bytes is : ", sizeinbytes, "B")

    elif m.lower() == "b":
        s = n
        t = math.log2(s)
        sizeinbytes = int(2 ** t)
        print(" Total Memory Size in Bytes is : ", sizeinbytes, "B")

    elif m.lower() == "m":
        s = n * 1024 * 1024
        t = math.log2(s)
        sizeinbytes = int(2 ** t)
        print(" Total Memory Size in Bytes is : ", sizeinbytes, "B")

    elif m.lower() == "g":
        s = n * 1024 * 1024 * 1024
        t = math.log2(s)
        sizeinbytes = int(2 ** t)
        print(" Total Memory Size in Bytes is : ", sizeinbytes, "B")

    elif m.lower() == "t":
        s = n * 1024 * 1024 * 1024 * 1024
        t = math.log2(s)
        sizeinbytes = int(2 ** t)
        print(" Total Memory Size in Bytes is : ", sizeinbytes, "B")

    elif m.lower() == "q":
        print(" Thank you for Trying the Program")
        break
    else:
        print(" Enter a Valid Value")
        break


    #############
    # SECTION 2 OF THE PROGRAM FOR GENERATING ADDRESS MAP.
    #############

    print("")
    mem_map = input(style.MAGENTA +" Do You wish to calculate MEMORY ADDRESS MAP of this Memory : Y or N : ")
    if mem_map.lower() == "y":
        reg_size = int(input(" Enter Register Size in bytes (Multiples of 2 powers ) : " + style.RESET))
        new_memsize = (sizeinbytes/reg_size)
        len_newmem = int(new_memsize)
        if len_newmem > 0:
            print(" Total number of registers in memory of [", n, m, "] are : ", len_newmem)

            print(" The first address of the memory is : " , hex(0) , "H")
            print(" The last address of the memory is : ", hex(len_newmem - 1) , "H")
        else:
            print(" Register Size cannot be greater than the total memory size !!")
            break
    elif mem_map.lower() == "n":
        print(" Thank you for using the Program !!")
        break
    else:
        break


