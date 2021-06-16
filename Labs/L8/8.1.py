from datetime import datetime

class Computer(object):
    def __init__(self, name:str='Computer', manufacturer:str=None, year:int=None, price:int=None): 
        self.__name = name
        self.__manufacturer = manufacturer
        self.__year = year
        self.__price = price

    def enter_properties(self):
        for key in vars(self):
            vars(self)[key] = input('Enter {}: '.format(key.split('__')[1]))

    def __repr__(self):
        props_str = self.__class__.__name__ + ':\n'
        for key in vars(self):
            props_str += '{}: {}\n'.format(key.split('__')[1], vars(self)[key])

        return props_str

           
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        self.__manufacturer = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if value > datetime.now().year:
            raise ValueError("{} year hasn't come yet. Unable to set as year of manufacture.".format(value))
        self._name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value


class PC(Computer):
    def __init__(self, name:str='PC', manufacturer:str=None, 
                 year:int=None, price:int=None, optical_drive:bool=True):
        super().__init__(name, manufacturer, year, price)
        self.__optical_drive = optical_drive

    @property
    def optical_drive(self):
        return self.__optical_drive

    @optical_drive.setter
    def optical_drive(self, value):
        self.__optical_drive = value

class Server(PC):
    def __init__(self, name:str='Server', manufacturer:str=None, 
                 year:int=None, price:int=None, optical_drive:bool=True, type:str=None):
        super().__init__(name, manufacturer, year, price, optical_drive)
        self.__type = type

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value

class Laptop(PC):
    def __init__(self, name:str='Laptop', manufacturer:str=None, 
                 year:int=None, price:int=None, optical_drive:bool=True, screen:float=None):
        super().__init__(name, manufacturer, year, price, optical_drive)
        self.__screen = screen

    @property
    def screen(self):
        return self.__screen

    @screen.setter
    def screen(self, value):
        self.__screen = value

choice = {
'c': Computer(),
'p': PC(),
'l': Laptop(),
's': Server()
}

obj_list = []

for _ in range(int(input('Enter number of objects: '))):
    option = input('\nChoose desired object type (computer - c, PC - p, laptop - l, server - s): ')
    obj = choice[option]
    print('\nEnter properties of a new {}:'.format(obj.__class__.__name__))
    obj.enter_properties()
    obj_list.append(obj)

for index, item in enumerate(obj_list):
    
    print('='*15, '\n{}. '.format(index+1), item, '='*15, sep='')


