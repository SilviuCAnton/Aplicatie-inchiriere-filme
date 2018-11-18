'''
Created on Nov 6, 2018

Modulul principal al aplicatiei

@author: Silviu Anton
'''
from controller.client_controller import ClientController
from controller.movie_controller import MovieController
from infrastructure.repository import MemoryRepository
from domain.validators import ClientValidator, MovieValidator, RentValidator
from ui.console import Console
from errors_tests.tests import TestClient, TestMovie, TestRent
from controller.rent_controller import RentController

if __name__ == '__main__':
    testClient = TestClient()
    testMovie = TestMovie()
    testRent = TestRent()
    
    testClient.runTests()
    testMovie.runTests()
    testRent.runTests()

    clientController = ClientController(MemoryRepository(ClientValidator()))
    movieController = MovieController(MemoryRepository(MovieValidator()))
    rentController = RentController(MemoryRepository(RentValidator()))

    console = Console(clientController, movieController, rentController)
    console.run()
