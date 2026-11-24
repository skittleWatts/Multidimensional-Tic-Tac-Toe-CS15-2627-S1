from functions import display_grid, determine_winner

grid = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]

]
turn = "X"
acceptable = ["top left", "top middle", "top right", "middle left", "middle middle", "middle right", "bottom left", "bottom middle", "bottom right"]

while True:
    if determine_winner(grid) not in ["X", "O", "Tie"]:
        display_grid(grid)
        print(f"It is {turn}'s turn!")
        while True:
            user_choice = input("""Where would you like to go? To choose, just type the row you would like to go in then the column, for 
    example: "middle middle" or "bottom right". Enter here: """).lower().strip()
            if user_choice in acceptable:
                break
            else:
                print("Please enter a valid choice.")
        if user_choice == "top left":
            if grid[0][0] == " ":
                if turn == "X":
                    grid[0][0] = "X"
                    turn = "O"
                elif turn == "O":
                    grid[0][0] = "O"
                    turn = "X"
            else:
                print("This square is already filled!")
        elif user_choice == "top middle":
            if grid[0][1] == " ":
                if turn == "X":
                    grid[0][1] = "X"
                    turn = "O"
                elif turn == "O":
                    grid[0][1] = "O"
                    turn = "X"
            else:
                print("This square is already filled!")
        elif user_choice == "top right":
            if grid[0][2] == " ":
                if turn == "X":
                    grid[0][2] = "X"
                    turn = "O"
                elif turn == "O":
                    grid[0][2] = "O"
                    turn = "X"
            else:
                print("This square is already filled!")
        elif user_choice == "middle left":
            if grid[1][0] == " ":
                if turn == "X":
                    grid[1][0] = "X"
                    turn = "O"
                elif turn == "O":
                    grid[1][0] = "O"
                    turn = "X"
            else:
                print("This square is already filled!")
        elif user_choice == "middle middle":
            if grid[1][1] == " ":
                if turn == "X":
                    grid[1][1] = "X"
                    turn = "O"
                elif turn == "O":
                    grid[1][1] = "O"
                    turn = "X"
            else:
                print("This square is already filled!")
        elif user_choice == "middle right":
            if grid[1][2] == " ":
                if turn == "X":
                    grid[1][2] = "X"
                    turn = "O"
                elif turn == "O":
                    grid[1][2] = "O"
                    turn = "X"
            else:
                print("This square is already filled!")
        elif user_choice == "bottom left":
            if grid[2][0] == " ":
                if turn == "X":
                    grid[2][0] = "X"
                    turn = "O"
                elif turn == "O":
                    grid[2][0] = "O"
                    turn = "X"
            else:
                print("This square is already filled!")
        elif user_choice == "bottom middle":
            if grid[2][1] == " ":
                if turn == "X":
                    grid[2][1] = "X"
                    turn = "O"
                elif turn == "O":
                    grid[2][1] = "O"
                    turn = "X"
            else:
                print("This square is already filled!")
        elif user_choice == "bottom right":
            if grid[2][2] == " ":
                if turn == "X":
                    grid[2][2] = "X"
                    turn = "O"
                elif turn == "O":
                    grid[2][2] = "O"
                    turn = "X"
            else:
                print("This square is already filled!")
    else:
        break

display_grid(grid)
print(f"{determine_winner(grid)} is the winner!")
