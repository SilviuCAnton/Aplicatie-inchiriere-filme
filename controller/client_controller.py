'''
Created on Nov 6, 2018

Modul pentru gestiunea clientilor

@author: Silviu Anton
'''
from domain.entities import Client

class ClientController:
    
    def __init__(self, repository):
        self.__repository = repository
    
    def get_all(self):
        return self.__repository.get_all()
    
    def add_client(self, ID, firstName, lastName, CNP):
        client = Client(ID, firstName, lastName, CNP)
        self.__repository.save(client)    
        
    def delete_client(self, ID):
        self.__repository.delete(ID)