'''
Created on Nov 6, 2018

Modulul principal al aplicatiei

@author: Silviu Anton
'''
from controller.client_controller import ClientController
from controller.movie_controller import MovieController

clientController = ClientController()

clientController.add_client("Silviu", "Anton", 1990722170051)
clientController.add_client("Andreea", "Finichiu", 1990722170051)
clientController.add_client("Alexandru", "Lazar", 1990722170051)
clientController.add_client("Andrei", "Nicodim", 1990722170051)

clientController.delete_client(3)

clientController.modify_client(4, "Nico", "Maximus", 1000220170046)
clientController.modify_client_name(2, "Andreea", "Anton")

clients = clientController.get_all()
print("Clientii sunt:")
for client in clients:
    print(client)
print()

movieController = MovieController()

movieController.add_movie("Pirates of the Carraibbean", "A movie about pirates and their mighty adventures.", "Action/Adventure")
movieController.add_movie("Lord of the Rings", "A movie about mithical creatures and a ring of power.", "Action/Adventure/Fantasy")
movieController.add_movie("IT", "A movie about a shapeshifter beeing who feeds on the fear of the kids and impersonates a clown.", "Horror/Thriller")

movieController.delete_movie(2)

movies = movieController.get_all()

print("Filmele sunt:")
for movie in movies:
    print(movie)
    