"""
For para listas
"""

def forList():
    for x in [1,2,3,4,5]:
        print(x)
    for x in ["uno","dos","tres", "cuatro", "cinco"]:
        print(x)

"""
For para rangos
"""

def forrange():
    for x in range(5):
        print(x)
    for y in range(-3,3):
        print(y)
    for z in range(-4, 2, 2):
        print(z)    
    for i in range(5,0,-1):
        print(i)   
        
"""
For para diccionarios
"""

def fordic():
    diccionario = {'manzana': 1, 'pera': 3, 'uva': 10}
    for clave, valor in diccionario.items():
        print(clave,"=",valor)

    for clave in diccionario.keys():
        print(clave)

    for valor in diccionario.values():
        print(valor)
    
    for idx,x in enumerate(diccionario):
        print("El indice {} del elemento {}".format(idx,x))



def elsefor():
    for x in range(5):
        print(x)
    else:
        print("Se acabo")

def elsefor2():
    for x in range(5):
        print(x)
        if x==2:
            break
    else:
        print("La cuenta se termino")

if __name__ == '__main__':
    #forList()
    #forrange()
    fordic()