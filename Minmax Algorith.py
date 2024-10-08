import tkinter as tk
from tkinter import messagebox

board = [['' for _ in range(3)] for _ in range(3)]
current_player = "X"
time_remaining = 30  # 30-second countdown

def check_winner():
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != '':
            return board[row][0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '':
        return board[0][2]
    return None

def is_full():
    for row in board:
        if '' in row:
            return False
    return True

def minimax(board, depth, is_maximizing):
    winner = check_winner()
    if winner == "X":
        return -1
    elif winner == "O":
        return 1
    elif is_full():
        return 0
    
    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ''
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ''
                    best_score = min(score, best_score)
        return best_score

def ai_move():
    best_score = -float('inf')
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = ''
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    if best_move:
        i, j = best_move
        buttons[i][j].config(text="O", state="disabled")
        board[i][j] = "O"
        if check_winner():
            messagebox.showinfo("Game Over", f"Player {check_winner()} wins!")
            root.quit()
        elif is_full():
            messagebox.showinfo("Game Over", "It's a draw!")
            root.quit()

def on_click(i, j):
    global current_player
    if board[i][j] == '' and current_player == "X":
        buttons[i][j].config(text="X", state="disabled")
        board[i][j] = "X"
        if check_winner():
            messagebox.showinfo("Game Over", f"Player {check_winner()} wins!")
            root.quit()
        elif is_full():
            messagebox.showinfo("Game Over", "It's a draw!")
            root.quit()
        else:
            current_player = "O"
            ai_move()
            current_player = "X"

def countdown():
    global time_remaining
    if time_remaining > 0:
        time_remaining -= 1
        timer_label.config(text=f"Time remaining: {time_remaining} seconds")
        root.after(1000, countdown)
    else:
        messagebox.showinfo("Time's Up", "Game Over! Time's up!")
        root.quit()

root = tk.Tk()
root.title("Tic Tac Toe")

timer_label = tk.Label(root, text=f"Time remaining: {time_remaining} seconds", font='Arial 12')
timer_label.grid(row=3, column=0, columnspan=3)

root.after(1000, countdown)

buttons = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", font='Arial 20', width=5, height=2,
                                  command=lambda i=i, j=j: on_click(i, j))
        buttons[i][j].grid(row=i, column=j)

root.mainloop()
