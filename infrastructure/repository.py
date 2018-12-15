'''
Created on Nov 8, 2018

Modul pentru modul de stocare a datelor (repository)

@author: Silviu Anton
'''
from errors_tests.errors import DuplicateError, IdNotFoundError
from domain.entities import Client, Rent, Movie
import datetime

# class MemoryRepository:
#      
#     def __init__(self, validator):
#         self._items = {}
#         self.__validator = validator
#          
#     def get_all(self):
#         '''
#         Description: returneaza o lista cu toate elementele din repository
#         '''
#         return list(self._items.values())
#      
#     def store(self, item):
#         '''
#         Description: memoreaza o entitate in repository
#          
#         Exceptions: ridica DuplicateError daca exista deja elementul
#         '''
#         if item.getID() in self._items:
#             raise DuplicateError("Elementul exista deja in repository!!!")
#          
#         self.__validator.validate(item)
#         self._items[item.getID()] = item
#          
#     def delete(self, ID):
#         '''
#         Description: sterge o entitate din repository
#          
#         Exceptions: ridica IdNotFoundError daca nu exista id-ul cautat
#         '''
#         if ID not in self._items.keys():
#             raise IdNotFoundError("Nu exista id-ul cautat!!!")
#         self._items.pop(ID)
#      
#     def getItem(self, ID):
#         '''
#         Description: returneaza item-ul cu id-ul introdus
#          
#         In:
#             - ID - id-ul entitatii
#          
#         Exceptions: ridica IdNotFoundError daca nu exista elementul cautat
#         '''
#         if ID not in self._items.keys():
#             raise IdNotFoundError("Nu exista elementul cautat!!!")
#         return self._items[ID]
#      
#     def update(self, item):
#         '''
#         Description: actualizeaza un element din repository
#         '''
#         self.__validator.validate(item)
#         self._items[item.getID()] = item
#          
#     def size(self):
#         '''
#         Description: returneaza cate entitati sunt in repository
#         '''
#         return len(self._items)
#      
#     def getLastID(self):
#         '''
#         Description: returneaza ultimul ID din repository
#         '''
#         maxID = 0
#         for ID in self._items.keys():
#             if maxID < ID:
#                 maxID = ID
#         return maxID
#      

class FileRepository:
    
    def __init__(self, fileName, Class):
        self.__fileName = fileName
        self.__class = Class 
        
    def get_all(self):
        '''
        Description: returneaza o lista cu toate elementele din fisier
        '''
        itemList = []
        
        with open(self.__fileName, 'r') as file:
            for line in file:
                if line.strip() == "":
                    pass
                else:
                    attr1, attr2, attr3, attr4 = line.split('|')
                    attr1 = int(attr1)
                    attr4 = attr4.strip()
                    if self.__class == Client:
                        attr4 = int(attr4)
                    myObject = self.__class(attr1, attr2, attr3, attr4)
                    itemList.append(myObject)
        return itemList
    
    def clearFile(self):
        with open(self.__fileName, 'w'):
            pass
    
    def delete(self, ID):
        '''
        Description: sterge un element din fisier
        '''
        itemList = self.get_all()
        
        with open(self.__fileName, 'w'):
            pass
        
        for item in itemList:
            if item.getID() != ID:
                self.__storeToFile(item)
    
    def getItem(self, ID, index = 0):    
        '''
        Description: gaseste un element dupa ID din fisier + implementare recursive
        '''
