import tkinter as tk
from S07_TP14_01 import *
from S07_TP15 import PlanetTk
#import keyboard
import time

class Food(Resource):
    """
    Une pomme vas apparaittre dans une celulle non occupée.
    An apple that will appear randomly in a free cell.
    """
    def __init__(self, lines_count, columns_count, cell_size):
        Resource.__init__(self, "🟥")

        x = random.randint(0, columns_count - 1)
        y = random.randint(0, lines_count - 1)

        self.__coordinates = [x, y]

class Obstacle:
    pass

class Snake(Animal):
    """
    Un serpent qui avance et grandit quand il mange des pommes. Le serpent meurt quand il touche lui-même ou un mur.
    A snake that advances and grows when it eats apples. The snake dies when it touches itself or a wall.
    Several animals connected into one?
    get_current_direction exists in Animal
    """
    def __init__(self):
        Animal.__init__(self, "🟩", 3)
        self.body_size = 1
        self.squares = []
        self.coordinates = []

        for i in range(0, self.body_size):
            self.coordinates.append([0, 0])
            self.squares.append(i)

        #self.turn()

    def turn(self):
        while True:
            if keyboard.read_key() == "left":
                direction = []
                if self.get_current_direction() == [1, 1]: #snake going up
                    direction = [-1, 0]
                elif self.get_current_direction() == [0, 0]: #snake going down
                    direction = [1, 0]
                elif self.get_current_direction() == [-1, 0]: #snake going left
                    direction = [0, 0]
                else: #snake going right
                    direction = [1, 1]
                self.set_current_direction(direction[0], direction[1])

                break

            elif keyboard.read_key() == "right":
                if self.get_current_direction() == [1, 1]:  # snake going up
                    direction = [1, 0]
                elif self.get_current_direction() == [0, 0]:  # snake going down
                    direction = [-1, 0]
                elif self.get_current_direction() == [-1, 0]:  # snake going left
                    direction = [1, 1]
                else:  # snake going right
                    direction = [0, 0]
                self.set_current_direction(direction[0], direction[1])

                break


class SnakeGame(PlanetTk): #mechanics of the game
    __AUTHORISED_TYPES = {Ground, Snake}
    def __init__(self,root, lines_count, columns_count, cell_size=20, **kw): #add root
        
        PlanetTk.__init__(self, root, "Snake Game", lines_count, columns_count, {Ground, Snake, Food, Obstacle}, cell_size)
        cell_number = self.get_cell_number_from_coordinates((lines_count-1)//2, (columns_count-1) //2)
        self.add_element(cell_number, Snake())
        self.title("Snake Game")


        self.gamestatus = 1
        self.score = 0
        self.life = True
        self.lives_left = 3
        self.speed = 15
        self.snake = Snake()
        self.pause = True
        #self.food = Food(lines_count, columns_count, cell_size)
        self.__lines_count = lines_count
        self.__columns_count = columns_count

    def pause(self):
        if keyboard.read_key() == "space" and self.pause == True:
            self.pause = True
        if keyboard.read_key() == "space" and self.pause == False:
            self.pause = False
    def move(self):

        direction = self.snake.get_current_direction()

        new_coordinates = [self.snake.coordinates[0][0] + direction[0],
                                self.snake.coordinates[0][1] + direction[1]]

        if 0 <= new_coordinates[0] < self.__lines_count and 0 <= new_coordinates[1] < self.__columns_count:

            self.snake.coordinates.insert(0, new_coordinates)
            PlanetAlpha.born(self, new_coordinates, Snake())
            PlanetAlpha.die(self, self.snake.coordinates)
        else:
            self.gamestatus = 0

    def restart(self):
        pass

    def game_over(self):
        pass

class SnakeGameWindow(tk.Toplevel):
    def __init__(self, master, **kw):
        tk.Toplevel.__init__(self, master, **kw)
        self.__master = master
        self.__game = SnakeGame(30, 50, cell_size=20)
        self.__game.pack()
        tk.Button(self, text="Quit", command=self.destroy).pack()
        self.title("Snake Game")

class MyApp(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Some Planets")
        self.geometry("200x200")
        tk.Button(self, text='Conway game', command=lambda: ConwayWindow(self)).pack(side=tk.TOP)
        tk.Button(self, text='Turmites game', command=lambda: TurmitesWindow(self)).pack(side=tk.TOP)
        tk.Button(self, text='Snake game', command=lambda: SnakeGameWindow(self)).pack(side=tk.TOP)
        tk.Button(self, text='Quit', command=self.quit).pack(side=tk.TOP)


if __name__ == "__main__":
    MyApp().mainloop()
    GAME = SnakeGame(10, 10, 10)
    while GAME.gamestatus == 1:
        GAME.move()

        # Clear the terminal (for Linux/macOS/Unix)
        print("\033c", end="")  # works for linux

        # Print the updated grid
        print(GAME)

        # Wait for a short period to make movements visible
        time.sleep(0.5)
    GAME.game_over()
