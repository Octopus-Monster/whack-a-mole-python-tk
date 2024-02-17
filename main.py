import tkinter as tk
import random
from tkinter import messagebox
from PIL import Image, ImageTk

class WhackAMoleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("打地鼠游戏")

        self.score = 0
        self.time_remaining = 60
        self.moles = []

        self.create_widgets()
        self.disable_buttons()

    def create_widgets(self):
        self.score_label = tk.Label(self.root, text="分数: 0")
        self.score_label.grid(row=0, column=0, padx=10, pady=10)

        self.time_label = tk.Label(self.root, text="倒计时: 60秒")
        self.time_label.grid(row=0, column=1, padx=10, pady=10)

        self.start_button = tk.Button(self.root, text="开始游戏", command=self.start_game)
        self.start_button.grid(row=0, column=2, padx=10, pady=10)

        self.buttons = []
        for i in range(5):
            row_buttons = []
            for j in range(5):
                button = tk.Button(self.root, width=300, height=300, state=tk.DISABLED, command=lambda i=i, j=j: self.button_click(i, j))
                button.grid(row=i+1, column=j, padx=5, pady=5)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

        # Load images
        self.hole_image = ImageTk.PhotoImage(Image.open("pic\\hole.png"))
        self.mole_image = ImageTk.PhotoImage(Image.open("pic\\mole.png"))
        self.hit_mole_image = ImageTk.PhotoImage(Image.open("pic\\hit_mole.png"))
        self.rabbit_image = ImageTk.PhotoImage(Image.open("pic\\rabbit.png"))
        self.hit_rabbit_image = ImageTk.PhotoImage(Image.open("pic\\hit_rabbit.png"))

    def disable_buttons(self):
        for row in self.buttons:
            for button in row:
                button.config(state=tk.DISABLED)

    def enable_buttons(self):
        for row in self.buttons:
            for button in row:
                button.config(state=tk.NORMAL)

    def start_game(self):
        self.score = 0
        self.update_score_label()
        self.time_remaining = 60
        self.update_time_label()
        self.enable_buttons()
        self.root.after(1000, self.update_time)
        self.moles = [[0 for _ in range(5)] for _ in range(5)]
        self.update_moles()

    def update_time(self):
        self.time_remaining -= 1
        self.update_time_label()
        if self.time_remaining > 0:
            self.root.after(1000, self.update_time)
            self.update_moles()
        else:
            self.disable_buttons()
            messagebox.showinfo("游戏结束", f"游戏结束！你的得分是 {self.score} 分")

    def update_time_label(self):
        self.time_label.config(text=f"倒计时: {self.time_remaining}秒")

    def update_score_label(self):
        self.score_label.config(text=f"分数: {self.score}")

    def update_moles(self):
        for i in range(5):
            for j in range(5):
                if self.moles[i][j] == 0:
                    self.buttons[i][j].config(image=self.hole_image, state=tk.NORMAL)
                elif self.moles[i][j] == 1:
                    self.buttons[i][j].config(image=self.mole_image, state=tk.NORMAL)
                elif self.moles[i][j] == 2:
                    self.buttons[i][j].config(image=self.hit_mole_image, state=tk.NORMAL)
                elif self.moles[i][j] == 3:
                    self.buttons[i][j].config(image=self.rabbit_image, state=tk.NORMAL)
                elif self.moles[i][j] == 4:
                    self.buttons[i][j].config(image=self.hit_rabbit_image, state=tk.NORMAL)

        self.root.after(500, self.update_moles_random)

    def update_moles_random(self):
        for i in range(5):
            for j in range(5):
                if random.random() < 0.2:
                    self.moles[i][j] = random.choice([1, 3])
                else:
                    self.moles[i][j] = 0
        self.update_moles()

    def button_click(self, row, col):
        button_state = self.moles[row][col]
        if button_state == 1:
            self.moles[row][col] = 2
            self.score += 5
            self.update_score_label()
        elif button_state == 3:
            self.moles[row][col] = 4
            self.score -= 10
            self.update_score_label()

        self.update_moles()

if __name__ == "__main__":
    root = tk.Tk()
    game = WhackAMoleGame(root)
    root.mainloop()
