'''
# Q1.
class Company(object):
    def __init__(self, name):
        self.company_name = name
        
company = Company("naver")
print(company.company_name)

'''


'''
# Q2.
class Car():
    def __init__(self):
        self.model = "BEN"
    def change_model(self):
        self.model = "CAR"
    def change_model_another(self):
        self.model = "TRUCK"
        
car = Car()
car.change_model_another()
car.change_model()
print(car.model)

'''


'''
# Q3.
class House():
    def __init__(self):
        self.__door = []

'''


'''
# Q5.
class Person():
    def __init__(self):
        self.name = "SJ"
        self.age = 20
        
class Player(Person):
    pass

the_player = Player()
print(the_player.name)

'''


'''
# Q6.
import random as rd

val = rd.random()
print(val)

'''


'''
# Q7
for i in range(3):
    res_list = []
    try:
        result = 10 / i
        print(result)
        res_list.append(result)
    except ZeroDivisionError:
        print("not divided by 0")
        
'''

