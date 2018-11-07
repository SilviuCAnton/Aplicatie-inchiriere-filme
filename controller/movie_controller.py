'''
Created on Nov 6, 2018

Modul pentru gestionarea filmelor

@author: Silviu Anton
'''
from domain.entities import Movie

class MovieController:
    
    def __init__(self):
        self.__repository = {}
        self.__nextMovieID = 1
    
    def get_all(self):
        '''
        Descriprion: returneaza o lista cu toate filmele din repository-ul de filme
        '''
        return list(self.__repository.values())
    
    def add_movie(self, title, description, genre):
        '''
        Description: adauga un film in repository-ul de filme, alocand-ui un ID
        
        In:
            - title - titlul filmului
            - description - descrierea filmului
            - genre - genul filmului
        '''
        movie = Movie(self.__nextMovieID, title, description, genre)
        self.__nextMovieID +=1
        self.__repository[movie.getID()] = movie 
        
    def delete_movie(self, ID):
        '''
        Description: sterge un film din repository-ul de filme
        '''
        self.__repository.pop(ID)
        
    def modify_movie(self, ID, title, description, genre):
        '''
        Description: modifica datele unui film
        
        In:
            - ID - id-ul filmului caruia ii modificam datele
            - title - titlu
            - description - descriere
            - genre - gen
        '''
        self.__repository[ID].setTitle(title)
        self.__repository[ID].setGenre(genre)
        self.__repository[ID].setDescription(description)
        
    def modify_movie_genre(self, ID, genre):
        '''
        Description: modifica genul unui film
        
        In:
            - ID - id-ul filmului caruia ii modificam datele
            - genre - gen
        '''
        self.__repository[ID].setGenre(genre)
        
    def modify_movie_description(self, ID, description):
        '''
        Description: modifica descrierea unui film
        
        In:
            - ID - id-ul filmului caruia ii modificam datele
            - description - descriere
        '''
        self.__repository[ID].setDescription(description)
        
    def modify_movie_title(self, ID, title):
        '''
        Description: modifica titlul unui film
        
        In:
            - ID - id-ul filmului caruia ii modificam datele
            - title - titlu
        '''
        self.__repository[ID].setTitle(title)
        