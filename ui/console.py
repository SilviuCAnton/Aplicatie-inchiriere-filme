'''
Created on Nov 11, 2018

Modul pentru interactiunea cu utilizatorul

@author: Silviu Anton
'''
from errors_validators_tests.errors import RepositoryError, ValidError
from time import sleep

class Console:
    
    def __init__(self, clientController, movieController):
        self.__clientController = clientController
        self.__movieController = movieController
        
        self.__submenuClient = {1: (self.__uiAddClient, "Adaugati un client"),
                                2: (self.__uiGetAllClients, "Afisare clientii"),
                                3: (self.__uiDeleteClient, "Stergeti un client"),
                                4: (self.__uiModifyClient, "Modificati un client"),
                                5: (self.__uiModifyClientName, "Modificati numele unui client"),
                                6: (self.__uiModifyClientCNP, "Modificati CNP-ul unui client"),
                                7: (self.__uiNumberOfClients, "Afisare numar clienti")}
        
        self.__submenuMovie = {1: (self.__uiAddMovie, "Adaugati un film"),
                               2: (self.__uiGetAllMovies, "Afisare filme"),
                               3: (self.__uiDeleteMovie, "Stergeti un film"),
                               4: (self.__uiModifyMovie, "Modificati un film"),
                               5: (self.__uiModifyMovieTitle, "Modificati titlul unui film"),
                               6: (self.__uiModifyMovieDescription, "Modificati descrierea unui film"),
                               7: (self.__uiModifyMovieGenre, "Modificati genul unui film"),
                               8: (self.__uiNumberOfMovies, "Afisare numar filme")}
        
        self.__mainMenu = {1: (self.__submenuClient, "Operatii clienti"),
                           2: (self.__submenuMovie, "Operatii filme"),
                           0: (None, "Inchideti aplicatia")}
        
    def __uiAddMovie(self):
        title = input("Introduceti titlul filmului: ")
        description = input("Introduceti descrierea filmului: ")
        genre = input("Introduceti genul/genurile filmului: ")
        
        try:
            self.__movieController.add_movie(title, description, genre)
            print()
            print("Filmul a fost adaugat!")
            sleep(1)
        
        except RepositoryError as re:
            print()
            print(re)
            print()
            sleep(1)
            
        except ValidError as ve:
            print()
            print(ve)
            print()
            sleep(1)
        
    def __uiAddClient(self):
        
        try:
            firstName = input("Introduceti prenumele: ")
            lastName = input("Introduceti numele de familie: ")
            CNP = int(input("Introduceti CNP: "))
        
        
            self.__clientController.add_client(firstName, lastName, CNP)
            print()
            print("Clientul a fost adaugat!")
            sleep(1)
        
        except RepositoryError as re:
            print()
            print(re)
            print()
            sleep(1)
        
        except ValidError as ve:
            print()
            print(ve)
            print()
            sleep(1)
        
        except ValueError:
            print()
            print("CNP trebuie sa fie numar!!!")
            print()
            sleep(1)
            
    def __uiGetAllClients(self):
        clients = self.__clientController.get_all()
        
        for client in clients:
            print(client)
        
        sleep(2)
        
    def __uiGetAllMovies(self):
        movies = self.__movieController.get_all()
        
        for movie in movies:
            print(movie)
            
        sleep(2)
        
    def __uiDeleteClient(self):
        try:
            ID = int(input("Introduceti id-ul clientului pe care doriti sa il stergeti: "))
            self.__clientController.delete_client(ID)
            print()
            print("Clientul a fost sters!")
            sleep(1)
        
        except RepositoryError as re:
            print(re)
            sleep(1)
        
        except ValueError:
            print()
            print("ID trebuie sa fie numar!!!")
            print()
            sleep(1)
            
    def __uiDeleteMovie(self):
        try:
            ID = int(input("Introduceti id-ul filmului pe care doriti sa il stergeti: "))
            self.__movieController.delete_movie(ID)
            print()
            print("Filmul a fost sters!")
            sleep(1)
            
        except RepositoryError as re:
            print(re) 
            sleep(1) 
            
        except ValueError:
            print()
            print("ID trebuie sa fie numar!!!") 
            print()
            sleep(1)
            
    def __uiModifyClient(self):  
        try:
            ID = int(input("Introduceti id-ul clientului pe care doriti sa il modificati: "))
            firstName = input("Introduceti prenumele: ")
            lastName = input("Introduceti numele de familie: ")
            CNP = int(input("Introduceti CNP: "))
            
            self.__clientController.modify_client(ID, firstName, lastName, CNP)
            print()
            print("Clientul cu id-ul", ID, "a fost modificat")
            sleep(1)
            
        except RepositoryError as re:
            print()
            print(re)
            print()  
            sleep(1) 
            
        except ValidError as ve:
            print()
            print(ve)
            print()
            sleep(1)
            
        except ValueError:
            print()
            print("ID  si CNP trebuie sa fie numere!!!")
            print()
            sleep(1)
            
    def __uiModifyMovie(self):
        try:
            ID = int(input("Introduceti id-ul filmului pe care doriti sa il modificati: "))
            title = input("Introduceti titlul filmului: ")
            description = input("Introduceti descrierea filmului: ")
            genre = input("Introduceti genul/genurile filmului: ")
            
            self.__movieController.modify_movie(ID, title, description, genre)
            print()
            print("Filmul cu id-ul", ID, "a fost modificat")
            sleep(1)
            
        except RepositoryError as re:
            print()
            print(re)
            print()
            sleep(1)
            
        except ValidError as ve:
            print()
            print(ve)
            print()
            sleep(1)
        
        except ValueError:
            print()
            print("ID trebuie sa fie numar!!!") 
            print()
            sleep(1)                 
            
    def __uiModifyClientName(self):      
        try:
            ID = int(input("Introduceti id-ul clientului pe care doriti sa il modificati: "))
            firstName = input("Introduceti prenumele: ")
            lastName = input("Introduceti numele de familie: ")
            
            self.__clientController.modify_client_name(ID, firstName, lastName)
            print()
            print("Clientul cu id-ul", ID, "a fost modificat")
            sleep(1)
        
        except RepositoryError as re:
            print()
            print(re)
            print()
            sleep(1)
            
        except ValidError as ve:
            print()
            print(ve)
            print()
            sleep(1)
            
        except ValueError:
            print()
            print("ID trebuie sa fie numar!!!") 
            print()
            sleep(1)
            
    def __uiModifyClientCNP(self): 
        try:
            ID = int(input("Introduceti id-ul clientului pe care doriti sa il modificati: "))
            CNP = int(input("Introduceti CNP: "))
            
            self.__clientController.modify_client_CNP(ID, CNP)
            print()
            print("Clientul cu id-ul", ID, "a fost modificat")
            sleep(1)
        
        except RepositoryError as re:
            print()
            print(re)
            print()
            sleep(1)
            
        except ValidError as ve:
            print()
            print(ve)
            print()
            sleep(1)
            
        except ValueError:
            print()
            print("ID  si CNP trebuie sa fie numere!!!")
            print()
            sleep(1)
            
    def __uiModifyMovieTitle(self):
        try:
            ID = int(input("Introduceti id-ul filmului pe care doriti sa il modificati: "))
            title = input("Introduceti titlul filmului: ")
            
            self.__movieController.modify_movie_title(ID, title)
            print()
            print("Filmul cu id-ul", ID, "a fost modificat")
            sleep(1)
            
        except RepositoryError as re:
            print()
            print(re)
            print()
            sleep(1)
            
        except ValidError as ve:
            print()
            print(ve)
            print()
            sleep(1)
            
        except ValueError:
            print()
            print("ID trebuie sa fie numar!!!") 
            print()
            sleep(1)    
    
    def __uiModifyMovieDescription(self):
        try:
            ID = int(input("Introduceti id-ul filmului pe care doriti sa il modificati: "))
            description = input("Introduceti descrierea filmului: ")
            
            self.__movieController.modify_movie_description(ID, description)
            print()
            print("Filmul cu id-ul", ID, "a fost modificat")
            sleep(1)
            
        except RepositoryError as re:
            print()
            print(re)
            print()
            sleep(1)
            
        except ValidError as ve:
            print()
            print(ve)
            print()    
            sleep(1)
            
        except ValueError:
            print()
            print("ID trebuie sa fie numar!!!") 
            print()
            sleep(1)
    
    def __uiModifyMovieGenre(self):
        try:
            ID = int(input("Introduceti id-ul filmului pe care doriti sa il modificati: "))
            genre = input("Introduceti genul/genurile filmului: ")
            
            self.__movieController.modify_movie_genre(ID, genre)
            print()
            print("Filmul cu id-ul", ID, "a fost modificat")
            sleep(1)
            
        except RepositoryError as re:
            print()
            print(re)
            print()
            sleep(1)
            
        except ValidError as ve:
            print()
            print(ve)
            print() 
            sleep(1)
            
        except ValueError:
            print()
            print("ID trebuie sa fie numar!!!") 
            print()
            sleep(1)   
    
    def __uiNumberOfClients(self):
        print("Numarul de clienti:", self.__clientController.number_of_clients())
        
    def __uiNumberOfMovies(self):
        print("Numarul de filme:", self.__movieController.number_of_movies())
        
    def __generateMenu(self, menu):
        print()
        print("Alegeti una dintre urmatoarele optiuni:")
        for option in menu:
            print(option, menu[option][1])
        print()
        
    def run(self):
        while True:
            self.__generateMenu(self.__mainMenu)
        
            choice1 = int(input("Optiunea dorita: "))
            
            if choice1 == 0:
                print()
                print("Se inchide aplicatia...")
                print()
                sleep(1)
                return
        
            try:
                submenu = self.__mainMenu[choice1][0]
                self.__generateMenu(submenu)
                choice2 = int(input("Optiunea dorita: "))
                submenu[choice2][0]()
        
            except KeyError:
                print()
                print("Optiunea nu exista!!!")  
                print()          
        