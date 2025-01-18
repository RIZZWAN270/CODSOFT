def display(frame):
    for row in frame:
        print(" | ".join(row))
        print("-" * 9)
def check(frame):
    for p in range(3):
        if frame[p][0] == frame[p][1] == frame[p][2] != " ":
            return frame[p][0]
        if frame[0][p] == frame[1][p] == frame[2][p] != " ":
            return frame[0][p]
    if frame[0][0] == frame[1][1] == frame[2][2] != " ":
        return frame[0][0]
    if frame[0][2] == frame[1][1] == frame[2][0] != " ":
        return frame[0][2]
    if all(cell != " " for row in frame for cell in row):
        return "game is draw or no possible move"
    return None
def user(frame):
    while True:
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter col (0-2): "))
            if frame[row][col] == " ":
                frame[row][col] = "X"
                break
            else:
                print("That spot is taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter numbers between 0 and 2.")
def minimax(frame, maximum):
    winner = check(frame)
    if winner == "X":
        return -1
    if winner == "O":
        return 1
    if winner == "game is draw or no possible move":
        return 0
    if maximum:
        top = float("-inf")
        for p in range(3):
            for a in range(3):
                if frame[p][a] == " ":
                    frame[p][a] = "O"
                    score = minimax(frame, False)
                    frame[p][a] = " "
                    top = max(score, top)
        return top
    else:
        top = float("inf")
        for p in range(3):
            for a in range(3):
                if frame[p][a] == " ":
                    frame[p][a] = "X"
                    score = minimax(frame, True)
                    frame[p][a] = " "
                    top = min(score, top)
        return top
def machine(frame):
    top = float("-inf")
    move = None
    for p in range(3):
        for a in range(3):
            if frame[p][a] == " ":
                frame[p][a] = "O"
                score = minimax(frame, False)
                frame[p][a] = " "
                if score > top:
                    top = score
                    move = (p, a)
    if move:
        frame[move[0]][move[1]] = "O"
def game():
    frame = [[" " for _ in range(3)] for _ in range(3)]  # Create an empty frame
    print("Welcome to Tic-Tac-Toe!")
    display(frame)

    while True:
        user(frame)
        display(frame)
        if check(frame):
            break
        machine(frame)
        display(frame)
        if check(frame):
            break
    winner = check(frame)
    if winner == "game is draw or no possible move":
        print("It's a draw!")
    else:
        print(f"The winner is {winner}!")
if __name__== "__main__":
    game()