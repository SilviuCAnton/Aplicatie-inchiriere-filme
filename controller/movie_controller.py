'''
Created on Nov 6, 2018

Modul pentru gestiunea filmelor

@author: Silviu Anton
'''
from domain.entities import Movie

class MovieController:
    
    def __init__(self):
        self.__repository = {}
        self.__nextMovieID = 1
    
    def get_all(self):
        return list(self.__repository.values())
    
    def add_movie(self, title, description, genre):
        movie = Movie(self.__nextMovieID, title, description, genre)
        self.__nextMovieID +=1
        self.__repository[movie.getID()] = movie 
        
    def delete_movie(self, ID):
        self.__repository.pop(ID)
        
    def modify_movie(self, ID, title, description, genre):
        self.__repository[ID].setTitle(title)
        self.__repository[ID].setGenre(genre)
        self.__repository[ID].setDescription(description)
        
    def modify_movie_genre(self, ID, genre):
        self.__repository[ID].setGenre(genre)
        
    def modify_movie_description(self, ID, description):
        self.__repository[ID].setDescription(description)
        
    def modify_movie_title(self, ID, title):
        self.__repository[ID].setTitle(title)
        