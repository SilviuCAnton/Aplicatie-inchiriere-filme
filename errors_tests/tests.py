'''
Created on Nov 11, 2018

Modul pentru teste

@author: Silviu Anton
'''
from domain.entities import Client, Movie, Rent
from domain.validators import ClientValidator, MovieValidator, RentValidator
from infrastructure.repository import MemoryRepository
from services.client_service import ClientService
from errors_tests.errors import ValidError, DuplicateError
from services.movie_service import MovieService
from datetime import date
from services.rent_service import RentService
import unittest

class TestClient(unittest.TestCase):
    
    def setUp(self):
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
        
    def testEntity(self):
        self.assertEqual(self.__client.getID(), self.__ID)
        
    def testValidator(self):
        
        self.__validator.validate(self.__client)
            
        self.assertRaises(ValidError, self.__validator.validate, self.__badClient)
        
    def testRepository(self):
        self.assertEqual(self.__repo.size(), 0) 
        self.__repo.store(self.__ID, self.__client)
        self.assertEqual(self.__repo.size(), 1) 
        
        self.assertRaises(DuplicateError, self.__repo.store, self.__ID, self.__client)
        
        self.assertEqual(len(self.__repo.get_all()), 1)
        
        self.assertEqual(self.__repo.size(), 1)
           
        self.__repo.delete(self.__ID)
        self.assertEqual(self.__repo.size(), 0)
        
    def testService(self):
        self.__service.add_client("Silviu", "Anton", 1990722170051)
        self.assertEqual(len(self.__service.get_all()), 1)
        
        self.__service.modify_client(1, "Constantin", "Anton", 1990722170052)
        self.assertEqual(self.__service.findByID(1).getCNP(), 1990722170052)
    
        self.__service.modify_client_name(1, "Anton", "Constantin")
        self.assertEqual(self.__service.findByID(1).getName(), "Anton Constantin")
        
        self.__service.generate_clients(4)
        self.assertEqual(self.__service.number_of_clients(), 5)
        
        self.__service.delete_client(5)
        self.__service.delete_client(4)
        self.__service.delete_client(3)
        self.__service.delete_client(2)
        self.__service.delete_client(1)
        
        self.assertEqual(self.__service.number_of_clients(), 0)       
        
        
class TestMovie(unittest.TestCase):
    
    def setUp(self):
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
        
    def testEntity(self):
        self.assertEqual(self.__movie.getID(), self.__ID)
        
    def testValidator(self):
        self.__validator.validate(self.__movie)
        
        self.assertRaises(ValidError, self.__validator.validate, self.__badMovie)
        
    def testRepository(self):
        self.assertEqual(self.__repo.size(), 0)
        self.__repo.store(self.__ID, self.__movie)
        self.assertEqual(self.__repo.size(), 1)
        
        self.assertRaises(DuplicateError, self.__repo.store, self.__ID, self.__movie)
        
        self.assertEqual(len(self.__repo.get_all()), 1)
        
        self.assertEqual(self.__repo.size(), 1)
           
        self.__repo.delete(self.__ID)
        self.assertEqual(self.__repo.size(), 0)
        
    def testService(self):
        self.__service.add_movie("Saw", "a movie about a psycho", "Horror")
        self.assertEqual(len(self.__service.get_all()), 1)
        
        self.__service.modify_movie("Saw", "Saw 2", "a second movie about a psycho", "Horror/Thriller")
        self.assertEqual(self.__service.findByTitle("Saw 2").getGenre(), "Horror/Thriller")
    
        self.__service.modify_movie_description("Saw 2", "abc")
        self.assertEqual(self.__service.findByTitle("Saw 2").getDescription(), "abc")
        
        self.assertEqual(self.__service.getIDbyTitle("Saw 2"), 1)
     
       
class TestRent(unittest.TestCase):
    
    def setUp(self):
        self.__ID = 13
        self.__client = Client(5, "Silviu", "Anton", 1990722170051)
        self.__movie = Movie(5, "Saw", "a movie about a psycho", "Horror")
        self.__date = date.today()
        self.__rent = Rent(self.__ID, self.__client, self.__movie, self.__date)
        self.__validator = RentValidator()
        self.__repo = MemoryRepository(self.__validator)
        self.__service = RentService(self.__repo)
        self.__clientService = ClientService(MemoryRepository(ClientValidator()))
        self.__movieService = MovieService(MemoryRepository(MovieValidator()))
        
    def testEntity(self):
        self.assertEqual(self.__rent.getID(), self.__ID)
        
    def testValidator(self):
        self.__validator.validate(self.__movie)
        
    def testRepository(self):
        self.assertEqual(self.__repo.size(), 0)
        self.__repo.store(self.__ID, self.__rent)
        self.assertEqual(self.__repo.size(), 1)
        
        self.assertRaises(DuplicateError, self.__repo.store, self.__ID, self.__rent)
        
        self.assertEqual(len(self.__repo.get_all()), 1)
        
        self.assertEqual(self.__repo.size(), 1)
           
        self.__repo.delete(self.__ID)
        self.assertEqual(self.__repo.size(), 0)
        
    def testService(self):
        self.__service.add_rent(self.__client, self.__movie)
        self.assertEqual(len(self.__service.get_all()), 1)

        self.assertRaises(DuplicateError, self.__service.add_rent, self.__client, self.__movie)
        
        self.assertEqual(self.__service.getIDbyClientAndMovie(self.__client, self.__movie), 1)
        
        self.assertEqual(self.__service.number_of_rents(), 1)
        
        self.__service.rentReturn(1)
        
        self.assertEqual(self.__service.number_of_rents(), 0)
        
        self.__clientService.add_client("Silviu", "Anton1", 1111111111111)
        self.__clientService.add_client("Silviu", "Anton2", 1111111111112)
        self.__clientService.add_client("Silviu", "Anton3", 1111111111113)
        self.__movieService.add_movie("Saw", "desc", "Action/Adventure")
        self.__movieService.add_movie("Saw2", "desc", "Horror/Adventure")
        self.__movieService.add_movie("Saw3", "desc", "Thriller")
        self.__movieService.add_movie("Saw4", "desc", "Thriller/Horror/Adventure")
        self.__service.add_rent(self.__clientService.findByID(1), self.__movieService.findByTitle("Saw"))
        self.__service.add_rent(self.__clientService.findByID(1), self.__movieService.findByTitle("Saw2"))
        self.__service.add_rent(self.__clientService.findByID(1), self.__movieService.findByTitle("Saw4"))
        self.__service.add_rent(self.__clientService.findByID(2), self.__movieService.findByTitle("Saw"))    
        self.__service.add_rent(self.__clientService.findByID(2), self.__movieService.findByTitle("Saw3")) 
        self.__service.add_rent(self.__clientService.findByID(2), self.__movieService.findByTitle("Saw4"))  
        self.__service.add_rent(self.__clientService.findByID(3), self.__movieService.findByTitle("Saw2")) 
        self.__service.add_rent(self.__clientService.findByID(3), self.__movieService.findByTitle("Saw3")) 
        
        self.assertEqual(self.__service.topClientsWithRentedMoviesByGenre("Adventure"), [("Silviu Anton1", 3),("Silviu Anton2", 2),("Silviu Anton3", 1)])
    
unittest.main()