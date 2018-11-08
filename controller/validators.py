'''
Created on Nov 8, 2018

Modul pentru validatoare

@author: Silviu Anton
'''

class ClientValidator:
    
    def validate(self, client):      
        if not 1000000000000<client.getCNP()< 10000000000000:
            raise ValueError("CNP-ul trebuie sa aiba exact 14 cifre!!!")
        
        if client.getName() == "":
            raise ValueError("Nume nu poate fi vid!!!")
        
class MovieValidator:
    
    def validate(self, movie):
        if movie.getTitle() == "":
            raise ValueError("Titlu nu poate fi vid!!!")