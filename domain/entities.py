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
        
    def getTitle(self):
        return self.__title
    
    def getDescription(self):
        return self.__description
    
    def getGenre(self):
        return self.__genre


class Client:
    
    def __init_(self, ID, firstName, lastName, CNP):
        
        self.__id = ID
        self.__firstName = firstName
        self.__lastName = lastName
        self.__cnp = CNP
        
    def getID(self):
        
        return self.__id
            
    def getName(self):
        
        fullName = self.__firstName + ' ' + self.__lastName
        
        return fullName
    
    def getCNP(self):
        
        return self.__cnp