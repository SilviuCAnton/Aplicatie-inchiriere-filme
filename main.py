'''
Created on Nov 6, 2018

Modulul principal al aplicatiei

@author: Silviu Anton
'''
from controller.client_controller import ClientController
from controller.movie_controller import MovieController
from infrastructure.repository import MemoryRepository
from errors_validators_tests.validators import ClientValidator, MovieValidator
from ui.console import Console


clientController = ClientController(MemoryRepository(ClientValidator()))
movieController = MovieController(MemoryRepository(MovieValidator()))

console = Console(clientController, movieController)
console.run()
