import tkinter as tk
from S06_TP11 import PlanetAlpha
from S07_TP14_01 import *

class PlanetTk(PlanetAlpha, tk.Canvas):
    def __init__(self, root, name, latitude_cells_count, longtitude_cells_count, authorised_classes, background_color='white', foreground_color='dark blue', gridlines_color='maroon', cell_size=40, gutter_size=0, margin_size=0, show_content=True, show_grid_lines=True, **kw):
        PlanetAlpha.__init__(self, name, latitude_cells_count, longtitude_cells_count, Ground())
        w = longtitude_cells_count * cell_size + (longtitude_cells_count - 1) * gutter_size + 2 * margin_size
        h = latitude_cells_count * cell_size + (latitude_cells_count - 1) * gutter_size + 2 * margin_size
        tk.Canvas.__init__(self, root, width=w, height=h, background=background_color)

        self.__cell_size = cell_size
        self.__gutter_size = gutter_size
        self.__margin_size = margin_size
        self.__root = root
        self.__show_content = show_content
        self.__show_grid_lines = show_grid_lines
        self.__authorised_classes = authorised_classes
        self.__background_color  = background_color
        self.__foreground_color = foreground_color
        self.__gridlines_color = gridlines_color

        self.nb_lines = latitude_cells_count
        self.nb_columns = longtitude_cells_count

        for i in range(self.nb_lines):
            for j in range(self.nb_columns):
                x = j * (self.__cell_size + self.__gutter_size) + self.__margin_size
                y = i * (self.__cell_size + self.__gutter_size) + self.__margin_size
                cell_number = self.get_cell_number_from_coordinates(i, j)
                tag = (f"c_{cell_number}")
                self.create_rectangle(x, y, x + self.__cell_size, y + self.__cell_size, fill=self.__background_color, tags=tag)

        self.pack()

    def get_root(self):
        return self.__root

    def get_background_color(self):
        return self.__background_color

    def get_foreground_color(self):
        return self.__foreground_color

    def _born(self, cell_number, element): 
        if element in self.__authorised_classes:
            PlanetAlpha.born(self, cell_number, element())
            tag_c = f"c_{cell_number}"
            tag_t = f"t_{cell_number}"
            y, x = self.get_coordinates_from_cell_number(cell_number)
            self.create_text(x *(self.__cell_size + self.__gutter_size) + self.__cell_size // 2, y * (self.__cell_size + self.__gutter_size) + self.__cell_size // 2, text=element().letter_repr, tags=tag_t)
            self.lift(tag_t)
            self.itemconfigure(tag_c, fill=self.__background_color)
            self.itemconfigure(tag_t, fill=self.__foreground_color)
            
            
            
    def die(self, cell_number, element): # why element?
        PlanetAlpha.die(self, cell_number)
        tag_t = f"t_{cell_number}"
        self.delete(tag_t)
        

    def born_randomly(self, element):
        place = PlanetAlpha.get_random_free_place(self)
        self._born(place, element)

    def populate(self, class_names_count):
        for element, number in class_names_count.items():
            for i in range(number):
                self.born_randomly(element)

    def move_element(self, cell_number, new_cell_number, element):
        self.die(cell_number, element())
        self._born(new_cell_number, element())

    def get_classes_cell_numbers(self):
        dictionnary_classes = {}
        for i in range(self.nb_lines * self.nb_columns):
            object = PlanetAlpha.get_cell(self, i)
            class_name = object.__class__.__name__
            if class_name not in dictionnary_classes.keys():
                dictionnary_classes[class_name] = [i]
            else:
                dictionnary_classes[class_name].append(i)
        return dictionnary_classes


    def __repr__(self):  #i don't know what this is supposed to do
        return f"PlanetTk(name={PlanetAlpha.__name__}, latitude_cells_count={self.nb_lines}, longitude_cells_count={self.nb_columns})"


    def __str__(self): #prints in terminal
        return PlanetAlpha.__repr__(self)

if __name__ == "__main__":
    ROOT = tk.Tk()
    AUTHORISED_TYPES = {Ground, Water, Herb, Cow, Lion, Dragon}
    PLANET = PlanetTk(ROOT, "Terre", 10, 10, AUTHORISED_TYPES)
    assert type(PLANET.get_root()) == tk.Tk
    assert PLANET.get_background_color() == 'white'
    assert PLANET.get_foreground_color() == 'dark blue'
    PLANET._born(3, Dragon)
    #print(PLANET)
    #PLANET.die(3, Dragon)
    #print(PLANET)
    #PLANET.born_randomly(Dragon)
    #print(PLANET)
    #PLANET.populate({Dragon: 50})
    #print(PLANET)
    PLANET.move_element(3, 4, Dragon)
    #print(PLANET.get_classes_cell_numbers())
    print(PLANET)

    ROOT.mainloop()
    print("All tests Ok")
