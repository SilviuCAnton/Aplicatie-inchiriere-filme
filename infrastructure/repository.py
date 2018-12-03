'''
Created on Nov 8, 2018

Modul pentru modul de stocare a datelor (repository)

@author: Silviu Anton
'''
from errors_tests.errors import DuplicateError, IdNotFoundError
from domain.entities import Client, Rent, Movie
import datetime

class MemoryRepository:
    
    def __init__(self, validator):
        self._items = {}
        self.__validator = validator
        
    def get_all(self):
        '''
        Description: returneaza o lista cu toate elementele din repository
        '''
        return list(self._items.values())
    
    def store(self, ID, item):
        '''
        Description: memoreaza o entitate in repository
        
        Exceptions: ridica DuplicateError daca exista deja elementul
        '''
        if ID in self._items:
            raise DuplicateError("Elementul exista deja in repository!!!")
        
        self.__validator.validate(item)
        self._items[ID] = item
        
    def delete(self, ID):
        '''
        Description: sterge o entitate din repository
        
        Exceptions: ridica IdNotFoundError daca nu exista id-ul cautat
        '''
        if ID not in self._items.keys():
            raise IdNotFoundError("Nu exista id-ul cautat!!!")
        self._items.pop(ID)
    
    def getItem(self, ID):
        '''
        Description: returneaza item-ul cu id-ul introdus
        
        In:
            - ID - id-ul entitatii
        
        Exceptions: ridica IdNotFoundError daca nu exista elementul cautat
        '''
        if ID not in self._items.keys():
            raise IdNotFoundError("Nu exista elementul cautat!!!")
        return self._items[ID]
    
    def update(self, item):
        '''
        Description: actualizeaza un element din repository
        '''
        self.__validator.validate(item)
        self._items[item.getID()] = item
        
    def size(self):
        '''
        Description: returneaza cate entitati sunt in repository
        '''
        return len(self._items)
    
    def getLastID(self):
        '''
        Description: returneaza ultimul ID din repository
        '''
        maxID = 0
        for ID in self._items.keys():
            if maxID < ID:
                maxID = ID
        return maxID
    

class FileRepository(MemoryRepository):
    
    def __init__(self, fileName, validator, Class):
        MemoryRepository.__init__(self, validator)
        self.__fileName = fileName
        self.__class = Class 
        self.__isLoaded = False
        
    def get_all(self):
        if self.__isLoaded == False:
            self.__loadFromFile()
            self.__isLoaded = True
        return MemoryRepository.get_all(self)
    
    def delete(self, ID):
        if self.__isLoaded == False:
            self.__loadFromFile()
            self.__isLoaded = True
        MemoryRepository.delete(self, ID)
        self.__storeToFile()
    
    def getItem(self, ID):
        if self.__isLoaded == False:
            self.__loadFromFile()
            self.__isLoaded = True
        return MemoryRepository.getItem(self, ID)  
    
    def size(self):
        if self.__isLoaded == False:
            self.__loadFromFile()
            self.__isLoaded = True
        return MemoryRepository.size(self)  
    
    def store(self, ID, item):
        if self.__isLoaded == False:
            self.__loadFromFile()
            self.__isLoaded = True
        MemoryRepository.store(self, ID, item)
        self.__storeToFile()
        
    def update(self, item):
        if self.__isLoaded == False:
            self.__loadFromFile()
            self.__isLoaded = True
        MemoryRepository.update(self, item)
        self.__storeToFile()
        
    def getLastID(self):
        if self.__isLoaded == False:
            self.__loadFromFile()
            self.__isLoaded = True
        
        maxKey = 0    
        for key in self._items.keys():
            if key>maxKey:
                maxKey = key
        return maxKey

    def __loadFromFile(self):
        with open(self.__fileName, 'r') as file:
            
            for line in file:
                attr1, attr2, attr3, attr4 = line.split('|')
                attr1 = int(attr1)
                if self.__class == Client:
                    attr4 = int(attr4)
                myObject = self.__class(attr1, attr2, attr3, attr4)
                self._items[myObject.getID()] = myObject
                
    def __storeToFile(self):
        with open(self.__fileName, 'w') as file:
            
            for key in self._items:
                file.write(str(key))
                file.write('|')
                file.write(str(self._items[key].getAttr1()))
                file.write('|')
                file.write(str(self._items[key].getAttr2()))
                file.write('|')
                file.write(str(self._items[key].getAttr3()))
                file.write('\n')

