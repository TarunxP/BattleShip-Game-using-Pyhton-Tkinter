import tkinter as tk
import random
from tkinter import messagebox

# Create the game window
window = tk.Tk()
window.title("Battleship Game")

# Game variables
board_size = 10
board = [[" " for _ in range(board_size)] for _ in range(board_size)]
ships = {"Carrier": 5, "Battleship": 4, "Cruiser": 3, "Submarine": 3, "Destroyer": 2}

# Function to handle button click
def handle_click(row, col):
    if board[row][col] == " ":
        board[row][col] = "X"
        button = buttons[row][col]
        button.config(text="X", bg="blue")
        check_game_over()
    elif board[row][col] == "X":
        messagebox.showinfo("Invalid Move", "You have already hit that spot!")
    else:
        messagebox.showinfo("Invalid Move", "You hit a ship!")

# Function to check if the game is over
def check_game_over():
    for ship, size in ships.items():
        count = 0
        for row in board:
            count += row.count(ship[0])
        if count == size:
            del ships[ship]
            messagebox.showinfo("Ship Sunk", f"You sank the {ship}!")
            if not ships:
                messagebox.showinfo("Game Over", "Congratulations! You sank all the ships!")
                window.quit()
            break

# Create the game board buttons
buttons = []
for row in range(board_size):
    row_buttons = []
    for col in range(board_size):
        button = tk.Button(window, text=" ", width=2, bg="white",
                           command=lambda r=row, c=col: handle_click(r, c))
        button.grid(row=row, column=col, padx=1, pady=1)
        row_buttons.append(button)
    buttons.append(row_buttons)

# Randomly place ships on the board
for ship, size in ships.items():
    ship_placed = False
    while not ship_placed:
        orientation = random.choice(["horizontal", "vertical"])
        if orientation == "horizontal":
            start_row = random.randint(0, board_size - 1)
            start_col = random.randint(0, board_size - size)
            end_col = start_col + size - 1
            if all(board[start_row][c] == " " for c in range(start_col, end_col + 1)):
                for c in range(start_col, end_col + 1):
                    board[start_row][c] = ship[0]
                ship_placed = True
        else:
            start_row = random.randint(0, board_size - size)
            start_col = random.randint(0, board_size - 1)
            end_row = start_row + size - 1
            if all(board[r][start_col] == " " for r in range(start_row, end_row + 1)):
                for r in range(start_row, end_row + 1):
                    board[r][start_col] = ship[0]
                ship_placed = True

# Run the game loop
window.mainloop()
