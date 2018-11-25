'''
Created on Nov 11, 2018

Modul pentru teste

@author: Silviu Anton
'''
from domain.entities import Client, Movie, Rent
from domain.validators import ClientValidator, MovieValidator, RentValidator
from infrastructure.repository import MemoryRepository
from services.client_service import ClientService
from errors_tests.errors import ValidError, RepositoryError, DuplicateError
from services.movie_service import MovieService
from datetime import date
from services.rent_service import RentService

class TestClient:
    
    def __init__(self):
        self.__ID = 13
        self.__firstName = "Silviu"
        self.__lastName = "Anton"
        self.__CNP = 1990722170051
        self.__client = Client(self.__ID, self.__firstName, self.__lastName, self.__CNP)
        self.__validator = ClientValidator()
        self.__badID = 5
        self.__badFirstName = ""
        self.__badLastName = ""
        self.__badCNP = 12654
        self.__badClient = Client(self.__badID, self.__badFirstName, self.__badLastName, self.__badCNP)
        self.__repo = MemoryRepository(self.__validator)
        self.__service = ClientService(self.__repo)
        
    def __testEntity(self):
        assert self.__client.getID() == self.__ID
        
    def __testValidator(self):
        try:
            self.__validator.validate(self.__client)
            assert True
            
        except ValidError:
            assert False
            
        try:
            self.__validator.validate(self.__badClient)
            assert False
        
        except ValidError:
            assert True
        
    def __testRepository(self):
        assert self.__repo.size() == 0
        self.__repo.store(self.__ID, self.__client)
        assert self.__repo.size() == 1
        
        try:
            self.__repo.store(self.__ID, self.__client)
            assert False
            
        except RepositoryError:
            assert True
        
        assert len(self.__repo.get_all()) == 1
        
        assert self.__repo.size() == 1
           
        self.__repo.delete(self.__ID)
        assert self.__repo.size() == 0
        
    def __testService(self):
        self.__service.add_client("Silviu", "Anton", 1990722170051)
        assert len(self.__service.get_all()) == 1
        
        self.__service.modify_client(1, "Constantin", "Anton", 1990722170052)
        assert self.__service.findByID(1).getCNP() == 1990722170052
    
        self.__service.modify_client_name(1, "Anton", "Constantin")
        assert self.__service.findByID(1).getName() == "Anton Constantin"
        
        self.__service.generate_clients(4)
        assert self.__service.number_of_clients() == 5
        
        self.__service.delete_client(5)
        self.__service.delete_client(4)
        self.__service.delete_client(3)
        self.__service.delete_client(2)
        self.__service.delete_client(1)
        
        assert self.__service.number_of_clients() == 0
        
        
    def runTests(self):
        self.__testEntity()
        self.__testValidator()
        self.__testRepository()
        self.__testService()
        
        
class TestMovie:
    
    def __init__(self):
        self.__ID = 13
        self.__title = "Pirates of the Caraibbean"
        self.__description = "a movie about pirates"
        self.__genre = "Action/Adventure"
        self.__movie = Movie(self.__ID, self.__title, self.__description, self.__genre)
        self.__validator = MovieValidator()
        self.__badID = 5
        self.__badTitle = ""
        self.__badDescription = "A moive  about 6 pirates."
        self.__badGenre = ""
        self.__badMovie = Movie(self.__badID, self.__badTitle, self.__badDescription, self.__badGenre)
        self.__repo = MemoryRepository(self.__validator)
        self.__service = MovieService(self.__repo)
        
    def __testEntity(self):
        assert self.__movie.getID() == self.__ID
        
    def __testValidator(self):
        try:
            self.__validator.validate(self.__movie)
            
        except ValidError:
            assert False
            
        try:
            self.__validator.validate(self.__badMovie)
            assert False
        
        except ValidError:
            assert True
        
    def __testRepository(self):
        assert self.__repo.size() == 0
        self.__repo.store(self.__ID, self.__movie)
        assert self.__repo.size() == 1
        
        try:
            self.__repo.store(self.__ID, self.__movie)
            assert False
            
        except RepositoryError:
            assert True
        
        assert len(self.__repo.get_all()) == 1
        
        assert self.__repo.size() == 1
           
        self.__repo.delete(self.__ID)
        assert self.__repo.size() == 0
        
    def __testService(self):
        self.__service.add_movie("Saw", "a movie about a psycho", "Horror")
        assert len(self.__service.get_all()) == 1
        
        self.__service.modify_movie("Saw", "Saw 2", "a second movie about a psycho", "Horror/Thriller")
        assert self.__service.findByTitle("Saw 2").getGenre() == "Horror/Thriller"
    
        self.__service.modify_movie_description("Saw 2", "abc")
        assert self.__service.findByTitle("Saw 2").getDescription() == "abc"
        
        assert self.__service.getIDbyTitle("Saw 2") == 1
        
    def runTests(self):
        self.__testEntity()
        self.__testValidator()
        self.__testRepository()
        self.__testService()
     
        
class TestRent:
    
    def __init__(self):
        self.__ID = 13
        self.__client = Client(5, "Silviu", "Anton", 1990722170051)
        self.__movie = Movie(5, "Saw", "a movie about a psycho", "Horror")
        self.__date = date.today()
        self.__rent = Rent(self.__ID, self.__client, self.__movie, self.__date)
        self.__validator = RentValidator()
        self.__repo = MemoryRepository(self.__validator)
        self.__service = RentService(self.__repo)
        
    def __testEntity(self):
        assert self.__rent.getID() == self.__ID
        
    def __testValidator(self):
        pass
        
    def __testRepository(self):
        assert self.__repo.size() == 0
        self.__repo.store(self.__ID, self.__rent)
        assert self.__repo.size() == 1
        
        try:
            self.__repo.store(self.__ID, self.__rent)
            assert False
            
        except DuplicateError:
            assert True
        
        assert len(self.__repo.get_all()) == 1
        
        assert self.__repo.size() == 1
           
        self.__repo.delete(self.__ID)
        assert self.__repo.size() == 0
        
    def __testService(self):
        self.__service.add_rent(self.__client, self.__movie)
        assert len(self.__service.get_all()) == 1
        
        try:
            self.__service.add_rent(self.__client, self.__movie)
            assert False
        except RepositoryError:
            assert True
        
        assert self.__service.getIDbyClientAndMovie(self.__client, self.__movie) == 1
        
        assert self.__service.number_of_rents() == 1
        
        self.__service.rentReturn(1)
        
        assert self.__service.number_of_rents() == 0
        
    def runTests(self):
        self.__testEntity()
        self.__testValidator()
        self.__testRepository()
        self.__testService()