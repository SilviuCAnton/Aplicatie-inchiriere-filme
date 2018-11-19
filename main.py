'''
Created on Nov 6, 2018

Modulul principal al aplicatiei

@author: Silviu Anton
'''
from services.client_service import ClientService
from services.movie_service import MovieService
from infrastructure.repository import MemoryRepository
from domain.validators import ClientValidator, MovieValidator, RentValidator
from ui.console import Console
from errors_tests.tests import TestClient, TestMovie, TestRent
from services.rent_service import RentService

if __name__ == '__main__':
    testClient = TestClient()
    testMovie = TestMovie()
    testRent = TestRent()
    
    testClient.runTests()
    testMovie.runTests()
    testRent.runTests()

    clientService = ClientService(MemoryRepository(ClientValidator()))
    movieService = MovieService(MemoryRepository(MovieValidator()))
    rentService = RentService(MemoryRepository(RentValidator()))

    console = Console(clientService, movieService, rentService)
    console.run()
