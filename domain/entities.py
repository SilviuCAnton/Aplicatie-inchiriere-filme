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
        
    def __eq__(self, otherMovie):
        return self.__title == otherMovie.__title
    
    def getID(self):
        return self.__id
        
    def getTitle(self):
        return self.__title
    
    def getDescription(self):
        return self.__description
    
    def getGenre(self):
        return self.__genre
    
    def setTitle(self, title):
        self.__title = title
        
    def setDescription(self, description):
        self.__description = description
        
    def setGenre(self, genre):
        self.__genre = genre
    
    def __repr__(self):
        return "#{} {}, genre: {}".format(self.getID(), self.getTitle(), self.getGenre())


class Client:
    
    def __init__(self, ID, firstName, lastName, CNP):  
        self.__id = ID
        self.__firstName = firstName
        self.__lastName = lastName
        self.__cnp = CNP
        
    def __eq__(self, otherClient):
        return self.__cnp == otherClient.__cnp
        
    def getID(self):       
        return self.__id
            
    def getName(self):
        fullName = self.__firstName + ' ' + self.__lastName
        return fullName
    
    def getCNP(self):
        return self.__cnp
    
    def setName(self, firstName, lastName):
        self.__firstName = firstName
        self.__lastName = lastName
        
    def setCNP(self, CNP):
        self.__cnp = CNP
    
    def __repr__(self):
        return "#{} {}".format(self.__id, self.getName())
    
    
class Rent:
    
    def __init__(self, ID, client, movie, date):
        self.__id = ID
        self.__client = client
        self.__movie = movie
        self.__date = date
    
    def __eq__(self, otherRent):
        return self.__client == otherRent.__client and self.__movie == self.__movie
    
    def __repr__(self):
        return "#{} {} - {}, data: {}".format(self.__id, self.__client.getName(), self.__movie.getTitle(), self.__date)
    
    def getClient(self):
        return self.__client
    
    def getMovie(self):
        return self.__movie
    
    def getDate(self):
        return self.__date
    
    def getID(self):
        return self.__id
    
    
    