'''
Created on Dec 15, 2018

Modul pentru algoritmii de sortare
    
@author: Silviu Anton
'''

def insertionSort(lst, *, key = lambda x: x, reverse = False):
    '''
    Descritpion: sorteaza o lista folosind algoritmul Insertion Sort si returneaza lista sortata
    
    In: lst - lista
    
    Out: result - lista rezultat
    '''
    result = lst[:]
    
    for i in range(1, len(result)): 
        element = result[i] 
  
        j = i-1
        while j >=0 and key(element) < key(result[j]): 
                result[j+1] = result[j] 
                j -= 1
        result[j+1] = element
    
    if reverse == True:
        result = list(reversed(result))    
        
    return result

def __getNextGap(gap): 
  
    gap = (gap * 10)//13
    if gap < 1: 
        return 1
    return gap 

def combSort(lst, *, key = lambda x: x, reverse = False):
    '''
    Descritpion: sorteaza o lista folosind algoritmul Comb Sort si returneaza lista sortata
    
    In: lst - lista
    
    Out: result - lista rezultat
    '''
    result = lst[:]
    lenght = len(result) 
  
    gap = lenght
  
    swapped = True
  
    while gap != 1 or swapped == True: 
        gap = __getNextGap(gap) 
  
        swapped = False
  
        for i in range(0, lenght - gap): 
            if key(result[i]) > key(result[i + gap]): 
                result[i], result[i + gap] = result[i + gap], result[i] 
                swapped = True
         
    if reverse == True:
        result = list(reversed(result))    
        
    return result
        