'''
Created on Nov 6, 2018

Modul pentru gestionarea filmelor

@author: Silviu Anton
'''
from domain.entities import Movie
from errors_tests.errors import RepositoryError

class MovieController:
    
    def __init__(self, repository):
        self.__repository = repository
        self.__nextMovieID = 1
    
    def get_all(self):
        '''
        Descriprion: returneaza o lista cu toate filmele din repository-ul de filme
        '''
        return self.__repository.get_all()
    
    def getIDbyTitle(self,title):
        '''
        Description: calculeaza id-ul unui film plecand de la titlu
        
        In:
            - title - titlul filmului
        
        Out:
            - returneaza id-ul filmului sau 0 daca filmul nu exista in repository
        '''
        movies = self.__repository.get_all()
        for movie in movies:
            if movie.getTitle() == title:
                return movie.getID()
        return 0
    
    def findByTitle(self, title):
        '''
        Description: returneaza clientul cu ID-ul dat
        
        In:
            - title - numar intreg
        
        Out:
            - movie - filmul cautat
        '''
        ID = self.getIDbyTitle(title)
        return self.__repository.getItem(ID)
    
    def add_movie(self, title, description, genre):
        '''
        Description: adauga un film in repository-ul de filme, alocand-ui un ID
        
        In:
            - title - titlul filmului
            - description - descrierea filmului
            - genre - genul filmului
        
        Exceptions:
            - ridica ValueError daca exista deja filmul
        '''
        try: 
            movie = Movie(self.__nextMovieID, title, description, genre)
                  
            if movie in self.__repository.get_all():
                raise RepositoryError("Filmul exista deja!!!")
            
            self.__nextMovieID += 1
            self.__repository.store(movie.getID(), movie) 
            
        except Exception as ex:
            self.__nextMovieID -= 1
            raise ex
        
    def delete_movie(self, title):
        '''
        Description: sterge un film din repository-ul de filme
        '''
        ID = self.getIDbyTitle(title)
        self.__repository.delete(ID)
        
    def modify_movie(self, title, newTitle, description, genre):
        '''
        Description: modifica datele unui film
        
        In:
            - ID - id-ul filmului caruia ii modificam datele
            - title - titlu
            - description - descriere
            - genre - gen
        '''
        ID = self.getIDbyTitle(title)
        movie = self.__repository.getItem(ID)
        movie.setTitle(newTitle)
        movie.setGenre(genre)
        movie.setDescription(description)
            
        self.__repository.update(movie)
        
    def modify_movie_genre(self, title, genre):
        '''
        Description: modifica genul unui film
        
        In:
            - ID - id-ul filmului caruia ii modificam datele
            - genre - gen
        '''
        ID = self.getIDbyTitle(title)
        movie = self.__repository.getItem(ID)
        movie.setGenre(genre)
            
        self.__repository.update(movie)
        
    def modify_movie_description(self, title, description):
        '''
        Description: modifica descrierea unui film
        
        In:
            - ID - id-ul filmului caruia ii modificam datele
            - description - descriere
        '''
        ID = self.getIDbyTitle(title)
        movie = self.__repository.getItem(ID)
        movie.setDescription(description)
            
        self.__repository.update(movie)
        
    def modify_movie_title(self, title, newTitle):
        '''
        Description: modifica titlul unui film
        
        In:
            - ID - id-ul filmului caruia ii modificam datele
            - title - titlu
        '''
        ID = self.getIDbyTitle(title)
        movie = self.__repository.getItem(ID)
        movie.setTitle(newTitle)
            
        self.__repository.update(movie)
            
    def number_of_movies(self):
        return self.__repository.size()
        