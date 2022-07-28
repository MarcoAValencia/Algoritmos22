import random
 
def randomGen(T):
 lista=[]
 for i in range (0,T):
  lista.append(random.randint(0,255))
 return lista

def randomSort(T):
 lista=randomGen(T)
 lista.sort()
 return lista
 
def randomInvertSort(T):
 lista=randomGen(T)
 lista.sort(reverse=True)
 return lista
