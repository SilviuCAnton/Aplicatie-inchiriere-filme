'''
Created on Nov 11, 2018

Modul pentru teste

@author: Silviu Anton
'''
from domain.entities import Client, Movie
from domain.validators import ClientValidator, MovieValidator
from infrastructure.repository import MemoryRepository
from controller.client_controller import ClientController
from errors_tests.errors import ValidError, RepositoryError
from controller.movie_controller import MovieController

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
        self.__controller = ClientController(self.__repo)
        
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
        
    def __testController(self):
        self.__controller.add_client("Silviu", "Anton", 1990722170051)
        assert len(self.__controller.get_all()) == 1
        
        self.__controller.modify_client(1, "Constantin", "Anton", 1990722170052)
        assert self.__controller.findByID(1).getCNP() == 1990722170052
    
        self.__controller.modify_client_name(1, "Anton", "Constantin")
        assert self.__controller.findByID(1).getName() == "Anton Constantin"
        
    def runTests(self):
        self.__testEntity()
        self.__testValidator()
        self.__testRepository()
        self.__testController()
        
        
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
        self.__controller = MovieController(self.__repo)
        
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
        
    def __testController(self):
        self.__controller.add_movie("Saw", "a movie about a psycho", "Horror")
        assert len(self.__controller.get_all()) == 1
        
        self.__controller.modify_movie("Saw", "Saw 2", "a second movie about a psycho", "Horror/Thriller")
        assert self.__controller.findByTitle("Saw 2").getGenre() == "Horror/Thriller"
    
        self.__controller.modify_movie_description("Saw 2", "abc")
        assert self.__controller.findByTitle("Saw 2").getDescription() == "abc"
        
    def runTests(self):
        self.__testEntity()
        self.__testValidator()
        self.__testRepository()
        self.__testController()