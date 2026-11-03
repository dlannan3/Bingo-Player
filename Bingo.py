#Initialize global variables for each letter in BINGO
B = []
I = []
N = []
G = []
O = []

def main(): #Main function of the program that asks for the number called and identifies the column based on the number range
    global B
    defineCards()
    card = input("What number was called?\n")
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
        bingoV()
        card = input("What number was called?\n")
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
                    print(B[i])
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

def bingoV():
    for char in "BINGO":
        bingo = True
        for i in range(len(char)):
            if "x" in char[i]:
                for y in range(len(char[i])):
                    if char[i][y] != "x":
                        print("here")
                        bingo = False
            else:
                print(char[i])
                bingo = False
            if bingo:
                print("BINGO")


main() #Starts the program
