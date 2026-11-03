B = []
I = []
N = []
G = []
O = []

def scanB(call):
    global B
    cards = []
    for i in range(len(B)):
        if (call in B[i]):
            cards.append(f"Card {i+1} Column B")
    return cards
def scanI(call):
    global I
    cards = []
    for i in range(len(I)):
        if (call in I[i]):
            cards.append(f"Card {i+1} Column I")
    return cards
def scanN(call):
    global N
    cards = []
    for i in range(len(N)):
        if (call in N[i]):
            cards.append(f"Card {i+1} Column N")
    return cards
def scanG(call):
    global G
    cards = []
    for i in range(len(G)):
        if (call in G[i]):
            cards.append(f"Card {i+1} Column G")
    return cards
def scanO(call):
    global O
    cards = []
    for i in range(len(O)):
        if (call in O[i]):
            cards.append(f"Card {i+1} Column O")
    return cards

def defineCards():
    global B,I,N,G,O
    loops = int(input("How many cards do you have?\n"))
    for i in range(loops):
        print(f"Please enter the B values for card {i + 1}")
        B.append([input() for _ in range(5)])
        print(f"Please enter the I values for card {i + 1}")
        I.append([input() for _ in range(5)])
        print(f"Please enter the N values for card {i + 1}")
        N.append([input() for _ in range(5)])
        print(f"Please enter the G values for card {i + 1}")
        G.append([input() for _ in range(5)])
        print(f"Please enter the O values for card {i + 1}")
        O.append([input() for _ in range(5)])
def main():
    global B
    defineCards()
    card = input("What number was called?\n")
    while(card != "quit"):
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
        card = input("What number was called?\n")
main()