'''
Created on Nov 6, 2018

Modulul principal al aplicatiei

@author: Silviu Anton
'''
from services.client_service import ClientService
from services.movie_service import MovieService
from infrastructure.repository import MemoryRepository, FileRepository
from domain.validators import ClientValidator, MovieValidator, RentValidator
from ui.console import Console
from services.rent_service import RentService
from domain.entities import Client, Movie
from errors_tests.errors import DuplicateError


if __name__ == '__main__':
    
    clientService = ClientService(FileRepository('clienti.txt', ClientValidator(), Client))
    movieService = MovieService(FileRepository('filme.txt', MovieValidator(), Movie))
    rentService = RentService(MemoryRepository(RentValidator()))
    
    try:
        clientService.add_client("s", "s", 1111111111111)
        clientService.delete_client(1)
    except DuplicateError:
        pass
    
    try:
        movieService.add_movie("t", "t", "t")
        movieService.delete_movie("t")
    except DuplicateError:
        pass

    console = Console(clientService, movieService, rentService)
    console.run()
