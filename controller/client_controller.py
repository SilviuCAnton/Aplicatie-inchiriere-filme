'''
Created on Nov 6, 2018

Modul pentru gestiunea clientilor

@author: Silviu Anton
'''
from domain.entities import Client

class ClientController:
    
    def __init__(self):
        self.__repository = {}
        self.__nextClient_ID = 1
    
    def get_all(self):
        return list(self.__repository.values())
    
    def get_client(self, ID):
        return self.__repository[ID]
    
    def add_client(self, firstName, lastName, CNP):
        client = Client(self.__nextClient_ID, firstName, lastName, CNP)
        self.__nextClient_ID += 1
        self.__repository[client.getID()] = client  
        
    def delete_client(self, ID):
        self.__repository.pop(ID)
    
    def modify_client(self, ID, firstName, lastName, CNP):
        self.__repository[ID].setName(firstName, lastName)
        self.__repository[ID].setCNP(CNP)
        
    def modify_client_name(self, ID, firstName, lastName):
        self.__repository[ID].setName(firstName, lastName)
    
    def modify_client_CNP(self, ID, CNP):
        self.__repository[ID].setCNP(CNP)
        