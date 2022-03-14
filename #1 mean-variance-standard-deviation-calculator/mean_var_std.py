import numpy as np

def calculate(l):

  if  len(l) != 9:   
    raise ValueError("List must contain nine numbers.")
  else:
    # Getting the array out of the list
    arr = np.array([[l[i],l[i+1],l[i+2]] for i in [0,3,6]]) 
    #Defining the calculations dictionary
    calculations ={}

    #Dictionary Entries
    calculations['mean'] = [list(np.mean(arr,axis = 0)),list(np.mean(arr,axis = 1)), np.mean(arr)]
    calculations['variance'] = [list(np.var(arr,axis = 0)),list(np.var(arr,axis = 1)), np.var(arr)]
    calculations['standard deviation'] = [list(np.std(arr,axis = 0)),list(np.std(arr,axis = 1)), np.std(arr)]
    calculations['max'] = [list(np.max(arr,axis = 0)),list(np.max(arr,axis = 1)), np.max(arr)]
    calculations['min'] = [list(np.min(arr,axis = 0)),list(np.min(arr,axis = 1)), np.min(arr)]
    calculations['sum'] = [list(np.sum(arr,axis = 0)),list(np.sum(arr,axis = 1)), np.sum(arr)]
  
    return calculations