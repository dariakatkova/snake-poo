from S05_TP09_01_template import *
import random


class PlanetAlpha(Grid):
    NORTH, EAST, SOUTH, WEST = (-1, 0), (0, 1), (1, 0), (0, -1)
    NORTH_EAST, SOUTH_EAST, SOUTH_WEST, NORTH_WEST = (-1, 1), (1, 1), (1, -1), (-1, -1)
    CARDINAL_POINTS = (NORTH, EAST, SOUTH, WEST)
    WIND_ROSE = (NORTH, NORTH_EAST, EAST, SOUTH_EAST, SOUTH, SOUTH_WEST, WEST, NORTH_WEST)

    def __init__(self, name, latitude_cells_count, longitude_cells_count, ground):
        self.__name = name
        self.__ground = ground
        self.__grid = [[ground for i in range(longitude_cells_count)] for j in range(latitude_cells_count)]
        self.__lines_count = latitude_cells_count
        self.__columns_count = longitude_cells_count
        Grid.__init__(self, self.__grid)




    def get_name(self):
        return self.__name

    def get_ground(self):
        return self.__ground

    def get_random_free_place(self):
        if self.get_count(self.__ground)!=0:
            i = random.randint(0, self.__lines_count - 1)
            j = random.randint(0, self.__columns_count - 1)
            if self.__grid[i][j] == self.__ground:
                return self.get_cell_number_from_coordinates(i, j)
            else:
                return self.get_random_free_place()
        return -1

    def born(self,cell_number, element):
        coord=self.get_coordinates_from_cell_number(cell_number)
        if self.__grid[coord[0]][coord[1]] == self.__ground:
            self.__grid[coord[0]][coord[1]] = element
            return 1
        return 0

    def die(self,cell_number):
        coord = self.get_coordinates_from_cell_number(cell_number)
        if self.__grid[coord[0]][coord[1]] != self.__ground:
            self.__grid[coord[0]][coord[1]] = self.__ground
            return 1
        return 0

    def __repr__(self):

        return f"{self.__name} ({self.get_lines_count()*self.get_columns_count()-self.get_count(self.__ground)} habitants )\n" + '\n'.join(self.get_line_str(line_number, "\t") for line_number in range(self.__lines_count))



if __name__ == '__main__':
    random.seed(10)
    PLANET_TEST= PlanetAlpha("Terre",5,10,".")
    INHABITANT_TEST= {"D":7,"C":3}
    RESOURCES_TEST={"E":10,"H":20}
    print(PLANET_TEST)
    for letter , letter_count in INHABITANT_TEST.items():
        for i in range(letter_count):
            PLANET_TEST.born(PLANET_TEST.get_random_free_place(),letter)
    print(PLANET_TEST)
    for letter, letter_count in RESOURCES_TEST.items():
        for i in range(letter_count):
            PLANET_TEST.born(PLANET_TEST.get_random_free_place(),letter)
    print(PLANET_TEST)
    print(PLANET_TEST.get_neighbour(0,0, PLANET_TEST.NORTH_WEST))
    print(PLANET_TEST.get_neighborhood(0,0, PLANET_TEST.CARDINAL_POINTS))
    print(PLANET_TEST.get_neighborhood(0,0, PLANET_TEST.WIND_ROSE))
    PLANET_TEST.die(0)
    for cell in PLANET_TEST.get_cell_neighborhood_numbers(0, PLANET_TEST.WIND_ROSE):
        PLANET_TEST.die(cell)
    print(PLANET_TEST)
    print(PLANET_TEST.get_neighborhood(0,0, PLANET_TEST.WIND_ROSE))
    assert PLANET_TEST.get_neighborhood(0,0, PLANET_TEST.WIND_ROSE) == ['.', '.', '.', '.', '.', '.', '.', '.']
    print("Test OK")