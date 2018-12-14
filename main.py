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


if __name__ == '__main__':
    
    clientRepository = FileRepository('clienti.txt', Client)
    clientService = ClientService(clientRepository, ClientValidator())
    
    movieRepository = FileRepository('filme.txt', Movie)
    movieService = MovieService(movieRepository, MovieValidator())
    
    rentRepository = RentFileRepository('inchirieri.txt')
    rentService = RentService(rentRepository, RentValidator(), clientRepository, movieRepository)

    console = Console(clientService, movieService, rentService)
    console.run()
