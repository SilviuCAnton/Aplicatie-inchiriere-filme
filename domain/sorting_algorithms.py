'''
Created on Dec 15, 2018

Modul pentru algoritmii de sortare
    
@author: Silviu Anton
'''
from copy import deepcopy

def insertionSort(lst, *, key = lambda x: x, cmp = lambda x, y: x - y, reverse = False):
    '''
    Descritpion: sorteaza o lista folosind algoritmul Insertion Sort si returneaza lista sortata
    
    In: 
        - lst - lista
        - key - cheia dupa care se face sortarea
        - cmp - criteriul de comparatie
        - reverse - specifica daca sortarea se face invers sau nu
    
    Out: result - lista rezultat
    '''
    result = deepcopy(lst)
    
    for i in range(1, len(result)): 
        element = result[i] 
  
        j = i-1
        while j >=0 and cmp(key(element), key(result[j])) < 0: 
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

def combSort(lst, *, key = lambda x: x, cmp = lambda x, y: x - y, reverse = False):
    '''
    Descritpion: sorteaza o lista folosind algoritmul Comb Sort si returneaza lista sortata
    
    In: 
        - lst - lista
        - key - cheia dupa care se face sortarea
        - cmp - criteriul de comparatie
        - reverse - specifica daca sortarea se face invers sau nu
    
    Out: result - lista rezultat
    '''
    result = deepcopy(lst)
    lenght = len(result) 
  
    gap = lenght
  
    swapped = True
  
    while gap != 1 or swapped == True: 
        gap = __getNextGap(gap) 
  
        swapped = False
  
        for i in range(0, lenght - gap): 
            if cmp(key(result[i]), key(result[i + gap])) > 0: 
                result[i], result[i + gap] = result[i + gap], result[i] 
                swapped = True
         
    if reverse == True:
        result = list(reversed(result))    
        
    return result

def mergeSort(lst, key = lambda x: x, cmp = lambda x, y: x - y, reverse = False):
    myList = deepcopy(lst)
    
    def helper(arr): 
        if len(arr) >1: 
            mid = len(arr)//2 #Finding the mid of the array 
            L = arr[:mid] # Dividing the array elements  
            R = arr[mid:] # into 2 halves 
      
            helper(L) # Sorting the first half 
            helper(R) # Sorting the second half 
      
            i = j = k = 0
              
            # Copy data to temp arrays L[] and R[] 
            while i < len(L) and j < len(R): 
                if cmp(key(L[i]), key(R[j])) < 0: 
                    arr[k] = L[i] 
                    i+=1
                else: 
                    arr[k] = R[j] 
                    j+=1
                k+=1
              
            # Checking if any element was left 
            while i < len(L): 
                arr[k] = L[i] 
                i+=1
                k+=1
              
            while j < len(R): 
                arr[k] = R[j] 
                j+=1
                k+=1
                
    helper(myList)
    
    if reverse == True:
        myList = list(reversed(myList))
        
    return myList
        