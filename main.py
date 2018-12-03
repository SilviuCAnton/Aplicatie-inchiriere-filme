'''
Created on Nov 6, 2018

Modulul principal al aplicatiei

@author: Silviu Anton
'''
from services.client_service import ClientService
from services.movie_service import MovieService
from infrastructure.repository import FileRepository, RentFileRepository
from domain.validators import ClientValidator, MovieValidator, RentValidator
from ui.console import Console
from services.rent_service import RentService
from domain.entities import Client, Movie
from errors_tests.errors import DuplicateError


if __name__ == '__main__':
    
    clientRepository = FileRepository('clienti.txt', ClientValidator(), Client)
    clientService = ClientService(clientRepository)
    
    movieRepository = FileRepository('filme.txt', MovieValidator(), Movie)
    movieService = MovieService(movieRepository)
    
    rentService = RentService(RentFileRepository('inchirieri.txt', RentValidator(), clientRepository, movieRepository))

    console = Console(clientService, movieService, rentService)
    console.run()
