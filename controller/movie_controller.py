'''
Created on Nov 6, 2018

Modul pentru gestiunea filmelor

@author: Silviu Anton
'''
from domain.entities import Movie

class MovieController:
    
    def __init__(self, repository):
        self.__repository = repository
    
    def get_all(self):
        return self.__repository.get_all()
    
    def add_movie(self, ID, title, description, genre):
        movie = Movie(ID, title, description, genre)
        self.__repository.save(movie)    
        
    def delete_movie(self, ID):
        self.__repository.delete(ID)