'''
Created on Nov 6, 2018

Modul pentru gestionarea clientilor.

@author: Silviu Anton
'''
from domain.entities import Client

class ClientController:
    
    def __init__(self):
        self.__repository = {}
        self.__nextClient_ID = 1
    
    def get_all(self):
        '''
        Description: returneaza o lista cu toti clientii din repository-ul de clienti
        '''
        return list(self.__repository.values())
    
    def get_client(self, ID):
        '''
        Description: returneaza clientul cu ID-ul dat
        
        In:
            - ID - numar intreg
        
        Out:
            - client
        '''
        return self.__repository[ID]
    
    def add_client(self, firstName, lastName, CNP):
        '''
        Description: audauga un client in repository-ul de clienti, alocandu-i un ID
        
        In:
            - firstName - prenumele clientului
            - lastName - nuemele clientului
            - CNP - codul numeric personal al clientului
        '''
        client = Client(self.__nextClient_ID, firstName, lastName, CNP)
        self.__nextClient_ID += 1
        self.__repository[client.getID()] = client  
        
    def delete_client(self, ID):
        '''
        Description: sterge un client din repository-ul de clienti
        '''
        self.__repository.pop(ID)
    
    def modify_client(self, ID, firstName, lastName, CNP):
        '''
        Description: modifica datele clientului cu ID-ul dat
        
        In:
            - ID - id-ul clientului caruia ii modificam datele
            - firstName - prenume
            - lastName - nume
            - CNP - cod numeric personal
        '''
        self.__repository[ID].setName(firstName, lastName)
        self.__repository[ID].setCNP(CNP)
        
    def modify_client_name(self, ID, firstName, lastName):
        '''
        Description: modifica numele unui clinet
        
        In:
            - ID - id-ul clientului caruia ii modificam datele
            - firstName - prenume
            - lastName - nume
        '''
        self.__repository[ID].setName(firstName, lastName)
    
    def modify_client_CNP(self, ID, CNP):
        '''
        Description: modifica numele unui clinet
        
        In:
            - ID - id-ul clientului caruia ii modificam datele
            - CNP - cod numeric personal
        '''
        self.__repository[ID].setCNP(CNP)
        