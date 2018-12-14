'''
Created on Nov 18, 2018

Modul pentru gestionarea inchirierilor

@author: Silviu Anton
'''
from domain.entities import Rent, StatisticsDTO
from errors_tests.errors import DuplicateError
from datetime import date

class RentService:
    
    def __init__(self, repository, validator, clientRepository, movieRepository):
        self.__repository = repository
        self.__validator = validator
        self.__clientRepository = clientRepository
        self.__movieRepository = movieRepository
        self.__nextRentID = self.__repository.getLastID() + 1
        
    def get_all(self):
        '''
        Descriprion: returneaza o lista cu toate inchirierile din repository-ul de inchirieri
        '''
        rentList = []
        rentTuples =  self.__repository.get_all()
        for rentTuple in rentTuples:
            client = self.__clientRepository.getItem(rentTuple[1])
            movie = self.__movieRepository.getItem(rentTuple[2])
            rent = Rent(rentTuple[0], client, movie, rentTuple[3])
            rentList.append(rent)
        
        return rentList
    
    def getIDbyClientAndMovie(self, client, movie):
        '''
        Description: calculeaza id-ul unei inchirieri plecand de la client si filmul pe care l-a inchiriat
        
        In:
            - client - clientul
            - movie - filmul inchiriat
        
        Out:
            - returneaza id-ul inchirierii sau 0 daca inchirierea nu exista in repository
        '''
        rents = self.get_all()
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
            self.__nextRentID = self.__repository.getLastID() + 1
            client.incReferenceCounter()
            movie.incReferenceCounter()
            
            todaysDate = date.today()
            rent = Rent(self.__nextRentID, client, movie, todaysDate)
            
            
            if rent in self.get_all():
                raise DuplicateError("Contractul de inchiriere exista deja!!!")
            
            self.__validator.validate(rent)
            self.__repository.store(rent) 
            
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
        rents = self.get_all()
        for rent in rents:
            if rent.getID() == ID:
                rent.getClient().decReferenceCounter()
                rent.getMovie().decReferenceCounter()
                self.__repository.delete(ID)
                break
    
    def number_of_rents(self):
        '''
        Description: returneaza numarul de inchirieri
        '''
        return self.__repository.size()
    
    def getMovieTitle(self, movieTuple):
        '''
        Description: returneaza titlul unui film din dto
        '''
        return movieTuple[0]
    
    def getMovieRents(self, movieTuple):
        '''
        Descritpion: returneaza numarul de inchirieri ale unui film din dto
        '''
        return movieTuple[1]
    
    def getClientName(self, clientTuple):
        '''
        Description: returneaza numele unui client din dto
        '''
        return clientTuple[0]
    
    def getClientRents(self, clientTuple):
        '''
        Description: returneaza numarul de inchirieri ale unui client din dto
        '''
        return clientTuple[1]
    
    def __getDTOList(self):
        '''
        Description: returneaza lista de dto pentru inchirieri
        
        Out:
            - dtoList - lista de dto(data transfer objects)
        '''
        dtoList = []
        for rent in self.get_all():
            dto = StatisticsDTO(rent)
            dtoList.append(dto)
        return dtoList
    
    def __getClientList(self):
        '''
        Description: returneaza lista de clienti din dto(data transfer objects)
        
        Out: 
            - clientList - lista de clienti
        '''
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
    
    def mostRentedMovies(self):
        '''
        Description: returneaza lista de filme ordonata descrescator dupa numarul de inchirieri
        
        Out:
            - movieList - lista de filme
        '''
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
                             
        movieList.sort(key = lambda x: self.getMovieRents(x), reverse = True)
            
        return movieList
    
    def ClientsOrderedByName(self):
        '''
        Description: returneaza lista de clienti ordonata dupa nume
        
        Out:
            - clientList - lista de client
        '''
        clientList = self.__getClientList()
                             
        clientList.sort(key = lambda x: self.getClientName(x), reverse = False)
            
        return clientList

    def ClientsOrderedByNumberOfRents(self):
        '''
        Description: returneaza lista de clienti ordonata dupa numarul de inchirieri
        
        Out:
            - clientList - lista de client
        '''
        clientList = self.__getClientList()
                             
        clientList.sort(key = lambda x: self.getClientRents(x), reverse = True)
            
        return clientList
    
    def Top30Clients(self):
        '''
        Description: returneaza lista cu primii 30% clienti cu cele mai multe inchirieri
        
        Out:
            - clientList - lista de clienti
        '''
        clientList = self.__getClientList()                    
        clientList.sort(key = lambda x: self.getClientRents(x), reverse = True)
        numberOfClietnsDisplayed = int(30/100 * len(clientList))
        if numberOfClietnsDisplayed > 0:
            clientList = clientList[:numberOfClietnsDisplayed]
        return clientList
    
    def topClientsWithRentedMoviesByGenre(self, genre):
        '''
        Description: returneza o lista cu clientii care au inchiriat filme de un anumit gen, ordonati dupa numarul de inchirieri
        
        In:
            - genre - genul filmului
            
        Out:
            - clientList - lista clientilor ce respecta conditia
        '''
        dtoList = self.__getDTOList()
        clientList = []
        clientRents = {}
        
        for dto in dtoList:
            if genre in dto.getMovieGenre():
                
                if dto.getClientName() not in clientRents:
                    clientRents[dto.getClientName()] = 1
                else:
                    clientRents[dto.getClientName()] += 1       
    
        for client in clientRents.keys():
            clientList.append((client, clientRents[client]))
        
        clientList.sort(key = lambda x: self.getClientRents(x), reverse = True)
        
        return clientList
        