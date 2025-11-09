#Step 1: Representing the Game Board
#Step 2: Displaying the Game Board
#Step 3: Getting Player Input
#Step 4: Checking for a Winner
#Step 5: Checking for a Tie
#Step 6: The Main Game Loop
def display_board():
    print("*" * 13)
    for idx,row in enumerate(board):
        print("* " + " | ".join(row) + " *")
        print("*---|---|---*") if idx != len(board) - 1 else None
    print("*" * 13)   
def player_input(player):
    while True:
        try:
            position = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            row, col = divmod(position, 3)
            if board[row][col] == " ":
                return row, col
            else:
                print("Position already taken. Choose another.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9.")
def check_win(board, player):
    # Check rows and columns
    for i in range(3):
        if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True
    # Check diagonals
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False
def check_tie():
    return all([cell != ' ' for row in board for cell in row])
def play():
    global board
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player =  "X"
    while True:
        display_board()
        row,col = player_input(player)
        board[row][col] = player
        if check_win(board, player):
            display_board()
            print(f"Good job Player {player}, you are the winer!")
            break
        if check_tie():
            display_board()
            print("Game Over, The game is a tie!")
            break
        player = "O" if player == "X" else "X"
        display_board()
play()
