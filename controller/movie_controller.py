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
    
    def findByID(self, ID):
        '''
        Description: returneaza clientul cu ID-ul dat
        
        In:
            - ID - numar intreg
        
        Out:
            - movie - filmul cautat
        '''
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
        
    def delete_movie(self, ID):
        '''
        Description: sterge un film din repository-ul de filme
        '''
        self.__repository.delete(ID)
        
    def modify_movie(self, ID, title, description, genre):
        '''
        Description: modifica datele unui film
        
        In:
            - ID - id-ul filmului caruia ii modificam datele
            - title - titlu
            - description - descriere
            - genre - gen
        '''
        movie = self.__repository.getItem(ID)
        movie.setTitle(title)
        movie.setGenre(genre)
        movie.setDescription(description)
            
        self.__repository.update(movie)
        
    def modify_movie_genre(self, ID, genre):
        '''
        Description: modifica genul unui film
        
        In:
            - ID - id-ul filmului caruia ii modificam datele
            - genre - gen
        '''
        movie = self.__repository.getItem(ID)
        movie.setGenre(genre)
            
        self.__repository.update(movie)
        
    def modify_movie_description(self, ID, description):
        '''
        Description: modifica descrierea unui film
        
        In:
            - ID - id-ul filmului caruia ii modificam datele
            - description - descriere
        '''
        movie = self.__repository.getItem(ID)
        movie.setDescription(description)
            
        self.__repository.update(movie)
        
    def modify_movie_title(self, ID, title):
        '''
        Description: modifica titlul unui film
        
        In:
            - ID - id-ul filmului caruia ii modificam datele
            - title - titlu
        '''
        movie = self.__repository.getItem(ID)
        movie.setTitle(title)
            
        self.__repository.update(movie)
            
    def number_of_movies(self):
        return self.__repository.size()
        