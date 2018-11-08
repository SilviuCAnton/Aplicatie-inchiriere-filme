'''
Created on Nov 6, 2018

Modul pentru gestionarea filmelor

@author: Silviu Anton
'''
from domain.entities import Movie

class MovieController:
    
    def __init__(self, repository, validator):
        self.__repository = repository
        self.__validator = validator
        self.__nextMovieID = 1
    
    def get_all(self):
        '''
        Descriprion: returneaza o lista cu toate filmele din repository-ul de filme
        '''
        return self.__repository.get_all()
    
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
        movie = Movie(self.__nextMovieID, title, description, genre)
        
        try:
            self.__validator.validate(movie)
            
            if movie in self.__repository.get_all():
                raise ValueError("Filmul exista deja!!!")
            
            self.__nextMovieID += 1
            self.__repository.store(movie.getID(), movie) 
        
        except ValueError as err:
            print()
            print(err)
            print()
        
    def delete_movie(self, ID):
        '''
        Description: sterge un film din repository-ul de filme
        '''
        try:
            self.__repository.delete(ID)
            
        except ValueError as err:
            print(err)
        
    def modify_movie(self, ID, title, description, genre):
        '''
        Description: modifica datele unui film
        
        In:
            - ID - id-ul filmului caruia ii modificam datele
            - title - titlu
            - description - descriere
            - genre - gen
        '''
        try:
            movie = self.__repository.getItem(ID)
            movie.setTitle(title)
            movie.setGenre(genre)
            movie.setDescription(description)
            
            self.__validator.validate(movie)
            self.__repository.update(movie)
        
        except ValueError as err:
            print()
            print(err)
            print()
        
    def modify_movie_genre(self, ID, genre):
        '''
        Description: modifica genul unui film
        
        In:
            - ID - id-ul filmului caruia ii modificam datele
            - genre - gen
        '''
        try:
            movie = self.__repository.getItem(ID)
            movie.setGenre(genre)
            
            self.__validator.validate(movie)
            self.__repository.update(movie)
        
        except ValueError as err:
            print()
            print(err)
            print()
        
    def modify_movie_description(self, ID, description):
        '''
        Description: modifica descrierea unui film
        
        In:
            - ID - id-ul filmului caruia ii modificam datele
            - description - descriere
        '''
        try:
            movie = self.__repository.getItem(ID)
            movie.setDescription(description)
            
            self.__validator.validate(movie)
            self.__repository.update(movie)
        
        except ValueError as err:
            print()
            print(err)
            print()
        
    def modify_movie_title(self, ID, title):
        '''
        Description: modifica titlul unui film
        
        In:
            - ID - id-ul filmului caruia ii modificam datele
            - title - titlu
        '''
        try:
            movie = self.__repository.getItem(ID)
            movie.setTitle(title)
            
            self.__validator.validate(movie)
            self.__repository.update(movie)
        
        except ValueError as err:
            print()
            print(err)
            print()
        