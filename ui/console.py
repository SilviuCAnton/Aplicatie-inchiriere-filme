'''
Created on Nov 11, 2018

Modul pentru interactiunea cu utilizatorul

@author: Silviu Anton
'''
from errors_tests.errors import RepositoryError, ValidError, DeletionError
from time import sleep

class Console:
    
    def __init__(self, clientService, movieService, rentService):
        self.__clientService = clientService
        self.__movieService = movieService
        self.__rentService = rentService
        
        self.__submenuClient = {1: (self.__uiAddClient, "Adaugati un client"),
                                2: (self.__uiPrintAllClients, "Afisare clientii"),
                                3: (self.__uiFindClientByID, "Gaseste client dupa ID"),
                                4: (self.__uiDeleteClient, "Stergeti un client"),
                                5: (self.__uiModifyClient, "Modificati un client"),
                                6: (self.__uiModifyClientName, "Modificati numele unui client"),
                                7: (self.__uiModifyClientCNP, "Modificati CNP-ul unui client"),
                                8: (self.__uiNumberOfClients, "Afisare numar clienti"),
                                9: (self.__uiGenerateClients, "Generare clienti")}
        
        self.__submenuMovie = {1: (self.__uiAddMovie, "Adaugati un film"),
                               2: (self.__uiPrintAllMovies, "Afisare filme"),
                               3: (self.__uiFindMovieByTitle, "Gaseste film dupa titlu"),
                               4: (self.__uiDeleteMovie, "Stergeti un film"),
                               5: (self.__uiModifyMovie, "Modificati un film"),
                               6: (self.__uiModifyMovieTitle, "Modificati titlul unui film"),
                               7: (self.__uiModifyMovieDescription, "Modificati descrierea unui film"),
                               8: (self.__uiModifyMovieGenre, "Modificati genul unui film"),
                               9: (self.__uiNumberOfMovies, "Afisare numar filme"),
                               10: (self.__uiGenerateMovies, "Generare filme")}
        
        self.__submenuInchirieri = {1: (self.__uiAddRent, "Adaugati o inchiriere"),
                                    2: (self.__uiPrintAllRents, "Afisare inchirieri"),
                                    3: (self.__uiRentReturn, "Returnare film"),
                                    4: (self.__uiNumberOfRents, "Numar de inchirieri"),
                                    5: (self.__uiClientsOrderedByName, "Clienti cu filme inchiriate ordonati dupa nume"),
                                    6: (self.__uiClientsOrderedByNumberOfRents, "Clienti cu filme inchiriate ordonati dupa numarul de filme"),
                                    7: (self.__uiMostRentedMovies, "Cele mai inchiriate filme"),
                                    8: (self.__uiTop30Clients, "Top 30% clienti"),
                                    9: (self.__uiTopClientsWithRentedMoviesByGenre, "Top clienti cu filme inchiriate cu un gen dat")}
        
        self.__mainMenu = {1: (self.__submenuClient, "Operatii clienti"),
                           2: (self.__submenuMovie, "Operatii filme"),
                           3: (self.__submenuInchirieri, "Operatii inchirieri"),
                           0: (None, "Inchideti aplicatia")}
        
    def __uiAddMovie(self):
        title = input("Introduceti titlul filmului: ")
        description = input("Introduceti descrierea filmului: ")
        genre = input("Introduceti genul/genurile filmului: ")
        
        try:
            self.__movieService.add_movie(title, description, genre)
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
        
        
            self.__clientService.add_client(firstName, lastName, CNP)
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
            
    def __uiAddRent(self):
        try:
            self.__uiPrintAllClients()
            idClient = int(input("Introduceti ID-ul clientului: "))
            client = self.__clientService.findByID(idClient)

            self.__uiPrintAllMovies()
            title = input("Introcueti titlul filmului: ")
            movie = self.__movieService.findByTitle(title)
            
            self.__rentService.add_rent(client, movie)
            
            print()
            print("A fost adaugat un nou contract de inchiriere!")
            print()
            sleep(1)
        
        except RepositoryError as re:
            print()
            print(re)
            print()
            sleep(1)
        
        except ValueError:
            print()
            print("ID trebuie sa fie numar!!!")
            print()
            sleep(1)
            
    def __uiPrintAllClients(self):
        print('----------------------------------------------------------------------------------------')
        
        clients = self.__clientService.get_all()
        
        for client in clients:
            print(client)
            
        print('----------------------------------------------------------------------------------------')
        
        sleep(1)
        
    def __uiPrintAllMovies(self):
        print('----------------------------------------------------------------------------------------')
        
        movies = self.__movieService.get_all()
        
        for movie in movies:
            print(movie)
            
        print('----------------------------------------------------------------------------------------')
        
        sleep(1)
        
    def __uiPrintAllRents(self):
        print('----------------------------------------------------------------------------------------')
        
        rents = self.__rentService.get_all()
        
        for rent in rents:
            print(rent)
            
        print('----------------------------------------------------------------------------------------')
        
        sleep(1)
    def __uiDeleteClient(self):
        try:
            self.__uiPrintAllClients()
            ID = int(input("Introduceti id-ul clientului pe care doriti sa il stergeti: "))
            self.__clientService.delete_client(ID)
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
            
        except DeletionError as de:
            print()
            print(de)
            print()
            sleep(1)
            
    def __uiDeleteMovie(self):
        try:
            self.__uiPrintAllMovies()
            title =input("Introduceti id-ul filmului pe care doriti sa il stergeti: ")
            self.__movieService.delete_movie(title)
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
            
        except DeletionError as de:
            print()
            print(de)
            print()
            sleep(1)
            
    def __uiRentReturn(self):
        try:
            self.__uiPrintAllRents()
            ID = int(input("Introduceti id-ul contractului de inchiriere: ")) 
            self.__rentService.rentReturn(ID)
            
            print()
            print("Filmul a fost returnat!")
            print()
            sleep(1)
        
        except RepositoryError as re:
            print()
            print(re)
            print()
            sleep(1)     
            
        except ValueError:
            print()
            print("ID trebuie sa fie numar!!!")
            print()
            sleep(1)  
    
    def __uiModifyClient(self):  
        try:
            self.__uiPrintAllClients()
            ID = int(input("Introduceti id-ul clientului pe care doriti sa il modificati: "))
            firstName = input("Introduceti prenumele: ")
            lastName = input("Introduceti numele de familie: ")
            CNP = int(input("Introduceti CNP: "))
            
            self.__clientService.modify_client(ID, firstName, lastName, CNP)
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
            self.__uiPrintAllMovies()
            title = input("Introduceti titlul filmului pe care doriti sa il modificati: ")
            newTitle = input("Introduceti noul titlu al filmului: ")
            description = input("Introduceti descrierea filmului: ")
            genre = input("Introduceti genul/genurile filmului: ")
            
            self.__movieService.modify_movie(title, newTitle, description, genre)
            print()
            print("Filmul cu titlul", title, "a fost modificat")
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
            
    def __uiModifyClientName(self):      
        try:
            self.__uiPrintAllClients()
            ID = int(input("Introduceti id-ul clientului pe care doriti sa il modificati: "))
            firstName = input("Introduceti prenumele: ")
            lastName = input("Introduceti numele de familie: ")
            
            self.__clientService.modify_client_name(ID, firstName, lastName)
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
            self.__uiPrintAllClients()
            ID = int(input("Introduceti id-ul clientului pe care doriti sa il modificati: "))
            CNP = int(input("Introduceti CNP: "))
            
            self.__clientService.modify_client_CNP(ID, CNP)
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
            self.__uiPrintAllMovies()
            title = input("Introduceti titlul filmului pe care doriti sa il modificati: ")
            newTitle = input("Introduceti titlul filmului: ")
            
            self.__movieService.modify_movie_title(title, newTitle)
            print()
            print("Titlul filmului", title, "a fost modificat in", newTitle)
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

    def __uiModifyMovieDescription(self):
        try:
            self.__uiPrintAllMovies()
            title = input("Introduceti titlul filmului pe care doriti sa il modificati: ")
            description = input("Introduceti descrierea filmului: ")
            
            self.__movieService.modify_movie_description(title, description)
            print()
            print("Filmul cu titlul", title, "a fost modificat")
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
    
    def __uiModifyMovieGenre(self):
        try:
            self.__uiPrintAllMovies()
            title = input("Introduceti titlul filmului pe care doriti sa il modificati: ")
            genre = input("Introduceti genul/genurile filmului: ")
            
            self.__movieService.modify_movie_genre(title, genre)
            print()
            print("Filmul cu titlul", title, "a fost modificat")
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
    
    def __uiNumberOfClients(self):
        print()
        print("Numarul de clienti:", self.__clientService.number_of_clients())
        print()
        sleep(1)
        
    def __uiNumberOfMovies(self):
        print()
        print("Numarul de filme:", self.__movieService.number_of_movies())
        print()
        sleep(1)
        
    def __uiNumberOfRents(self):
        print()
        print("Numarul de inchirieri:", self.__rentService.number_of_rents())
        print()
        sleep(1)
        
    def __uiFindClientByID(self):
        try:
            ID = int(input("Id-ul clientului: "))
            print()
            print("Clientul cautat:", self.__clientService.findByID(ID))
            print()
            sleep(1)
        
        except RepositoryError as re:
            print()
            print(re)
            print()
            sleep(1)
            
        except ValueError:
            print()
            print("ID trebuie sa fie numar!!!")
            print()
            sleep(1)
            
    def __uiFindMovieByTitle(self):
        try:
            title = input("Titlul filmului: ")
            print()
            print("Filmul cautat:", self.__movieService.findByTitle(title))
            print()
            sleep(1)
        
        except RepositoryError as re:
            print()
            print(re)
            print()
            sleep(1)
        
    def __uiGenerateClients(self):
        try:
            numberOfClients = int(input("Introduceti numarul de clienti ce urmeaza a fi generati: "))
            self.__clientService.generate_clients(numberOfClients)
            
            print()
            print("Au fost generati", numberOfClients, "clienti!")
            print()
            sleep(1)
        
        except ValueError as ve:
            print()
            print(ve)
            print()
            sleep(1)
            
    def __uiGenerateMovies(self):
        try:
            numberOfMovies = int(input("Introduceti numarul de filme ce urmeaza a fi generate: "))
            self.__movieService.generate_movies(numberOfMovies)
            
            print()
            print("Au fost generate", numberOfMovies, "filme!")
            print()
            sleep(1)
        
        except ValueError as ve:
            print()
            print(ve)
            print()
            sleep(1)
            
    def __uiMostRentedMovies(self):
        mostRentedMovies = self.__rentService.mostRentedMovies()
        print()
        print("Cele mai inchiriate filme")
        for movie in mostRentedMovies:
            print(self.__rentService.getMovieTitle(movie), '-', self.__rentService.getMovieRents(movie), "inchirieri")
        print()
        sleep(1)
    
    def __uiClientsOrderedByName(self):
        clientsOrderedByName = self.__rentService.ClientsOrderedByName()
        print()
        print("Clienti cu filme inchiriate(ordonati dupa nume): ")
        for client in clientsOrderedByName:
            print(self.__rentService.getClientName(client), '-', self.__rentService.getClientRents(client), "inchirieri")
        print()
        sleep(1)
        
    def __uiClientsOrderedByNumberOfRents(self):
        clientsOrderedByNumberOfRents = self.__rentService.ClientsOrderedByNumberOfRents()
        print()
        print("Clienti cu filme inchiriate(ordonati dupa numarul de filme inchiriate): ")
        for client in clientsOrderedByNumberOfRents:
            print(self.__rentService.getClientName(client), '-', self.__rentService.getClientRents(client), "inchirieri")
        print()
        sleep(1)
            
    def __uiTop30Clients(self):
        top30Clients = self.__rentService.Top30Clients()
        print()
        print("Top 30% Clienti cu cele mai multe filme inchiriate: ")
        for client in top30Clients:
            print(self.__rentService.getClientName(client), '-', self.__rentService.getClientRents(client), "inchirieri")
        print()
        sleep(1)
        
    def __uiTopClientsWithRentedMoviesByGenre(self):
        genre = input("Introduceti genul: ")
        topClientsWithRentedMoviesByGenre = self.__rentService.topClientsWithRentedMoviesByGenre(genre)
        print()
        print("Top clienti ce au inchiriat filme cu genul {}, ordonati dupa nr de inchirieri:".format(genre))
        for client in topClientsWithRentedMoviesByGenre:
            print(self.__rentService.getClientName(client), '-', self.__rentService.getClientRents(client), "inchirieri")
        print()
        sleep(1)
        
    def __generateMenu(self, menu):
        print()
        print("Alegeti una dintre urmatoarele optiuni:")
        for option in menu:
            print(option, menu[option][1])
        print()
        
    def run(self):
        while True:
            self.__generateMenu(self.__mainMenu)
        
            try:
                choice1 = int(input("Optiunea dorita: "))
            
                if choice1 == 0:
                    print()
                    print("Se inchide aplicatia...")
                    print()
                    sleep(1)
                    return
        
            
                submenu = self.__mainMenu[choice1][0]
                self.__generateMenu(submenu)
                choice2 = int(input("Optiunea dorita: "))
                submenu[choice2][0]()
        
            except KeyError:
                print()
                print("Optiunea nu exista!!!")  
                print()       
                sleep(1)   
                
            except ValueError:
                print()
                print("Optiunea trebuie sa fie un numar!!!")
                print()
                sleep(1)
        