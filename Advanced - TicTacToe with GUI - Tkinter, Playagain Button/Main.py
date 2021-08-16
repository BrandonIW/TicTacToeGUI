from tkinter import *
import random
from tkinter import messagebox

class TikTacToe:

    players = ["X","O"]

    def __init__(self):
        #### Define 2D list of buttons
        self.buttons = [[0,0,0],
                        [0,0,0],
                        [0,0,0]]

        #### Define our window
        self.window = Tk()
        self.window.title("Tik-Tac-Toe")
        self.window.geometry("500x500")

        #### Define Label
        self.player = random.choice(TikTacToe.players)
        self.label = Label(text= self.player + " turn", font=('consolas',40))
        self.label.pack(side="top")

        #### Define reset button
        self.reset_button = Button(text="Restart Game", font=('consolas',20), command=self.new_game)
        self.reset_button.pack(side="top")

        #### Define frame
        self.frame=Frame(self.window)
        self.frame.pack()

        #### Define buttons

        for row in range(3):
            for column in range(3):
                 self.buttons[row][column] = Button(self.frame,text="",height=4,width=9,font=35,
                                                        command=lambda row=row,column=column:self.next_turn(row,column))
                 self.buttons[row][column].grid(row=row,column=column)


        self.window.mainloop()

    def next_turn(self,row,column):
        #### Checks to see if the current button we've selected is empty and there's no winner
        if self.buttons[row][column]['text'] == "" and self.check_winner() is False:

            #### If the above is True, check and see who's the current player and edit the text of the button to that player
            if self.player == TikTacToe.players[0]:
                self.buttons[row][column]['text'] = self.player

                #### Then check and see if there's a winner. If not, change the player
                if self.check_winner() is False:
                    self.player = TikTacToe.players[1]
                    self.label.config(text=(TikTacToe.players[1] +" turn"))

                #### If there is a winner ask to play again
                elif self.check_winner() is True:
                    self.label.config(text=TikTacToe.players[0] +" wins")
                    self.play_again()

            #### If the above is True, check and see who's the current player and edit the text of the button to that player
            elif self.player == TikTacToe.players[1]:
                self.buttons[row][column]['text'] = self.player

                #### Then check and see if there's a winner. If not, change the player
                if self.check_winner() is False:
                    self.player = TikTacToe.players[0]
                    self.label.config(text=(TikTacToe.players[0] +" turn"))

                #### If there is a winner ask to play again
                elif self.check_winner() is True:
                    self.label.config(text=TikTacToe.players[0] +" wins")
                    self.play_again()


    def check_winner(self):
        for row in range(3):
            if self.buttons[row][0]['text'] == self.buttons[row][1]['text'] == self.buttons[row][2]['text'] != "":
                self.buttons[row][0].config(bg='green')
                self.buttons[row][1].config(bg='green')
                self.buttons[row][2].config(bg='green')
                return True

        for column in range(3):
            if self.buttons[0][column]['text'] == self.buttons[1][column]['text'] == self.buttons[2][column]['text'] != "":
                self.buttons[0][column].config(bg='green')
                self.buttons[1][column].config(bg='green')
                self.buttons[2][column].config(bg='green')
                return True

        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != "":
            self.buttons[0][0].config(bg='green')
            self.buttons[1][1].config(bg='green')
            self.buttons[2][2].config(bg='green')
            return True

        if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != "":
            self.buttons[0][2].config(bg='green')
            self.buttons[1][1].config(bg='green')
            self.buttons[2][0].config(bg='green')
            return True

        elif self.empty() is False:
            return "Tie"

        return False

    def empty(self):
        spaces = 9

        for row in range(3):
            for column in range(3):
                if self.buttons[row][column]['text'] != "":
                    spaces -= 1

        if spaces == 0:
            return False

        else:
            return True

    def new_game(self):
        self.player = random.choice(TikTacToe.players)
        self.label.config(text=self.player+" turn")
        for row in range(3):
            for column in range(3):
                self.buttons[row][column].config(text="",bg="#F0F0F0")

    def play_again(self):
        if messagebox.askyesno(title="Game Over",message="Play again?"):
            self.new_game()
        else:
            quit()


if __name__ == '__main__':
     game = TikTacToe()


