import os
os.system('CLS')

def elim_dupl (lista):
    return list(set(lista))
    #list zamienia kolekcj� w list�
    #tworzy kolekcj� unikalnych element�w

print(elim_dupl(['kot', 'chomik', 'ryba','kot' ,'koza', 'chomik', 'chomik']))
