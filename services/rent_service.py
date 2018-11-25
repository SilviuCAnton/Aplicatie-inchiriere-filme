'''
Created on Nov 18, 2018

Modul pentru gestionarea inchirierilor

@author: Silviu Anton
'''
from domain.entities import Rent, StatisticsDTO
from errors_tests.errors import RepositoryError
from datetime import date

class RentService:
    
    def __init__(self, repository):
        self.__repository = repository
        self.__nextRentID = self.__repository.getLastID() + 1
        
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
            client.incReferenceCounter()
            movie.incReferenceCounter()
            
            todaysDate = date.today()
            rent = Rent(self.__nextRentID, client, movie, todaysDate)
            
            if rent in self.__repository.get_all():
                raise RepositoryError("Contractul de inchiriere exista deja!!!")
            
            self.__nextRentID += 1
            self.__repository.store(rent.getID(), rent) 
            
        except Exception as ex:
            client.decReferenceCounter()
            movie.decReferenceCounter()
            self.__nextRentID -= 1
            raise ex
        
    def rentReturn(self, ID):
        '''
        Description: returneaza un film deja inchiriat
        
        In:
            - ID - id-ul inchirierii
        '''
        self.__repository.getItem(ID).getClient().decReferenceCounter()
        self.__repository.getItem(ID).getMovie().decReferenceCounter()
        self.__repository.delete(ID)
    
    def number_of_rents(self):
        '''
        Description: returneaza numarul de inchirieri
        '''
        return self.__repository.size()
    
    def __getDTOList(self):
        dtoList = []
        for rent in self.get_all():
            dto = StatisticsDTO(rent)
            dtoList.append(dto)
        return dtoList
    
    def mostRentedMovies(self):
        dtoList = self.__getDTOList()
        movieRents = {}
        movieList = []
        for dto in dtoList:
            if dto.getMovieTitle() not in movieRents:
                movieRents[dto.getMovieTitle()] = 1
            else:
                movieRents[dto.getMovieTitle()] += 1
                
        for movie in movieRents.keys():
            movieList.append((movie, movieRents[movie]))
                             
        movieList.sort(key = lambda x: x[1], reverse = True)
            
        return movieList
    
    def getMovieTitle(self, movieTuple):
        return movieTuple[0]
    
    def getMovieRents(self, movieTuple):
        return movieTuple[1]
    
    def __getClientList(self):
        dtoList = self.__getDTOList()
        clientList = []
        clientRents = {}
        for dto in dtoList:
            if dto.getClientName() not in clientRents:
                clientRents[dto.getClientName()] = 1
            else:
                clientRents[dto.getClientName()] += 1
    
        for client in clientRents.keys():
            clientList.append((client, clientRents[client]))
            
        return clientList
    
    def ClientsOrderedByName(self):
        clientList = self.__getClientList()
                             
        clientList.sort(key = lambda x: x[0], reverse = False)
            
        return clientList
    
    def getClientName(self, clientTuple):
        return clientTuple[0]
    
    def getClientRents(self, clientTuple):
        return clientTuple[1]
    
    def ClientsOrderedByNumberOfRents(self):
        clientList = self.__getClientList()
                             
        clientList.sort(key = lambda x: x[1], reverse = True)
            
        return clientList
    
    def Top30Clients(self):
        clientList = self.__getClientList()                    
        clientList.sort(key = lambda x: x[1], reverse = True)
        numberOfClietnsDisplayed = int(30/100 * len(clientList))
        if numberOfClietnsDisplayed > 0:
            clientList = clientList[:numberOfClietnsDisplayed]
        return clientList
    