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
        '''
        Description: returneaza o lista cu toate elementele din repository
        '''
        return list(self.__items.values())
    
    def store(self, ID, item):
        '''
        Description: memoreaza o entitate in repository
        
        Exceptions: ridica RepositoryError daca exista deja elementul
        '''
        if ID in self.__items:
            raise RepositoryError("Elementul exista deja in repository!!!")
        
        self.__validator.validate(item)
        self.__items[ID] = item
        
    def delete(self, ID):
        '''
        Description: sterge o entitate din repository
        
        Exceptions: ridica RepositoryError daca nu exista id-ul cautat
        '''
        if ID not in self.__items.keys():
            raise RepositoryError("Nu exista id-ul cautat!!!")
        self.__items.pop(ID)
    
    def getItem(self, ID):
        '''
        Description: returneaza item-ul cu id-ul introdus
        
        In:
            - ID - id-ul entitatii
        
        Exceptions: ridica RepositoryError daca nu exista elementul cautat
        '''
        if ID not in self.__items:
            raise RepositoryError("Nu exista elementul cautat!!!")
        return self.__items[ID]
    
    def update(self, item):
        '''
        Description: actualizeaza un element din repository
        '''
        self.__validator.validate(item)
        self.__items[item.getID()] = item
        
    def size(self):
        '''
        Description: returneaza cate entitati sunt in repository
        '''
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
