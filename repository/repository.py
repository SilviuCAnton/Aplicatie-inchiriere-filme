'''
Created on Nov 6, 2018

Modul pentru stocarea clientilor/filmelor

@author: Silviu Anton
'''

class Repository:
    
    def __init__(self):
        self.__items = {}
        
    def save(self, item):
        self.__items[item.getID()] = item   
        
    def delete(self, ID):
        self.__items.pop(ID)
        
    def get_all(self):
        return list(self.__items.values())