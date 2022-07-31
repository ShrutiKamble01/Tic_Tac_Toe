def sum(a, b, c ):
    return a + b + c

def printBoard(x, z):
    zero = 'X' if x[0] else ('O' if z[0] else 0)
    one = 'X' if x[1] else ('O' if z[1] else 1)
    two = 'X' if x[2] else ('O' if z[2] else 2)
    three = 'X' if x[3] else ('O' if z[3] else 3)
    four = 'X' if x[4] else ('O' if z[4] else 4)
    five = 'X' if x[5] else ('O' if z[5] else 5)
    six = 'X' if x[6] else ('O' if z[6] else 6)
    seven = 'X' if x[7] else ('O' if z[7] else 7)
    eight = 'X' if x[8] else ('O' if z[8] else 8)
    print(f"{zero} | {one} | {two} ")
    print(f"--|---|---")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight} ") 

def checkWin(x, z):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if(sum(x[win[0]], x[win[1]], x[win[2]]) == 3):
            print("X Won the match")
            return 1
        if(sum(z[win[0]], z[win[1]], z[win[2]]) == 3):
            print("O Won the match")
            return 0
    return -1
    
if __name__ == "__main__":
    x = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    z = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1 # 1 for X and 0 for O
    print("Welcome to Tic Tac Toe")
    while(True):
        printBoard(x, z)
        if(turn == 1):
            print("X's Chance")
            value = int(input("Please enter a value: "))
            x[value] = 1
        else:
            print("O's Chance")
            value = int(input("Please enter a value: "))
            z[value] = 1
        cwin = checkWin(x, z)
        if(cwin != -1):
            print("Match over")
            break
        
        turn = 1 - turn