'''
Created on Nov 8, 2018

Modul pentru modul de stocare a datelor (repository)

@author: Silviu Anton
'''
from errors_tests.errors import RepositoryError

class MemoryRepository:
    
    def __init__(self, validator):
        self.__items = {}
        self.__validator = validator
        
    def get_all(self):
        return list(self.__items.values())
    
    def store(self, ID, item):
        if ID in self.__items:
            raise RepositoryError("Clientul deja exista!!!")
        self.__validator.validate(item)
        self.__items[ID] = item
        
    def delete(self, ID):
        if ID not in self.__items.keys():
            raise RepositoryError("Nu exista id-ul cautat!!!")
        self.__items.pop(ID)
    
    def getItem(self, ID):
        if ID not in self.__items.keys():
            raise RepositoryError("Nu exista elementul cautat!!!")
        return self.__items[ID]
    
    def update(self, item):
        self.__validator.validate(item)
        self.__items[item.getID()] = item
        
    def size(self):
        return len(self.__items)
    
'''
class FileRepository:
    
    def __init__(self, fileName, validator):
        self.__fileName = fileName
        self.__validator = validator
        
    def get_all(self):
        elementList = []
        with open(self.__fileName, 'r') as file:
            for line in file:
       # fileString = file.readline()
            
                
                #elementList.append(object)
        return elementList
    '''