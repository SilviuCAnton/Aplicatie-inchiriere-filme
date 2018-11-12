'''
Created on Nov 8, 2018

Modul pentru validatoare

@author: Silviu Anton
'''
from errors_validators_tests.errors import ValidError

class ClientValidator:
    '''
    Description: Valideaza un client
    
    In: 
        - client - clientul de validat
    
    Exceptions:
        - ridica ValidError daca CNP-ul sau numele nu este valid
    '''
    
    def validate(self, client):      
        if not 1000000000000<client.getCNP()< 10000000000000:
            raise ValidError("CNP-ul trebuie sa aiba exact 14 cifre!!!")
        
        if client.getName() == " ":
            raise ValidError("Nume nu poate fi vid!!!")
        
class MovieValidator:
    '''
    Description: Valideaza un film
    
    In: 
        - movie - filmul de validat
    
    Exceptions:
        - ridica ValidError daca titlul filmului nu e valid
    '''
    
    def validate(self, movie):
        if movie.getTitle() == "":
            raise ValidError("Titlu nu poate fi vid!!!")
        