class RentFileRepository(MemoryRepository):
    
    def __init__(self, fileName, validator, clientRepository, movieRepository):
        MemoryRepository.__init__(self, validator)
        self.__fileName = fileName
        self.__isLoaded = False
        self.__clientRepository = clientRepository
        self.__movieRepository = movieRepository
        
    def get_all(self):
        if self.__isLoaded == False:
            self.__loadFromFile()
            self.__isLoaded = True
        return MemoryRepository.get_all(self)
    
    def delete(self, ID):
        if self.__isLoaded == False:
            self.__loadFromFile()
            self.__isLoaded = True
        MemoryRepository.delete(self, ID)
        self.__storeToFile()
    
    def getItem(self, ID):
        if self.__isLoaded == False:
            self.__loadFromFile()
            self.__isLoaded = True
        return MemoryRepository.getItem(self, ID)  
    
    def size(self):
        if self.__isLoaded == False:
            self.__loadFromFile()
            self.__isLoaded = True
        return MemoryRepository.size(self)  
    
    def store(self, ID, item):
        if self.__isLoaded == False:
            self.__loadFromFile()
            self.__isLoaded = True
        MemoryRepository.store(self, ID, item)
        self.__storeToFile()
        
    def update(self, item):
        if self.__isLoaded == False:
            self.__loadFromFile()
            self.__isLoaded = True
        MemoryRepository.update(self, item)
        self.__storeToFile()
        
    def getLastID(self):
        if self.__isLoaded == False:
            self.__loadFromFile()
            self.__isLoaded = True
        
        maxKey = 0    
        for key in self._items.keys():
            if key>maxKey:
                maxKey = key
        return maxKey
        
    def __storeToFile(self):
        with open(self.__fileName, 'w') as file:
            
            for rentID in self._items:
                file.write(str(rentID))
                file.write('|')
                file.write(str(self._items[rentID].getClient().getID()))
                file.write('|')
                file.write(str(self._items[rentID].getMovie().getID()))
                file.write('|')
                file.write(str(self._items[rentID].getDate()))
                file.write('\n')

    def __getClientAndMovieFromID(self, clientID, movieID):
        
        nullClient = Client(0, "0", "0", 0)
        nullMovie = Movie(0, "0", "0", "0")
        client = nullClient
        movie = nullMovie
        
        for repoClient in self.__clientRepository.get_all():
            if int(clientID) == int(repoClient.getID()):
                client = repoClient
                
        for repoMovie in self.__movieRepository.get_all():
            if int(movieID) == int(repoMovie.getID()):
                movie = repoMovie
        
        if client == nullClient or movie == nullMovie:
            raise IdNotFoundError("Clientul sau filmul din contract nu exista")
        
        return client, movie
                
    def __loadFromFile(self):
        with open(self.__fileName, 'r') as file:
            
            for line in file:
                attrs = line.split('|')
                rentID = int(attrs[0])
                clientID = int(attrs[1])
                movieID = int(attrs[2])
                
                dateList = []
                for item in attrs[3].split('-'):
                    dateList.append(int(item))
                date = datetime.date(dateList[0], dateList[1], dateList[2])
                
                client, movie = self.__getClientAndMovieFromID(clientID, movieID)
                
                self._items[rentID] = Rent(rentID, client, movie, date)
                
                
        