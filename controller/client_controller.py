'''
Created on Nov 6, 2018

Modul pentru gestionarea clientilor.

@author: Silviu Anton
'''
from domain.entities import Client

class ClientController:
    
    def __init__(self, repository, validator):
        self.__repository = repository
        self.__validator = validator
        self.__nextClientID = 1
    
    def get_all(self):
        '''
        Description: returneaza o lista cu toti clientii din repository-ul de clienti
        '''
        return self.__repository.get_all()
    
    def get_client(self, ID):
        '''
        Description: returneaza clientul cu ID-ul dat
        
        In:
            - ID - numar intreg
        
        Out:
            - client
        '''
        return self.__repository.getItem(ID)
    
    def add_client(self, firstName, lastName, CNP):
        '''
        Description: audauga un client in repository-ul de clienti, alocandu-i un ID
        
        In:
            - firstName - prenumele clientului
            - lastName - nuemele clientului
            - CNP - codul numeric personal al clientului
        '''
        client = Client(self.__nextClientID, firstName, lastName, CNP)
        
        try:
            self.__validator.validate(client)
            self.__nextClientID += 1
        
            if client in self.__repository.get_all():
                raise ValueError("Clientul deja exista!!!")
        
            self.__repository.store(client.getID(), client)
        
        except ValueError as err:
            print()
            print(err)
            print()
        
    def delete_client(self, ID):
        '''
        Description: sterge un client din repository-ul de clienti
        '''
        try:
            self.__repository.delete(ID)
            
        except ValueError as err:
            print(err)
    
    def modify_client(self, ID, firstName, lastName, CNP):
        '''
        Description: modifica datele clientului cu ID-ul dat
        
        In:
            - ID - id-ul clientului caruia ii modificam datele
            - firstName - prenume
            - lastName - nume
            - CNP - cod numeric personal
        '''
        try:
            client = self.__repository.getItem(ID)
            client.setName(firstName, lastName)
            client.setCNP(CNP)
            
            self.__validator.validate(client)          
            self.__repository.update(client)
        
        except ValueError as err:
            print()
            print(err)
            print()   
        
    def modify_client_name(self, ID, firstName, lastName):
        '''
        Description: modifica numele unui clinet
        
        In:
            - ID - id-ul clientului caruia ii modificam datele
            - firstName - prenume
            - lastName - nume
        '''
        try:
            client = self.__repository.getItem(ID)
            client.setName(firstName, lastName)
        
            self.__validator.validate(client) 
            self.__repository.update(client)
            
        except ValueError as err:
            print()
            print(err)
            print()
    
    def modify_client_CNP(self, ID, CNP):
        '''
        Description: modifica numele unui clinet
        
        In:
            - ID - id-ul clientului caruia ii modificam datele
            - CNP - cod numeric personal
        '''  
        try:
            client = self.__repository.getItem(ID)
            client.setCNP(CNP)
            
            self.__validator.validate(client)
            self.__repository.update(client)
        
        except ValueError as err:
            print()
            print(err)
            print()
        