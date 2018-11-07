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
clientController.add_client(2, "Andreea", "Finichiu", 1990722170051)
clientController.add_client(3, "Alexandru", "Lazar", 1990722170051)
clientController.add_client(4, "Andrei", "Nicodim", 1990722170051)

clientController.delete_client(3)

clients = clientController.get_all()
print("Clientii sunt:")
for client in clients:
    print(client)
print()

movieController = MovieController(Repository())

movieController.add_movie(1, "Pirates of the Carraibbean", "A movie about pirates and their mighty adventures.", "Action/Adventure")
movieController.add_movie(2, "Lord of the Rings", "A movie about mithical creatures and a ring of power.", "Action/Adventure/Fantasy")
movieController.add_movie(3, "IT", "A movie about a shapeshifter beeing who feeds on the fear of the kids and impersonates a clown.", "Horror/Thriller")

movieController.delete_movie(2)

movies = movieController.get_all()

print("Filmele sunt:")
for movie in movies:
    print(movie)
    