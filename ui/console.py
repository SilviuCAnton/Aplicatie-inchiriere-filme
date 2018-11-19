'''
Created on Nov 11, 2018

Modul pentru interactiunea cu utilizatorul

@author: Silviu Anton
'''
from errors_tests.errors import RepositoryError, ValidError
from time import sleep

class Console:
    
    def __init__(self, clientController, movieController, rentController):
        self.__clientController = clientController
        self.__movieController = movieController
        self.__rentController = rentController
        
        self.__submenuClient = {1: (self.__uiAddClient, "Adaugati un client"),
                                2: (self.__uiPrintAllClients, "Afisare clientii"),
                                3: (self.__uiFindClientByID, "Gaseste client dupa ID"),
                                4: (self.__uiDeleteClient, "Stergeti un client"),
                                5: (self.__uiModifyClient, "Modificati un client"),
                                6: (self.__uiModifyClientName, "Modificati numele unui client"),
                                7: (self.__uiModifyClientCNP, "Modificati CNP-ul unui client"),
                                8: (self.__uiNumberOfClients, "Afisare numar clienti")}
        
        self.__submenuMovie = {1: (self.__uiAddMovie, "Adaugati un film"),
                               2: (self.__uiPrintAllMovies, "Afisare filme"),
                               3: (self.__uiFindMovieByTitle, "Gaseste film dupa titlu"),
                               4: (self.__uiDeleteMovie, "Stergeti un film"),
                               5: (self.__uiModifyMovie, "Modificati un film"),
                               6: (self.__uiModifyMovieTitle, "Modificati titlul unui film"),
                               7: (self.__uiModifyMovieDescription, "Modificati descrierea unui film"),
                               8: (self.__uiModifyMovieGenre, "Modificati genul unui film"),
                               9: (self.__uiNumberOfMovies, "Afisare numar filme")}
        
        self.__submenuInchirieri = {1: (self.__uiAddRent, "Adaugati o inchiriere"),
                                    2: (self.__uiPrintAllRents, "Afisare inchirieri"),
                                    3: (self.__uiRentReturn, "Returnare film"),
                                    4: (self.__uiNumberOfRents, "Numar de inchirieri")}
        
        self.__mainMenu = {1: (self.__submenuClient, "Operatii clienti"),
                           2: (self.__submenuMovie, "Operatii filme"),
                           3: (self.__submenuInchirieri, "Operatii inchirieri"),
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
            
    def __uiAddRent(self):
        try:
            self.__uiPrintAllClients()
            idClient = int(input("Introduceti ID-ul clientului: "))
            client = self.__clientController.findByID(idClient)

            self.__uiPrintAllMovies()
            title = input("Introcueti titlul filmului: ")
            movie = self.__movieController.findByTitle(title)
            
            self.__rentController.add_rent(client, movie)
            
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
        
        clients = self.__clientController.get_all()
        
        for client in clients:
            print(client)
            
        print('----------------------------------------------------------------------------------------')
        
        sleep(1)
        
    def __uiPrintAllMovies(self):
        print('----------------------------------------------------------------------------------------')
        
        movies = self.__movieController.get_all()
        
        for movie in movies:
            print(movie)
            
        print('----------------------------------------------------------------------------------------')
        
        sleep(1)
        
    def __uiPrintAllRents(self):
        print('----------------------------------------------------------------------------------------')
        
        rents = self.__rentController.get_all()
        
        for rent in rents:
            print(rent)
            
        print('----------------------------------------------------------------------------------------')
        
        sleep(1)
    def __uiDeleteClient(self):
        try:
            self.__uiPrintAllClients()
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
            self.__uiPrintAllMovies()
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
            
    def __uiRentReturn(self):
        try:
            self.__uiPrintAllRents()
            ID = int(input("Introduceti id-ul contractului de inchiriere: ")) 
            self.__rentController.rentReturn(ID)
            
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
            self.__uiPrintAllMovies()
            title = input("Introduceti titlul filmului pe care doriti sa il modificati: ")
            newTitle = input("Introduceti noul titlu al filmului: ")
            description = input("Introduceti descrierea filmului: ")
            genre = input("Introduceti genul/genurile filmului: ")
            
            self.__movieController.modify_movie(title, newTitle, description, genre)
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
            self.__uiPrintAllClients()
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
            self.__uiPrintAllMovies()
            title = input("Introduceti titlul filmului pe care doriti sa il modificati: ")
            newTitle = input("Introduceti titlul filmului: ")
            
            self.__movieController.modify_movie_title(title, newTitle)
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
            
            self.__movieController.modify_movie_description(title, description)
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
            
            self.__movieController.modify_movie_genre(title, genre)
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
        print("Numarul de clienti:", self.__clientController.number_of_clients())
        print()
        sleep(1)
        
    def __uiNumberOfMovies(self):
        print()
        print("Numarul de filme:", self.__movieController.number_of_movies())
        print()
        sleep(1)
        
    def __uiNumberOfRents(self):
        print()
        print("Numarul de inchirieri:", self.__rentController.number_of_rents())
        print()
        sleep(1)
        
    def __uiFindClientByID(self):
        try:
            ID = int(input("Id-ul clientului: "))
            print()
            print("Clientul cautat:", self.__clientController.findByID(ID))
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
            print("Filmul cautat:", self.__movieController.findByTitle(title))
            print()
            sleep(1)
        
        except RepositoryError as re:
            print()
            print(re)
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
        