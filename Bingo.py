import os
#Initialize global variables for each letter in BINGO
B = []
I = []
N = []
G = []
O = []
lists = {
    "B" : B,
    "I" : I,
    "N" : N,
    "G" : G,
    "O" : O
}

def clear(): #Clears the console when called
    os.system('cls' if os.name == 'nt' else 'clear')

def main(): #Main function of the program that asks for the number called and identifies the column based on the number range
    global B, I, N, G, O
    #Clears each list when the program is started
    B.clear()
    I.clear()
    N.clear()
    G.clear()
    O.clear()
    defineCards()
    clear() #Clears the console before asking for the first number
    card = input("What number was called?\n")
    clear() #Clears the console after asking for number called
    print(card) #Reprints the last call while keeping the variable defined to create a pause
    while(card != "quit" and card != "new"): #Loops the function until the user enters "quit" or "new"
        card = int(card)
        if(card <= 15):
            print(scanB(str(card)))
        elif(card <= 30):
            print(scanI(str(card)))
        elif(card <= 45):
            print(scanN(str(card)))
        elif(card <= 60):
            print(scanG(str(card)))
        else:
            print(scanO(str(card)))
        bingoV() #Checks for vertical bingos
        bingoH() #Checks for horizontal bingos
        bingoD() #Checks for diagonal bingos
        card = input("What number was called?\n")
        clear() #Clears the console after asking for number called
        print(card) #Reprints the last call while keeping the variable defined to create a pause
    if(card == "new"): #Restarts the program

        main()

def defineCards(): #Defines each list for the cards and their columns
    global B,I,N,G,O
    loops = int(input("How many cards do you have?\n")) #Asks the user how many cards they are going to use and turns it to an integer
    for i in range(loops): #The user is asked for the 5 numbers in each column, then it loops as many times as the user specified cards
        print(f"Please enter the B values for card {i + 1}") 
        B.append([input() for _ in range(5)]) #Appends a list as a value in the list B
        print(f"Please enter the I values for card {i + 1}")
        I.append([input() for _ in range(5)]) #Appends a list as a value in the list I
        print(f"Please enter the N values for card {i + 1}")
        N.append([input() for _ in range(4)]) #Appends a list as a value in the list N
        print(f"Please enter the G values for card {i + 1}")
        G.append([input() for _ in range(5)]) #Appends a list as a value in the list G
        print(f"Please enter the O values for card {i + 1}")
        O.append([input() for _ in range(5)]) #Appends a list as a value in the list O
        N[i].insert(2,"x") #Creates the free space on each card before moving to the next


def scanB(call): #Each functions checks if the number entered is on any of the cards by checking the column identified in main()
    global B
    cards = []
    for i in range(len(B)):
        if (call in B[i]):
            for y in range(len(B[i])):
                if (call == B[i][y]):
                    B[i][y] = "x"
            cards.append(f"Card {i+1} Column B") #Appends to the local list "cards" with an identifier for the user to know what cards have that number in column B
    return cards
def scanI(call):
    global I
    cards = []
    for i in range(len(I)):
        if (call in I[i]):
            for y in range(len(I[i])):
                if (call == I[i][y]):
                    I[i][y] = "x"
            cards.append(f"Card {i+1} Column I") #Appends to the local list "cards" with an identifier for the user to know what cards have that number in column I
    return cards
def scanN(call):
    global N
    cards = []
    for i in range(len(N)):
        if (call in N[i]):
            for y in range(len(N[i])):
                if (call == N[i][y]):
                    N[i][y] = "x"
            cards.append(f"Card {i+1} Column N") #Appends to the local list "cards" with an identifier for the user to know what cards have that number in column N
    return cards
def scanG(call):
    global G
    cards = []
    for i in range(len(G)):
        if (call in G[i]):
            for y in range(len(G[i])):
                if (call == G[i][y]):
                    G[i][y] = "x"
            cards.append(f"Card {i+1} Column G") #Appends to the local list "cards" with an identifier for the user to know what cards have that number in column G
    return cards
def scanO(call):
    global O
    cards = []
    for i in range(len(O)):
        if (call in O[i]):
            for y in range(len(O[i])):
                if (call == O[i][y]):
                    O[i][y] = "x"
            cards.append(f"Card {i+1} Column O") #Appends to the local list "cards" with an identifier for the user to know what cards have that number in column O
    return cards

def bingoV(): #Check for a bingo in each column
    for char in "BINGO": #Cycles through each column
        charL = lists[char] #Converts letters as a string to the list names
        bingo = True #Starts bingo as true until proven false
        for i in range(len(charL)): #Loops through each card
            if "x" in charL[i]: #Checks if there are an x's at all and breaks if none have been dabbed
                for y in range(len(charL[i])): #Loops through each index of the column
                    if charL[i][y] != "x": #Checks if any numbers in the column aren't dabbed
                        bingo = False
            else:
                bingo = False #Sets bingo to false if there are no numbers dabbed
            if bingo:
                callBingo(i) #Calls bingo if never proven wrong


def bingoD(): #Checks for a bingo on the diagonals
    for i in range(len(B)): #Loops through each card
        if (B[i][0] == "x" and I[i][1] =="x" and G[i][3] == "x" and O[i][4] == "x"): #Checks for diagonal from top left to bottom right
            callBingo(i)
        elif(B[i][4] == "x" and I[i][3] =="x" and G[i][1] == "x" and O[i][0] == "x"): #Check for diagonal from bottom left to top right
            callBingo(i)

def bingoH(): #Checks for a bingo on the horizontals
    for i in range(len(B)): #Loops through each card
        if "x" in B[i]: #Checks to see if there are any x's in column B since there must be atleast one to have a horizontal
            for x in range(len(B[i])): #Loops through each index of each card
                if (B[i][x] == "x" and I[i][x] == "x" and N[i][x] == "x" and G[i][x] == "x" and O[i][x] == "x"):
                    callBingo(i) #Calls bingo if any horizontals are found


def callBingo(i): #Prints the card number and layout for the user to dab them
    print(f"BINGO on card {i+1}\n") #Displays the card number and creates a blank line below
    print(" B  I  N  G  O") #Identifies the rows
    #Prints the numbers and dabs for the card with bingo
    print(f"{B[i][0]} {I[i][0]} {N[i][0]} {G[i][0]} {O[i][0]}")
    print(f"{B[i][1]} {I[i][1]} {N[i][1]} {G[i][1]} {O[i][1]}")
    print(f"{B[i][2]} {I[i][2]} {N[i][2]} {G[i][2]} {O[i][2]}")
    print(f"{B[i][3]} {I[i][3]} {N[i][3]} {G[i][3]} {O[i][3]}")
    print(f"{B[i][4]} {I[i][4]} {N[i][4]} {G[i][4]} {O[i][4]}\n") #Creates a blank space below the card

if __name__ == "__main__":
    main() #Starts the program
