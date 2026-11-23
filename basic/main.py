grid_1 = [
    ["X", "X", "X"],
    ["O", "O", "X"],
    ["O", "X", "O"]
]

grid_2 = [
    ["X", "O", "X"],
    ["X", "O", "O"],
    ["O", "O", "X"]
]

grid_3 = [
    ["X", "O", "O"],
    ["O", "X", "X"],
    ["O", "X", "X"]
]

grid_4 = [
    ["X", "O", "X"],
    ["X", "O", "O"],
    ["O", "X", "X"]
]


def display_grid(grid: list[list[str]]):
    """
    Displays the Tic-Tac-Toe board you input.
    :param grid: The multi-dimensional list that is a Tic-Tac-Toe board.
    :return: No return, directly prints to terminal.
    """
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
    :return: Return either "X" or "O" depending on who won.
    """
    check_list = []
    winner = ""
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            check_list.append(grid[i][j])
        if check_list[0] == check_list[1] and check_list[1] == check_list[2] and winner == "":
            winner = grid[i][j]
        check_list = []

    if winner == "":
        for j in

    return winner

print(determine_winner(grid_3))
