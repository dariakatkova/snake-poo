import random

class Element:
    def __init__(self, char_repr):
        self.char_repr  = char_repr

    def __repr__(self):
        return str(self.char_repr)

    def __eq__(self, other):
        return self.__repr__() == other.__repr__()

class Ground(Element):
    def __init__(self):
        Element.__init__(self, "🌫️")


class Resource(Element):
    def __init__(self, char_repr, value=1):
        Element.__init__(self, char_repr)
        self.__value = value

    def get_value(self):
        return self.__value


class Water(Resource):
    def __init__(self):
        Resource.__init__(self, "💧")


class Herb(Resource):
    def __init__(self):
        Resource.__init__(self, "🌱")


class Animal(Element):
    def __init__(self, char_repr, life_max):
        Element.__init__(self, char_repr)
        self.__age = 0
        self.__gender = random.randint(0, 1)
        self.__bar_life = [life_max, life_max]
        self.__current_direction =[random.randint(-1, 1),random.randint(-1, 1)]
        while self.__current_direction==[0,0]:
            self.__current_direction =[random.randint(-1, 1),random.randint(-1, 1)]
            

    def get_age(self):
        return self.__age

    def ageing(self, years=1):
        self.__age += years

    def get_gender(self):
        return self.__gender

    def get_life_max(self):
        return self.__bar_life[1]

    def get_life(self):
        return self.__bar_life[0]

    def is_alive(self):
        return self.get_life()!=0

    def is_dead(self):
        if not self.is_alive():
            return 1
        return 0

    def recovering_life(self, value):
        if self.get_life()+value>= self.get_life_max():
            self.__bar_life[0]=self.get_life_max()
        self.__bar_life[0]+=value

    def losing_life(self, value):
        if self.get_life()-value<= 0:
            self.__bar_life[0]=0
        self.__bar_life[0]-=value

    def get_current_direction(self): #(self, value)
        return self.__current_direction
        

    def set_current_direction(self, line_direction, column_direction):
        self.__current_direction = [line_direction, column_direction]
       

class Cow(Animal):
    def __init__(self):
        Animal.__init__(self, "🐮", 20)


class Dragon(Animal):
    def __init__(self):
        Animal.__init__(self, "🐉", 1000)


class Lion(Animal):
    def __init__(self):
        Animal.__init__(self, "🦁", 100)


class Mouse(Animal):
    def __init__(self):
        Animal.__init__(self, "🐭", 5)

if __name__ == "__main__":
    #ADD SEED +self.current_direction in Animal + finish class Animal
    e1 = Element("🐉")
    e2 = Element("🔮")
    assert e1.__eq__(e2) == False
    g1 = Ground()
    #print(g1)

    print(Ground(), str(Ground()))
    print(Ground() == str(Ground()))
    print(Ground() == Ground())
    print(Ground() is Ground())

    TYPES_COUNT = {Herb: 2, Water: 3, Cow: 2, Dragon: 1, Lion: 5, Mouse: 10}
    ELEMENTS_BY_TYPE = {element_type: [element_type() for _ in range(element_count)] for element_type, element_count in TYPES_COUNT.items()}
    for element_type, elements in ELEMENTS_BY_TYPE.items():
        print(element_type.__name__, elements)

    print("All tests ok")
