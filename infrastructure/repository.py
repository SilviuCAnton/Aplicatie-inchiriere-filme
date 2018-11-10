'''
Created on Nov 8, 2018

Modul pentru modul de stocare a datelor (repository)

@author: Silviu Anton
'''

class MemoryRepository:
    
    def __init__(self, validator):
        self.__items = {}
        self.__validator = validator
        
    def get_all(self):
        return list(self.__items.values())
    
    def store(self, ID, item):
            self.__validator.validate(item)
            self.__items[ID] = item
        
    def delete(self, ID):
        if ID not in self.__items.keys():
            raise ValueError("Nu exista id-ul cautat!!!")
        self.__items.pop(ID)
    
    def getItem(self, ID):
        if ID not in self.__items.keys():
            raise ValueError("Nu exista id-ul cautat!!!")
        return self.__items[ID]
    
    def update(self, item):
        self.__validator.validate(item)
        self.__items[item.getID()] = item
        
    def size(self):
        return len(self.__items)