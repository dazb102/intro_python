# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 15:45:33 2017
Content: Things to do Ch6 @ Introducing Python 
@author: KimballWu
"""

#6.1
class Thing():
    pass    
print Thing
print Thing()


#6.2
class Things2():
    letters='abc'
print Things2.letters


#6.3
class Things3():
    def __init__(self, letters):
        self.letters=letters
print Things3('xyz').letters

#6.4, 6.5, 6.6, 6.7
class Element():
    def __init__(self,name,symbol,number):
        self.name=name
        self.symbol=symbol
        self.number=number
        
    def __str__(self):
        return 'name: {}\nsymbol: {}\nnumber: {}'.format(self.name, self.symbol,self.number)
        
    def dump(self):
        print 'name ' + self.name
        print 'symbol: '+ self.symbol
        print 'number: '+ str(self.number)

Element('Hydrogen','H',1)  ##6.4

print 6.5, 6.6, 6.7
a={'name':'Hydrogen','symbol':'H','number':1}
hydrogen=Element(**a) ##6.5
hydrogen.dump() ##6.6
print hydrogen  ##6.7


#6.8
class Element():
    def __init__(self,name,symbol,number):
        self.__name=name
        self.__symbol=symbol
        self.__number=number
    @property
    def name(self):
        return(self.__name)
    @property
    def symbol(self):
        return(self.__symbol)
    @property
    def number(self):
        return(self.__number)
        
#6.9
class Bear():
    @classmethod
    def eats(cls):
        return 'berries'
        
class Rabbit():
    @classmethod
    def eats(cls):
        return 'colver'

class Octothorpe():
    @classmethod
    def eats(cls):
        return 'campers'

Bear().eats()
Rabbit().eats()
Octothorpe.eats()


#6.10
class Laser():
    @staticmethod
    def does():
        return 'disintegrated'

class Claw():
    @staticmethod
    def does():
        return 'crush'
        
class SmartPhone():
    @staticmethod
    def does():
        return 'ring'

class Robot():
    def __init__(self,laser,claw,smartphone):
        self.laser=laser
        self.claw=claw
        self.smartphone=smartphone
    def does(self):
        print 'Robot does {}, {}, and {}'.format(\
        self.laser.does(), self.claw.does(), self.smartphone.does())

Robot(Laser(),Claw(),SmartPhone()).does()
