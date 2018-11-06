'''
Created on Nov 6, 2018

Modulul principal al aplicatiei

@author: Silviu Anton
'''
from controller.client_controller import ClientController
from repository.repository import Repository
from controller.movie_controller import MovieController

clientController = ClientController(Repository())

clientController.add_client(1, "Silviu", "Anton", 1990722170051)
clientController.add_client(2, "Silviu", "Anton", 1990722170051)
clientController.add_client(3, "Silviu", "Anton", 1990722170051)
clientController.add_client(4, "Silviu", "Anton", 1990722170051)

clientController.delete_client(2)

clients = clientController.get_all()
for client in clients:
    print(str(client.getID()) + ' ' + str(client.getName()))

movieController = MovieController(Repository())

movieController.add_movie(1, "Pirates of the Carraibbean", "A movie about pirates", "Action/Adventure")
movieController.add_movie(2, "Pirates of the Carraibbean", "A movie about pirates", "Action/Adventure")
movieController.add_movie(3, "Pirates of the Carraibbean", "A movie about pirates", "Action/Adventure")

movieController.delete_movie(2)

movies = movieController.get_all()
for movie in movies:
    print(str(movie.getID()) + ' ' + movie.getDescription())