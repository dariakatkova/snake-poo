import tkinter as tk
from S07_TP14_01 import *
from S07_TP15 import PlanetTk
import keyboard
import time

class Food(Resource):
    """
    Une pomme va apparaittre dans une celulle non occupée
    """
    def __init__(self, lines_count, columns_count, cell_size):
        Resource.__init__(self, "🟥")

        x = random.randint(0, columns_count - 1)
        y = random.randint(0, lines_count - 1)

        self.__coordinates = [x, y]

    def get_coordinates(self):
        return self.__coordinates

class Obstacle(Element):
    """
    An obstacle. When the snake touches it, it dies.
    """
    def __init__(self, lines_count, columns_count):
        Element.__init__(self, "⬛️")

        x = random.randint(0, columns_count - 1)
        y = random.randint(0, lines_count - 1)

        self.__coordinates = [x, y]

    def get_coordinates(self):
        return self.__coordinates


class Snake(Animal):
    """
    Un serpent qui avance et grandit quand il mange des pommes. Le serpent meurt quand il touche lui-même ou un mur.
    Several animals connected into one?
    get_current_direction exists in Animal
    """
    def __init__(self):
        Animal.__init__(self, "🟩", 3)
        self.body_size = 1
        self.squares = []
        self.coordinates = []
        self.letter_repr = 'S'

        for i in range(0, self.body_size):
            self.coordinates.append([0, 0])
            self.squares.append(i)

        #self.turn()

    def turn(self):  #running with sudo failed because python3 not configured for tkinter
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

    def death(self):
        """
        if the snake collides with an object, with itself, with the border of the grid
        """
        self.char_repr = "🟧"

    def alive(self):
        self.char_repr = "🟩"

    def growth(self):
        self.body_size += 1
        #self.coordinates.append()


class SnakeGame(PlanetTk): #mechanics of the game
    __AUTHORISED_TYPES = {Ground, Snake}
    def __init__(self,root, lines_count, columns_count, cell_size=20, obstacles=False):
        PlanetTk.__init__(self, root, "Snake Game", lines_count, columns_count, {Ground, Snake, Food, Obstacle}, cell_size=cell_size)
        cell_number = self.get_cell_number_from_coordinates((lines_count-1)//2, (columns_count-1) //2)
        #PlanetTk._born(self, cell_number, Snake)

        self.obstacles = obstacles
        self.gamestatus = 1
        self.score = 0
        self.life = True
        self.lives_left = 3
        self.speed = 15
        self.snake = Snake()
        self.paused = True
        #self.food = Food(lines_count, columns_count, cell_size)
        self.__lines_count = lines_count
        self.__columns_count = columns_count
        self.coordinate_head = 0


    def pause(self):
        if keyboard.read_key() == "space" and self.paused == True:
            self.paused = True
        if keyboard.read_key() == "space" and self.paused == False:
            self.paused = False

    def move(self):
        #self.snake.turn()
        while self.life == True:
            if self.paused == False:
                direction = self.snake.get_current_direction()

                new_coordinates = [self.snake.coordinates[0][0] + direction[0],
                                self.snake.coordinates[0][1] + direction[1]]
                new_cell_number = PlanetTk.get_cell_number_from_coordinates(new_coordinates[0], new_coordinates[1])

                if 0 <= new_coordinates[0] < self.__lines_count and 0 <= new_coordinates[1] < self.__columns_count:

                    self.snake.coordinates.insert(0, new_coordinates)
                    PlanetTk.move_element(self, self.snake.coordinates[0], new_cell_number, self.snake) #old coordinates do not exist yet
                else:
                    self.lives_left -= 1
                    if self.lives_left == 0:
                        self.gamestatus = 0
                        self.snake.death()

                time.sleep(0.5)

    def restart(self):
        center = (self.__lines_count // 2-1, self.__columns_count// 2-1)
        self.coordinate_head = self.get_cell_number_from_coordinates(center[0], center[1])
        PlanetTk._born(self, self.coordinate_head, Snake)
        self.gamestatus = 1
        self.snake.alive()

    def game_over(self):
        if self.gamestatus == 0:
            self.restart()

    def start_game(self):
        while self.gamestatus == 1:
            #if self.paused == False:
                #self.move()
                self.restart()
                print(PlanetTk.__str__(self))
                print("\033", end="")
                time.sleep(0.5)

    def add_obstacles(self):
        pass

class SnakeGameWindow(tk.Toplevel):
    def __init__(self, master, **kw):
        tk.Toplevel.__init__(self, master, **kw)
        self.__master = master
        self.__game = SnakeGame(lines_count=30, columns_count=50, cell_size=20)
        self.__game.pack()
        tk.Button(self, text="Quit", command=self.destroy).pack()
        tk.Button(self, text="Pause", command=self.pause).pack()
        tk.Button(self, text="Back to menu", command=self.pause).pack()
        self.title("Snake Game")

    def pause(self):
        pass

    def back_to_menu(self):
        pass
    
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
    #MyApp().mainloop()
    ROOT = tk.Tk()
    GAME = SnakeGame(ROOT, 10, 10)
    GAME.start_game()
    print(GAME)
