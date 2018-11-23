'''
Created on Nov 11, 2018

Modul pentru definirea exceptiilor

@author: Silviu Anton
'''

class RepositoryError(Exception):
    pass

class ValidError(Exception):
    pass

class DuplicateError(RepositoryError):
    pass

class IdNotFoundError(RepositoryError):
    pass

class DeletionError(Exception):
    pass