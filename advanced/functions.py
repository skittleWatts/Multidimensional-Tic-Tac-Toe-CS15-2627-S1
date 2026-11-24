def display_grid(grid: list[list[str]]):
    """
    Displays the Tic-Tac-Toe board you input.
    :param grid: The multi-dimensional list that is a Tic-Tac-Toe board.
    :return: No return, directly prints to terminal.
    """
    print("This is the board: ")
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if j == 2:
                print(f"{grid[i][j]}")
            else:
                print(f"{grid[i][j]} | ", end= "")
        if i != 2:
            print("----------")

def determine_winner(grid: list[list[str]]):
    """
    Determines the winner from a given Tic-Tac-Toe.
    :param grid: The multi-dimensional list that is a Tic-Tac-Toe board.
    :return: Return either "X" or "O" depending on who won, returning "Tie" if it's a tie and "Not finished" if the game isn't finished.
    """
    check_list = []
    winner = ""
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            check_list.append(grid[i][j])
        if check_list[0] == check_list[1] and check_list[1] == check_list[2] and winner == "" and check_list[0] != " ":
            winner = grid[i][j]
        check_list = []

    if winner == "":
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                check_list.append(grid[j][i])
            if check_list[0] == check_list[1] and check_list[1] == check_list[2] and winner == "" and check_list[0] != " ":
                winner = grid[j][i]
            check_list = []

    if winner == "":
        if grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2] and grid[0][0] != " ":
            winner = grid[0][0]
        elif grid[0][2] == grid[1][1] and grid[1][1] == grid[2][0] and grid[0][2] != " ":
            winner = grid[0][2]

    if winner == "":
        for row in grid:
            if " " in row:
                winner = "Not finished"
        winner = "Tie"
    return winner