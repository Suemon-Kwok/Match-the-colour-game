import tkinter as tk
import random
import tkinter.messagebox as messagebox

class Game:
    def __init__(self, master):
        self.master = master
        self.buttons = [[None for _ in range(8)] for _ in range(8)]
        self.first_click = None
        self.colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'pink', 'cyan']
        for i in range(8):
            for j in range(8):
                self.buttons[i][j] = tk.Button(master, width=2, height=1, bg='white', command=lambda i=i, j=j: self.on_click(i, j))
                self.buttons[i][j].grid(row=i, column=j)

    def reset_color(self, i1, j1, i2, j2):
        self.buttons[i1][j1].config(bg='white')
        self.buttons[i2][j2].config(bg='white')

    def on_click(self, i, j):
        if self.buttons[i][j]['bg'] == 'white':
            color = random.choice(self.colors)
            self.buttons[i][j].config(bg=color)
            if self.first_click is None:
                self.first_click = (i, j, color)
            else:
                if self.first_click[2] == color:
                    print('You win!')
                    if messagebox.askyesno("Play Again?", "Do you want to play again?"):
                        self.reset_game()
                    else:
                        self.master.quit()
                else:
                    self.master.after(1000, self.reset_color, self.first_click[0], self.first_click[1], i, j)
                self.first_click = None

    def reset_game(self):
        for i in range(8):
            for j in range(8):
                self.buttons[i][j].config(bg='white')

root = tk.Tk()
game = Game(root)
root.mainloop()
