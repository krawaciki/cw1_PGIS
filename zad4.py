import os
os.system('CLS')

def elim_dupl (lista):
    return list(set(lista))
    #list zamienia kolekcjê w listê
    #tworzy kolekcjê unikalnych elementów

print(elim_dupl(['kot', 'chomik', 'ryba','kot' ,'koza', 'chomik', 'chomik']))
