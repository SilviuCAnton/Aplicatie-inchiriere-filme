'''
Created on Nov 8, 2018

Modul pentru validatoare

@author: Silviu Anton
'''
from errors_tests.errors import ValidError

class ClientValidator:
    '''
    Description: Valideaza un client
    
    In: 
        - client - clientul de validat
    
    Exceptions:
        - ridica ValidError daca CNP-ul sau numele nu este valid
    '''
    @staticmethod
    def validate(client):      
        if not 1000000000000<client.getCNP()< 10000000000000:
            raise ValidError("CNP-ul trebuie sa aiba exact 13 cifre!!!")
        
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
    @staticmethod
    def validate(movie):
        if movie.getTitle() == "":
            raise ValidError("Titlu nu poate fi vid!!!")
        
        description = movie.getDescription()
        
        if not description[0].isalpha():
            raise ValidError("Trebuie ca descrierea sa inceapa cu o litera mica")
        
        if description[0]. lower() != description[0] or description[0] == " ":
            raise ValidError("Trebuie ca descrierea sa inceapa cu litera mica")
        
        for ch in range(1, len(description)-1):
            if not (description[ch].isdigit() or description[ch].isalpha() or description[ch].isspace()):
                raise ValidError("Toate caracterele trebuie sa fie litere sau cifre")
            
            elif description[ch] == " " and description[ch+1].isalpha() == False:
                raise ValidError("Dupa spatiu trebuie sa urmeze un cuvant")
            
            elif description[ch] == " " and description[ch+1] == " ":
                raise ValidError("Trebuie ca descrierea sa nu aiba doua spatii consecutive")
            
            elif description[ch] == " " and description[ch+1] != description[ch+1].lower():
                raise ValidError("Trebuie ca descrierea sa nu inceapa cuvant nou cu litera mare")
                