
'''
Created on Jan 5, 2019

@author: Silviu Anton
'''

class RecursiveMountainPermutationGenerator:
    '''
    Clasa pentru backtracking recursiv - generare permutari de tip munte
    '''
    
    def __init__(self):
        pass
    
    @staticmethod
    def __helper(x, myList, varf, result):
        '''
        Description: genereaza permutarile de tip munte ale unei liste de numere
        
        In: 
            - x - posibila solutie (La apel lista vida)
            - mylist - lista a carei permutari le generam
            - varf - True daca a fost gasit un posibil varf si False in caz contrar
        '''
        x.append(0) 
 
        for i in range(len(myList)):
            x[-1] = myList[i]
            isConsitent, varfGasit = RecursiveMountainPermutationGenerator.__consistent(x, varf, len(myList))

            if varfGasit:
                varf = True

         
            if isConsitent:
                if RecursiveMountainPermutationGenerator.__solution(x, myList, varf):
                    RecursiveMountainPermutationGenerator.__solutionFound(x, result)
                RecursiveMountainPermutationGenerator.__helper(x, myList, varf, result)
                varf = False
         
        x.pop()
    
    @staticmethod
    def generatePermutations(myList):
        '''
        Description: genereaza permutarile de tip munte ale unei liste date
        
        Formalizare: 
            - solutie candidat:
                x = (x1,x2,x3,...,xk), xi apartine (0,1,2,...len(mylist)-1)
                
            - conditie consistent:
                x = (x1,x2,x3,...,xk) este consistent daca:
                    - xi != xj, oricare ar fi i, j
                    - xi > xj daca nu am trecut de varf (varf = False), unde i>j
                    - xi < xj daca am trecut de varf (varf = True), unde i>j si len(x)> 2
            
            - conditie solutie:
                x = (x1,x2,x3,...,xk) este solutie daca este consistent, len(x) = len(myList) si am trecut de varf (varf = True)
        
        In: 
            - mylist - lista a carei permutari le generam
            
        Out:
             - result - lista de solutii
        '''
        varf = False
        x = []
        result = []
        
        RecursiveMountainPermutationGenerator.__helper(x, myList, varf, result)
        return result
        
    
    @staticmethod
    def __consistent(x, varf, dim):
        '''
        Description: returneaza True/False daca elementul propus in solutie corespunde cerintei si True/False daca am trecut de varf
        
        In: 
            - x - solutia construita
            - varf - True daca am gasit un posiblil var si False in caz contrar
            - dim - dimensiunea listei a carei permutari le construim
            
        Out:
            - True/False - daca ultimul element ales corespunde cerintei
            - varf - True daca am gasit un posiblil var si False in caz contrar
        '''
        if x[-1] in x[:-1]: return False, varf
        if len(x) > dim: return False, varf
        if len(x) > 1 and varf == True and x[-1] > x[-2]: return False, varf
        if len(x) == 2 and varf == False and x[-1] < x[-2]: return False, varf
        if len(x) > 2 and varf == False and x[-1] < x[-2]: return True, True
        return True, varf
    
    @staticmethod
    def __solution(x, myList, varf):
        '''
        Description: verifica daca am gasit o solutie sau nu
        
        In: 
            - x - solutia construita
            - myList - lista a carei permutari le construim
            - varf - True daca am gasit un posiblil var si False in caz contrar
            
        Out:
            - True/False - daca am gasit o solutie sau nu
        '''
        return len(x) == len(myList) and varf == True

    @staticmethod
    def __solutionFound(x, resultList):
        '''
        Description: adauga la rezultat o solutie
        
        In: - x - solutia
        '''
        resultList.append(x[:])
        

class IterativeMountainPermutationGenerator:
    '''
    Clasa pentru backtracking iterativ - generare permutari de tip munte
    '''
    __result = []
    
    def __init__(self):
        pass
    
    @staticmethod
    def __helper(x, myList, varf, result):
        '''
        Description: genereaza permutarile de tip munte ale unei liste de numere
        
        In: 
            - x - posibila solutie (La apel lista vida)
            - mylist - lista a carei permutari le generam
            - varf - True daca a fost gasit un posibil varf si False in caz contrar
        '''
        varfGasit = False
        x=[-1]
        
        while len(x)>0:
            choosed = False
            
            while not choosed and x[-1] < len(myList) - 1:
                x[-1] = x[-1] + 1 
                choosed, varfGasit = IterativeMountainPermutationGenerator.__consistent(x, myList, varf)
    
            if varfGasit:
                varf = True
                
            if choosed:
                if IterativeMountainPermutationGenerator.__solution(x, myList, varf):
                    IterativeMountainPermutationGenerator.__solutionFound(x, myList, result)
                x.append(-1)
                
            else:
                x = x[:-1]
                varf = False
    
    @staticmethod
    def generatePermutations(myList):
        '''
        Description: genereaza permutarile de tip munte ale unei liste de numere
        
        Formalizare: 
            - solutie candidat:
                x = (x1,x2,x3,...,xk), xi apartine (0,1,2,...len(mylist)-1)
                
            - conditie consistent:
                x = (x1,x2,x3,...,xk) este consistent daca:
                    - xi != xj, oricare ar fi i, j
                    - xi > xj daca nu am trecut de varf (varf = False), unde i>j
                    - xi < xj daca am trecut de varf (varf = True), unde i>j si len(x)> 2
            
            - conditie solutie:
                x = (x1,x2,x3,...,xk) este solutie daca este consistent, len(x) = len(myList) si am trecut de varf (varf = True)
                
                
        In: 
            - mylist - lista a carei permutari le generam
        Out:
            - result - lista rezultat
        '''
        varf = False
        x = []
        result = []
        
        IterativeMountainPermutationGenerator.__helper(x, myList, varf, result)
        return result
 
    @staticmethod
    def __consistent(x, myList, varf):
        '''
        Description: returneaza True/False daca elementul propus in solutie corespunde cerintei si True/False daca am trecut de varf
        
        In: 
            - x - solutia construita
            - myList - lista a carei permutari le construim
            - varf - True daca am gasit un posiblil var si False in caz contrar
            
            
        Out:
            - True/False - daca ultimul element ales corespunde cerintei
            - varf - True daca am gasit un posiblil var si False in caz contrar
        '''
        if x[-1] in x[:-1]: return False, varf
        if len(x) > len(myList): return False, varf
        if len(x) > 1 and varf == True and myList[x[-1]] > myList[x[-2]]: return False, varf
        if len(x) == 2 and varf == False and myList[x[-1]] < myList[x[-2]]: return False, varf
        if len(x) > 2 and varf == False and myList[x[-1]] < myList[x[-2]]: return True, True
        return True, varf
    
    @staticmethod
    def __solution(x, myList, varf):
        '''
        Description: verifica daca am gasit o solutie sau nu
        
        In: 
            - x - solutia construita
            - myList - lista a carei permutari le construim
            - varf - True daca am gasit un posiblil var si False in caz contrar
            
        Out:
            - True/False - daca am gasit o solutie sau nu
        '''
        return len(x) == len(myList) and varf == True
    
    @staticmethod
    def __solutionFound(x, myList, resultList):
        '''
        Description - adauga o solutie la rezultat
        
        In: 
            - x - solutia
            - myList - lista a carei permutari le construim
        '''
        result = []
        for item in x:
            result.append(myList[item])
        resultList.append(result)
