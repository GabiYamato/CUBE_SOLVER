import kociemba 

import numpy as np

def SOLVEALGORITHM(input):
    try:
        return kociemba.solve(input)
    except:
        print("invalid input")
        
def line_space():
    for i in range(75):
        print("_",end='')
    print()

def print_statements ():
    
    line_space()
    print("          ______    __     __    _________    _________  ")
    print("         |  ____|  |  |   |  |  |  _____  |  | ________|   ")
    print("         | |       |  |   |  |  | |_____| |  | |____   ")
    print("         | |       |  |   |  |  |  _____  |  |  ____|    ")
    print("         | |____   |  |___|  |  | |_____| |  | |_______  ")
    print("         |______|  |_________|  |_________|  |_________| ")
    
    print("                                                                                              ")    
    print("   _______    _________    __      ___      ___   ________    ______")
    print("  |  _____|  |   ___   |  |  |     \  \    /  /  |  ______|  |  _____ |")
    print("  | |_____   |  |   |  |  |  |      \  \  /  /   | |____     |  ______|")
    print("  |_____  |  |  |   |  |  |  |       \  \/  /    |  ____|    |   \  \ ")
    print("   _____| |  |  |___|  |  |  |____    \    /     | |______   |  | \  \ ")
    print("  |_______|  |_________|  |_______|    \__/      |________|  |__|  \__\  ")
    line_space()
    
    
def cubestateforinput():
    print("\n cube position: \n make sure your cube is in shown position:")
    print("        |*******|")
    print("        |*WHITE*|")
    print("        |*******|")
    print(" *******|*******|*******|*******")
    print(" *ORANGE|*GREEN*|**RED**|*BLUE**")
    print(" *******|*******|*******|*******")
    print("        |*******|")
    print("        |*YELLOW|")
    print("        |*******|")
    print()
    line_space()

def pieceslocation():
    line_space()
    print("LOCATION OF PIECES: \n")
    line_space()
    print("             |************|")
    print("             |*1 * 2 * 3 *|")
    print("             |************|")
    print("             |*4 * 5 * 6 *|")
    print("             |************|")
    print("             |*7 * 8 * 9 *|")
    print("             |************|")
    print(" ************|************|************|************")
    print(" *37 *38 *39*|*19 *20 *21*|*10* 11* 12*|*46 *47 *48*")
    print(" ************|************|************|************")
    print(" *40 *41 *42*|*22 *23 *24*|*13 *14 *15*|*49 *50 *51*")
    print(" ************|************|************|************")
    print(" *43 *44 *45*|*25 *26 *27*|*16 *17 *18*|*52 *53 *54*")
    print(" ************|************|************|************")
    print("             |************|")
    print("             |*28 *29 *30*|")
    print("             |************|")
    print("             |*31 *32 *33*|")
    print("             |************|")
    print("             |*34 *35 *36*|")
    print("             |************|")
    line_space()


state= np.empty((6,9))
def camscan(input):
    pass

def colortokoci(input):
    if input=='G':
        return 'F'
    elif input == 'R':
        return 'R'
    elif input == 'O':
        return 'L'
    elif input == 'B':
        return 'B'
    elif input == 'Y':
        return 'D'
    elif input == 'W':
        return 'U'
    
def moves():
    pass


def proper_input():
    while True:
        randomvar1=input("enter color: [R,G,B,O,Y,W]- ")
        if randomvar1 in ("RGBOWY"):
            break
        elif randomvar1 =='' or randomvar1 =='\n':
            print("invalid input.")
        else:
            print("invalid input, enter again!")     
    return randomvar1           
    
def list_change(list):
    pieceslocation()
    while True:
        i=int(input("enter the number of the piece you want to change:"))
        list[i-1]=colortokoci(proper_input())
        temp=int(input("saved...press (0) to exit, (1) to change another value"))
        if temp == 0:
            break

def list_to_string(list):
    str= ''
    return(str.join(list))

#this code will not run if file is imported as a module (the part under the if loop)
if __name__=='__main__':
    print_statements()
    while True:
        cubestateforinput()
        print("PLEASE PUT YOUR CUBE IN THIS POSITION, GREEN FACING FRONT AND WHITE ON TOP!")
        
        list=[]
        
        for i in ('white','red','green','yellow','orange','blue'):
            print('side:',i)
            for j in range(9):
                a=proper_input()
                list.append(colortokoci(a))
        if int(input("press (0) if you need to edit a value")) == 0:
            list_change(list)
        
        M=list_to_string(list)
        #print(M)
        k=SOLVEALGORITHM(M)
        print('SOLUTION:',k)
        break
