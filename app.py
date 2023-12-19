from game_color import *
from gui import *
import tkinter as tk
import random 


#placar
frame_score(self) = tk.Frame(self)
frame_score.place(relx=0.5, y =60, anchor = "center")
tk.Label(
    frame_score,
    text = "PLACAR",
    font = Game.Font_ScoreLabel
).grid(row=0)

self.label_score = tk.Label(frame_score, text="0", Game.Font_Score)
self.label_score.grid(row=1)



#mecanica jogo
class Game (tk.Frame):
    def init_game(self):
        tk.Frame.init_game(self)
        self.grid()
        self.master.title("2048 de Daniel Lourenço Affonso")

        self..grid_main = tk.Frame(

            self bg = Game.Color_grid, bd= 4, width 600, heigth 600
        )
        self.GUI_maker()
        self.start_game()
        

        self.master.bind("< Esquerda >", self.left)
        self.master.bind("< Direita >", self.right)
        self.master.bind("< Baixo ", self.down)
        self.master.bind("< Cima >", self.up)


        self.mainloop()




def start_game():
    self.matrix[[0]*4 for in_range(4)]

    row = self

matrix_row = []
matrix_line= []