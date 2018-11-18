'''
Created on Nov 18, 2018

Modul pentru gestionarea inchirierilor

@author: Silviu Anton
'''
from domain.entities import Rent
from errors_tests.errors import RepositoryError
from datetime import date

class RentController:
    
    def __init__(self, repository):
        self.__repository = repository
        self.__nextRentID = 1
        
    def get_all(self):
        '''
        Descriprion: returneaza o lista cu toate inchirierile din repository-ul de inchirieri
        '''
        return self.__repository.get_all()
    
    def getIDbyClientAndMovie(self, client, movie):
        '''
        Description: calculeaza id-ul unei inchirieri plecand de la client si filmul pe care l-a inchiriat
        
        In:
            - client - clientul
            - movie - filmul inchiriat
        
        Out:
            - returneaza id-ul inchirierii sau 0 daca inchirierea nu exista in repository
        '''
        rents = self.__repository.get_all()
        for rent in rents:
            if rent.getClient() == client and rent.getMovie() == movie:
                return rent.getID()
        return 0
    
    def add_rent(self, client, movie):
        '''
        Description: adauga un film in repository-ul de filme, alocand-ui un ID
        
        In:
            - client - clientul care a inchiriat
            - movie - filmul pe care l-a inchiriat
        
        Exceptions:
            - ridica RepositoryError daca exista deja filmul
        '''
        try:
            todaysDate = date.today()
            rent = Rent(self.__nextRentID, client, movie, todaysDate)
                  
            if rent in self.__repository.get_all():
                raise RepositoryError("Inchirierea exista deja!!!")
            
            self.__nextRentID += 1
            self.__repository.store(rent.getID(), rent) 
            
        except Exception as ex:
            self.__nextRentID -= 1
            raise ex
        
    def rentReturn(self, ID):
        '''
        Description: returneaza un film deja inchiriat
        
        In:
            - ID - id-ul inchirierii
        '''
        self.__repository.delete(ID)
    
    def number_of_rents(self):
        '''
        Description: returneaza numarul de inchirieri
        '''
        return self.__repository.size()
    