#         itemList = self.get_all()
#          
#         for item in itemList:
#             if item.getID() == ID:
#                 return item
#          
#         raise IdNotFoundError("Nu exista elementul cautat!!!")
    
        itemList = self.get_all()
        if index == len(itemList):
            raise IdNotFoundError("Nu exista elementul cautat!!!")
        if itemList[index].getID() == ID:
            return itemList[index]
        return self.getItem(ID, index+1)
        
    def size(self):
        '''
        Description: returneaza cate elemente sunt in fisier
        '''
        itemList = self.get_all()
        return len(itemList)
    
    def store(self, item):
        '''
        Description: memoreaza un element in fisier
        '''
        itemList = self.get_all()    
        if item in itemList:
            raise DuplicateError("Elementul exista deja in repository!!!")
        
        self.__storeToFile(item)
        
    def update(self, item):     
        '''
        Description: update-aza un element din fisier
        '''   
        self.delete(item.getID())
        self.__storeToFile(item)
        
    def getLastID(self): 
        '''
        Description: returneaza cel mai mare id din fisier
        '''
        itemList = self.get_all()
        maxKey = 0    
        for item in itemList:
            if item.getID()>maxKey:
                maxKey = item.getID()
        return maxKey
               
    def __storeToFile(self, item):
        with open(self.__fileName, 'a') as file:
            file.write("\n")
            file.write(str(item.getID()))
            file.write('|')
            file.write(str(item.getAttr1()))
            file.write('|')
            file.write(str(item.getAttr2()))
            file.write('|')
            file.write(str(item.getAttr3()))                                    

class RentFileRepository:
    
    def __init__(self, fileName):
        self.__fileName = fileName
        
    def get_all(self):
        '''
        Description: returneaza o lista cu toate elementele din fisier
        '''
        rentList = []
        
        with open(self.__fileName, 'r') as file:
            for line in file:
                if line.strip() == "":
                    pass
                else:
                    rentID, clientID, movieID, dateString = line.split('|')
                    rentID = int(rentID)
                    clientID = int(clientID)
                    movieID = int(movieID)
                    
                    dateList = []
                    for item in dateString.split('-'):
                        dateList.append(int(item))
                    date = datetime.date(dateList[0], dateList[1], dateList[2])
                    
                    rentTuple = (rentID, clientID, movieID, date)
                    rentList.append(rentTuple)
                
        return rentList
    
    def clearFile(self):
        with open(self.__fileName, 'w'):
            pass
    
    def delete(self, ID):
        '''
        Description: sterge un element din fisier
        '''
        rentTuples = self.get_all()
        
        with open(self.__fileName, 'w') as file:
            for rentTuple in rentTuples:
                if rentTuple[0] != ID:
                    file.write('\n')
                    file.write(str(rentTuple[0]))
                    file.write('|')
                    file.write(str(rentTuple[1]))
                    file.write('|')
                    file.write(str(rentTuple[2]))
                    file.write('|')
                    file.write(str(rentTuple[3]))
    
    def getItem(self, ID):    
        '''
        Description: gaseste un element dupa ID din fisier
        '''
        rentTuples = self.get_all()
         
        for rentTuple in rentTuples:
            if rentTuple[0] == ID:
                return rentTuple
         
        raise IdNotFoundError("Nu exista elementul cautat!!!")
    
    def size(self):
        '''
        Description: returneaza cate elemente sunt in fisier
        '''
        itemList = self.get_all()
        return len(itemList)
    
    def store(self, rent):
        '''
        Description: memoreaza un element in fisier
        '''
        rentTuples = self.get_all()  
        for rentTuple in rentTuples:  
            if rent.getID() == rentTuple[0]:
                raise DuplicateError("Inchirierea exista deja in repository!!!")
        
        self.__storeToFile(rent)
        
    def update(self, rent):     
        '''
        Description: update-aza un element din fisier
        '''   
        self.delete(rent.getID())
        self.__storeToFile(rent)
        
    def getLastID(self): 
        '''
        Description: returneaza cel mai mare id din fisier ; rent[0] semnifica ID-ul inchirierii
        '''
        rentTuples = self.get_all()
        if rentTuples == []:
            return 0
        
        maxKey = 0    
        for rentTuple in rentTuples:
            if rentTuple[0] > maxKey:
                maxKey = rentTuple[0]
        return maxKey
                
    def __storeToFile(self, rent):
        with open(self.__fileName, 'a') as file:
                file.write('\n')
                file.write(str(rent.getID()))
                file.write('|')
                file.write(str(rent.getClient().getID()))
                file.write('|')
                file.write(str(rent.getMovie().getID()))
                file.write('|')
                file.write(str(rent.getDate()))
                