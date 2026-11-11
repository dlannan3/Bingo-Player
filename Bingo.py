import os
import random as r
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

#Program Functions
def clear(): #Clears the console when called
    os.system('cls' if os.name == 'nt' else 'clear')


def main(): #Main function of the program that asks for the number called and identifies the column based on the number range
    global B, I, N, G, O
    nums = 0
    #Clears each list when the program is started
    clear() #Clears the console before asking for the first number
    B.clear()
    I.clear()
    N.clear()
    G.clear()
    O.clear()
    defineCards()
    card = input("What number was called?\n")
    clear() #Clears the console after asking for number called
    print(card) #Reprints the last call while keeping the variable defined to create a pause
    while(card != "quit" and card != "new"): #Loops the function until the user enters "quit" or "new"
        if nums <= 3:
            nums += 1
        if test(card):
            nums = 4
        else:
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
        if nums >= 4:
            bingoV() #Checks for vertical bingos
            bingoD() #Checks for diagonal bingos
            bingoH() #Checks for horizontal bingos
        card = input("What number was called?\n")
        clear() #Clears the console after asking for number called
        print(card) #Reprints the last call while keeping the variable defined to create a pause
    if(card == "new"): #Restarts the program
        main()


def defineCards(): #Defines each list for the cards and their columns
    global B,I,N,G,O
    loops = input("How many cards do you have?\n") #Asks the user how many cards they are going to use and turns it to an integer
    clear()
    if "test" in loops:
        for i in range(int(loops.split()[1])): #Generates a random card as many times as the user states
            B.append([f'{r.randint(1,15)}',f'{r.randint(1,15)}',f'{r.randint(1,15)}',f'{r.randint(1,15)}',f'{r.randint(1,15)}'])
            I.append([f'{r.randint(16,30)}',f'{r.randint(16,30)}',f'{r.randint(16,30)}',f'{r.randint(16,30)}',f'{r.randint(16,30)}'])
            N.append([f'{r.randint(31,45)}',f'{r.randint(31,45)}',f'{r.randint(31,45)}',f'{r.randint(31,45)}',f'{r.randint(31,45)}'])
            G.append([f'{r.randint(46,60)}',f'{r.randint(46,60)}',f'{r.randint(46,60)}',f'{r.randint(46,60)}',f'{r.randint(46,60)}'])
            O.append([f'{r.randint(61,75)}',f'{r.randint(61,75)}',f'{r.randint(61,75)}',f'{r.randint(61,75)}',f'{r.randint(61,75)}'])
        clear()
        print(f"Number of cards: {loops.split()[1]}") #Reminds the user as to how many test cards they chose
        print("Test Card Layouts:")
        for i in range(int(loops.split()[1])): #Displays each card separately for the player to see
            print(f'Card {i+1}')
            print(" B  I  N  G  O")
            print(f"{B[i][0]} {I[i][0]} {N[i][0]} {G[i][0]} {O[i][0]}")
            print(f"{B[i][1]} {I[i][1]} {N[i][1]} {G[i][1]} {O[i][1]}")
            print(f"{B[i][2]} {I[i][2]} {N[i][2]} {G[i][2]} {O[i][2]}")
            print(f"{B[i][3]} {I[i][3]} {N[i][3]} {G[i][3]} {O[i][3]}")
            print(f"{B[i][4]} {I[i][4]} {N[i][4]} {G[i][4]} {O[i][4]}\n\n")
        input("Press enter to continue") #Pauses the program until the player is doing previewing the cards
    else:
        for i in range(int(loops)): #The user is asked for the 5 numbers in each column, then it loops as many times as the user specified cards
            print(f"Please enter the B values for card {i + 1}") 
            B.append([input() for _ in range(5)]) #Appends a list as a value in the list B
            clear()
            print(f"Please enter the I values for card {i + 1}")
            I.append([input() for _ in range(5)]) #Appends a list as a value in the list I
            clear()
            print(f"Please enter the N values for card {i + 1}")
            N.append([input() for _ in range(4)]) #Appends a list as a value in the list N
            clear()
            print(f"Please enter the G values for card {i + 1}")
            G.append([input() for _ in range(5)]) #Appends a list as a value in the list G
            clear()
            print(f"Please enter the O values for card {i + 1}")
            O.append([input() for _ in range(5)]) #Appends a list as a value in the list O
            clear()
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
                if (B[i][x] == "x" and I[i][x] == "x" and N[i][x] == "x" and G[i][x] == "x" and O[i][x] == "x"): #Checks for an x in each column of a specific index
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


def test(card): #Allows the user to type certain codes to instantly bingo
    if "D1" in card:
        cardnum = int(list(card)[2]) - 1 #Checks what card the player wants to bingo on
        scanB(B[cardnum][0])
        scanI(I[cardnum][1])
        scanG(G[cardnum][3])
        scanO(O[cardnum][4])
        return True
    elif "D2" in card:
        cardnum = int(list(card)[2])-1 #Checks what card the player wants to bingo on
        scanB(B[cardnum][4])
        scanI(I[cardnum][3])
        scanG(G[cardnum][1])
        scanO(O[cardnum][0])
        return True
    elif "V" in card:
        cardnum = int(list(card)[2])-1 #Checks what card the player wants to bingo on
        testV = list(card)[0]
        testV = lists[testV]
        for i in range(len(testV[0])): 
            testV[cardnum][i] = "x"
        return True
    elif "H" in card:
        cardnum = int(list(card)[2])-1 #Checks what card the player wants to bingo on
        testH = int(list(card)[1]) - 1
        for char in "BINGO":
            charL = lists[char]
            for i in range(len(charL[cardnum])):
                charL[cardnum][testH] = "x"
        return True
    elif "black" in card:
        cardnum = int(card.split()[1])-1 #Checks what card the player wants to bingo on
        for char in "BINGO":
            charL = lists[char]
            for y in range(len(charL[cardnum])):
                charL[cardnum][y] = "x"
        return True
    else:
        return False #Tells the main program that the player did not type any of the test codes


if __name__ == "__main__":
    main() #Starts the program
