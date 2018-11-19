'''
Created on Nov 6, 2018

Modul pentru gestionarea clientilor.

@author: Silviu Anton
'''
from domain.entities import Client
from errors_tests.errors import RepositoryError, ValidError
from random import randint, choice

class ClientService:
    
    def __init__(self, repository):
        self.__repository = repository
        self.__nextClientID = 1
    
    def get_all(self):
        '''
        Description: returneaza o lista cu toti clientii din repository-ul de clienti
        '''
        return self.__repository.get_all()
    
    def findByID(self, ID):
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
            
        Exceptions:
            - ridica RepositoryError daca exista deja clientul
        '''
        client = Client(self.__nextClientID, firstName, lastName, CNP)
        
        if client in self.__repository.get_all():
            raise RepositoryError("Clientul deja exista!!!")
        
        try:    
            self.__nextClientID += 1
            self.__repository.store(client.getID(), client)
            
        except Exception as ex:
            self.__nextClientID -= 1
            raise ex
        
    def delete_client(self, ID):
        '''
        Description: sterge un client din repository-ul de clienti
        '''
        self.__repository.delete(ID)
    
    def modify_client(self, ID, firstName, lastName, CNP):
        '''
        Description: modifica datele clientului cu ID-ul dat
        
        In:
            - ID - id-ul clientului caruia ii modificam datele
            - firstName - prenume
            - lastName - nume
            - CNP - cod numeric personal
        '''
        client = self.__repository.getItem(ID)
        client.setName(firstName, lastName)
        client.setCNP(CNP)
                      
        self.__repository.update(client)
        
    def modify_client_name(self, ID, firstName, lastName):
        '''
        Description: modifica numele unui clinet
        
        In:
            - ID - id-ul clientului caruia ii modificam datele
            - firstName - prenume
            - lastName - nume
        '''
        client = self.__repository.getItem(ID)
        client.setName(firstName, lastName)
        
        self.__repository.update(client)
    
    def modify_client_CNP(self, ID, CNP):
        '''
        Description: modifica numele unui clinet
        
        In:
            - ID - id-ul clientului caruia ii modificam datele
            - CNP - cod numeric personal
        '''  
        client = self.__repository.getItem(ID)
        client.setCNP(CNP)
            
        self.__repository.update(client)
            
    def number_of_clients(self):
        '''
        Description: returneaza numarul de clienti
        '''
        return self.__repository.size()
    
    def generate_clients(self, numberOfClients):
        '''
        Description: genereaza si adauga in repository un numar de clienti
        
        In:
            - numberOfClients - numarul de clienti
        
        Exceptions: ridica ValueError daca numberOfClients nu este un numar natural mai mare decat 0
        '''
        if numberOfClients <= 0:
            raise ValueError("Trebuie introdus un numar valid!!!")
        
        while numberOfClients > 0:
            firstName = ''
            lastName = ''
            cnp = randint(1000000000000, 9999999999999)
            lowerAlpha = 'qwertyuiopasdfghjklzxcvbnm'
            upperAlpha = 'QWERTYUIOPASDFGHJKLZXCVBNM'
            firstNameLenght = randint(3, 10)
            lastNameLenght = randint(3, 10)
            firstName += choice(upperAlpha)
            lastName += choice(upperAlpha)
            
            for letter in range(firstNameLenght):
                firstName += choice(lowerAlpha)
            for letter in range(lastNameLenght):
                lastName += choice(lowerAlpha)
            
            try:
                numberOfClients -= 1
                self.add_client(firstName, lastName, cnp)
            except ValidError:
                numberOfClients += 1
                