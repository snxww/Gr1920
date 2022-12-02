class animal:

    def __init__(self, name, age, height ):
        self.name = name
        self.age = age
        self.height = height
        print('Создался объект животное')



am1 = animal(name='Dog', age=4, height=75 )
am2 = animal(name='Cat', age=2, height=24 )
print(am1.name)
print(am2.name)
print(am1.height)
print(am2.height)



class car:

    def __init__(self, name, hp, height ):
        self.name = name
        self.hp = hp
        self.height = height
        print('Создался объект машина')



cr1 = car(name='Vaz 2101', hp=69, height=1440 )
cr2 = car(name='BMW X5', hp=390, height=1770 )
print(cr1.name)
print(cr2.name)
print(cr1.hp)
print(cr2.hp)
print(cr1.height)
print(cr2.height)
