import random
from S06_TP11 import PlanetAlpha
from S07_TP14_01 import Ground, Water, Herb, Cow, Lion


class Main(PlanetAlpha):
    __AUTHORISED_TYPES = {Ground, Water, Herb, Cow, Lion}
    def __init__(self,planet_name, latitude_cells_count, longitude_cells_count):
        PlanetAlpha.__init__(self, planet_name, latitude_cells_count, longitude_cells_count, Ground())

        self.__planet_alpha = self
        
    def get_planet(self):
        return self.__planet_alpha

    def add_element(self, cell_number, element):
        PlanetAlpha.born(self, cell_number, element)

    def add_element_randomly(self, element):
        place = PlanetAlpha.get_random_free_place(self)
        self.add_element(place, element)

    def populate(self, types_count):
        for element_type, number in types_count.items():
            for i in range(number):
                element = element_type().__repr__()
                PlanetAlpha.born(self, PlanetAlpha.get_random_free_place(self), element)

    def __repr__(self):
        return PlanetAlpha.__repr__(self)

if __name__ == "__main__":
    random.seed(10)
    app = Main("Terre", 5, 10)
    app.populate({Lion: 7, Cow: 3})
    app.populate({Water: 10, Herb: 100})
    print(app)
    nw_neighborhood = app.get_planet().get_cell_neighborhood_numbers(0, PlanetAlpha.WIND_ROSE )
    app.get_planet().die(0)
    for cell in nw_neighborhood:
        app.get_planet().die(cell)
    print(app)
