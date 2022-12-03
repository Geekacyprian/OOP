class bsit:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value):
        self.__country = value
        
    def __repr__(self):
        return f'My name is {self.name} age is {self.age} and country is {self.country}'

bsit1 = bsit('Geeka Cyprian', 24, 'Uganda')
bsit1.name = 'Namudhasi Getrude'
bsit1.age = 26
bsit1.country = 'Uganda'

print(bsit1)



#2222222222

class bsit:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value):
        if(value not in ['Uganda', 'Kenya', 'Tanzania', 'DRC']):
            raise('Country not in East Africa')
        self.__country = value
        
    def __repr__(self):
        return f'My name is {self.name} age is {self.age} and country is {self.country}'

bsit1 = bsit('Geeka Cyprian', 24, 'Uganda')
bsit1.name = 'Namudhasi Getrude'
bsit1.age = 26
bsit1.country = 'Uganda'

print(bsit1)
