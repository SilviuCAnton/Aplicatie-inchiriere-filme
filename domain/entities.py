'''
Created on Nov 6, 2018

Modul pentru entitatile din aplicatie. (Application logic)

@author: Silviu Anton
'''

class Movie:
    
    def __init__(self, ID, title, description, genre):
        self.__id = ID
        self.__title = title
        self.__description = description
        self.__genre = genre
        self.__referenceCounter = 0
        
    def __eq__(self, otherMovie):
        return self.__title == otherMovie.__title
    
    def __repr__(self):
        return "#{} {} | genre: {} | description: {}".format(self.__id, self.__title, self.__genre, self.__description)
        
    def getReferenceCounter(self):
        return self.__referenceCounter
    
    def incReferenceCounter(self):
        self.__referenceCounter += 1
        
    def decReferenceCounter(self):
        self.__referenceCounter -= 1
    
    def getID(self):
        return self.__id
        
    def getTitle(self):
        return self.__title
    
    def getAttr1(self):
        return self.getTitle()
    
    def getDescription(self):
        return self.__description
    
    def getAttr2(self):
        return self.getDescription()
    
    def getGenre(self):
        return self.__genre
    
    def getAttr3(self):
        return self.getGenre()
    
    def setTitle(self, title):
        self.__title = title
        
    def setDescription(self, description):
        self.__description = description
        
    def setGenre(self, genre):
        self.__genre = genre


class Client:
    
    def __init__(self, ID, firstName, lastName, CNP):  
        self.__id = ID
        self.__firstName = firstName
        self.__lastName = lastName
        self.__cnp = CNP
        self.__referenceCounter = 0
        
    def __eq__(self, otherClient):
        return self.__cnp == otherClient.__cnp
    
    def __repr__(self):
        return "#{} {}, CNP: {}".format(self.__id, self.getName(), self.__cnp)
    
    def getReferenceCounter(self):
        return self.__referenceCounter
    
    def incReferenceCounter(self):
        self.__referenceCounter += 1
        
    def decReferenceCounter(self):
        self.__referenceCounter -= 1
        
    def getID(self):       
        return self.__id
            
    def getName(self):
        fullName = self.__firstName + ' ' + self.__lastName
        return fullName
    
    def getAttr1(self):
        return self.__firstName
    
    def getAttr2(self):
        return self.__lastName
    
    def getCNP(self):
        return self.__cnp
    
    def getAttr3(self):
        return self.getCNP()
    
    def setName(self, firstName, lastName):
        self.__firstName = firstName
        self.__lastName = lastName
        
    def setCNP(self, CNP):
        self.__cnp = CNP
    
    
class Rent:
    
    def __init__(self, ID, client, movie, date):
        self.__id = ID
        self.__client = client
        self.__movie = movie
        self.__date = date
    
    def __eq__(self, otherRent):
        return self.__client == otherRent.__client and self.__movie == otherRent.__movie
    
    def __repr__(self):
        return "#{} {} - {}, data: {}".format(self.__id, self.__client.getName(), self.__movie.getTitle(), self.__date)
    
    def getClient(self):
        return self.__client
    
    def getAttr1(self):
        return self.__client.getName()
    
    def getMovie(self):
        return self.__movie
    
    def getAttr2(self):
        return self.__movie.getTitle()
    
    def getDate(self):
        return self.__date
    
    def getAttr3(self):
        return self.getDate()
    
    def getID(self):
        return self.__id
    
class StatisticsDTO:
    
    def __init__(self, rent):
        self.__movieTitle = rent.getMovie().getTitle()
        self.__clientName = rent.getClient().getName()
        self.__movieGenre = rent.getMovie().getGenre()
        
    def getClientName(self):
        return self.__clientName
        
    def getNumberOfRentsPerClient(self):
        return self.__numberOfRentsPerClient
        
    def getMovieTitle(self):
        return self.__movieTitle
        
    def getNumberOfRentsPerMovie(self):
        return self.__numberOfRentsPerMovie
    
    def getMovieGenre(self):
        return self.__movieGenre
    