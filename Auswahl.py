import numpy as np
import random 
import matplotlib.pyplot as plt
import copy


## 4 for "Sehr gerne" 2 for "gerne"  0 for "egal" -2 for "nicht gerne" -6 for "gar nicht gerne"

teams = 15
projects = 15
Iterations = 1000

constellation = []
epsilons = []



groups =[
  {"1": 0 ,"2": 0 ,"3": 4 ,"4": 0 ,"5": 0 ,"6":  0,"7": 0 ,"8": 0 ,"9": 0 ,"10": 2 ,"11": 0 ,"12": 0 ,"13": 0 ,"14": 0 ,"15": 6 }
, {"1": 4 ,"2": 0 ,"3": 0 ,"4": 6 ,"5": 0 ,"6":  2,"7": 0 ,"8": 0 ,"9": 0 ,"10": 0 ,"11": 0 ,"12": 0 ,"13": 0 ,"14": 0 ,"15": 0 }
, {"1": 4 ,"2": 0 ,"3": 0 ,"4": 6 ,"5": 0 ,"6":  2,"7": 0 ,"8": 0 ,"9": 0 ,"10": 0 ,"11": 0 ,"12": 0 ,"13": 0 ,"14": 0 ,"15": 0 }
, {"1": 0 ,"2": 2 ,"3": 6 ,"4": 0 ,"5": 0 ,"6":  0,"7": 0 ,"8": 0 ,"9": 0 ,"10": 0 ,"11": 4 ,"12": 0 ,"13": 0 ,"14": 0 ,"15": 0 }
, {"1": 4 ,"2": 2 ,"3": 0 ,"4": 0 ,"5": 0 ,"6":  0,"7": 0 ,"8": 6 ,"9": 0 ,"10": 0 ,"11": 0 ,"12": 0 ,"13": 0 ,"14": 0 ,"15": 0 }
, {"1": 4 ,"2": 2 ,"3": 0 ,"4": 6 ,"5": 0 ,"6":  0,"7": 0 ,"8": 0 ,"9": 0 ,"10": 0 ,"11": 0 ,"12": 0 ,"13": 0 ,"14": 0 ,"15": 0 }
, {"1": 2 ,"2": 0 ,"3": 4 ,"4": 0 ,"5": 0 ,"6":  0,"7": 0 ,"8": 0 ,"9": 0 ,"10": 0 ,"11": 0 ,"12": 6 ,"13": 0 ,"14": 0 ,"15": 0 }
, {"1": 0 ,"2": 0 ,"3": 0 ,"4": 6 ,"5": 0 ,"6":  0,"7": 0 ,"8": 4 ,"9": 0 ,"10": 0 ,"11": 0 ,"12": 2 ,"13": 0 ,"14": 0 ,"15": 0 }
, {"1": 0 ,"2": 0 ,"3": 6 ,"4": 2 ,"5": 0 ,"6":  0,"7": 0 ,"8": 4 ,"9": 0 ,"10": 0 ,"11": 0 ,"12": 0 ,"13": 0 ,"14": 0 ,"15": 0 }
, {"1": 0 ,"2": 0 ,"3": 6 ,"4": 0 ,"5": 0 ,"6":  4,"7": 0 ,"8": 2 ,"9": 0 ,"10": 0 ,"11": 0 ,"12": 0 ,"13": 0 ,"14": 0 ,"15": 0 }
, {"1": 6 ,"2": 0 ,"3": 0 ,"4": 0 ,"5": 0 ,"6":  0,"7": 0 ,"8": 0 ,"9": 0 ,"10": 0 ,"11": 0 ,"12": 2 ,"13": 0 ,"14": 0 ,"15": 4 }
, {"1": 0 ,"2": 0 ,"3": 6 ,"4": 2 ,"5": 0 ,"6":  0,"7": 0 ,"8": 0 ,"9": 0 ,"10": 0 ,"11": 0 ,"12": 0 ,"13": 0 ,"14": 0 ,"15": 4 }
, {"1": 0 ,"2": 0 ,"3": 6 ,"4": 0 ,"5": 0 ,"6":  0,"7": 0 ,"8": 2 ,"9": 0 ,"10": 0 ,"11": 0 ,"12": 0 ,"13": 0 ,"14": 0 ,"15": 4 }
, {"1": 2 ,"2": 0 ,"3": 0 ,"4": 4 ,"5": 0 ,"6":  0,"7": 0 ,"8": 6 ,"9": 0 ,"10": 0 ,"11": 0 ,"12": 0 ,"13": 0 ,"14": 0 ,"15": 0 }
, {"1": 0 ,"2": 0 ,"3": 0 ,"4": 0 ,"5": 0 ,"6":  0,"7": 0 ,"8": 0 ,"9": 0 ,"10": 0 ,"11": 0 ,"12": 0 ,"13": 0 ,"14": 0 ,"15": 6 }
]


group1 = {"1": 0 ,"2": 0 ,"3": 4 ,"4": 0 ,"5": 0 ,"6":  0,"7": 0 ,"8": 0 ,"9": 0 ,"10": 2 ,"11": 0 ,"12": 0 ,"13": 0 ,"14": 0 ,"15": 6 }
group2 = {"1": 4 ,"2": 0 ,"3": 0 ,"4": 6 ,"5": 0 ,"6":  2,"7": 0 ,"8": 0 ,"9": 0 ,"10": 0 ,"11": 0 ,"12": 0 ,"13": 0 ,"14": 0 ,"15": 0 }
group3 = {"1": 4 ,"2": 0 ,"3": 0 ,"4": 6 ,"5": 0 ,"6":  2,"7": 0 ,"8": 0 ,"9": 0 ,"10": 0 ,"11": 0 ,"12": 0 ,"13": 0 ,"14": 0 ,"15": 0 }
group4 = {"1": 0 ,"2": 2 ,"3": 6 ,"4": 0 ,"5": 0 ,"6":  0,"7": 0 ,"8": 0 ,"9": 0 ,"10": 0 ,"11": 4 ,"12": 0 ,"13": 0 ,"14": 0 ,"15": 0 }
group5 = {"1": 4 ,"2": 2 ,"3": 0 ,"4": 0 ,"5": 0 ,"6":  0,"7": 0 ,"8": 6 ,"9": 0 ,"10": 0 ,"11": 0 ,"12": 0 ,"13": 0 ,"14": 0 ,"15": 0 }
group6 = {"1": 4 ,"2": 2 ,"3": 0 ,"4": 6 ,"5": 0 ,"6":  0,"7": 0 ,"8": 0 ,"9": 0 ,"10": 0 ,"11": 0 ,"12": 0 ,"13": 0 ,"14": 0 ,"15": 0 }
group7 = {"1": 2 ,"2": 0 ,"3": 4 ,"4": 0 ,"5": 0 ,"6":  0,"7": 0 ,"8": 0 ,"9": 0 ,"10": 0 ,"11": 0 ,"12": 6 ,"13": 0 ,"14": 0 ,"15": 0 }
group8 = {"1": 0 ,"2": 0 ,"3": 0 ,"4": 6 ,"5": 0 ,"6":  0,"7": 0 ,"8": 4 ,"9": 0 ,"10": 0 ,"11": 0 ,"12": 2 ,"13": 0 ,"14": 0 ,"15": 0 }
group9 = {"1": 0 ,"2": 0 ,"3": 6 ,"4": 2 ,"5": 0 ,"6":  0,"7": 0 ,"8": 4 ,"9": 0 ,"10": 0 ,"11": 0 ,"12": 0 ,"13": 0 ,"14": 0 ,"15": 0 }
group10 = {"1": 0 ,"2": 0 ,"3": 6 ,"4": 0 ,"5": 0 ,"6":  4,"7": 0 ,"8": 2 ,"9": 0 ,"10": 0 ,"11": 0 ,"12": 0 ,"13": 0 ,"14": 0 ,"15": 0 }
group11 = {"1": 6 ,"2": 0 ,"3": 0 ,"4": 0 ,"5": 0 ,"6":  0,"7": 0 ,"8": 0 ,"9": 0 ,"10": 0 ,"11": 0 ,"12": 2 ,"13": 0 ,"14": 0 ,"15": 4 }
group12 = {"1": 0 ,"2": 0 ,"3": 6 ,"4": 2 ,"5": 0 ,"6":  0,"7": 0 ,"8": 0 ,"9": 0 ,"10": 0 ,"11": 0 ,"12": 0 ,"13": 0 ,"14": 0 ,"15": 4 }
group13 = {"1": 0 ,"2": 0 ,"3": 6 ,"4": 0 ,"5": 0 ,"6":  0,"7": 0 ,"8": 2 ,"9": 0 ,"10": 0 ,"11": 0 ,"12": 0 ,"13": 0 ,"14": 0 ,"15": 4 }
group14 = {"1": 2 ,"2": 0 ,"3": 0 ,"4": 4 ,"5": 0 ,"6":  0,"7": 0 ,"8": 6 ,"9": 0 ,"10": 0 ,"11": 0 ,"12": 0 ,"13": 0 ,"14": 0 ,"15": 0 }
group15 = {"1": 0 ,"2": 0 ,"3": 0 ,"4": 0 ,"5": 0 ,"6":  0,"7": 0 ,"8": 0 ,"9": 0 ,"10": 0 ,"11": 0 ,"12": 0 ,"13": 0 ,"14": 0 ,"15": 6 }
group16 = {"1": 2 ,"2": 0 ,"3": 4 ,"4": 0 ,"5": 0 ,"6":  0,"7": 0 ,"8": 0 ,"9": 0 ,"10": 0 ,"11": 0 ,"12": 0 ,"13": 0 ,"14": 0 ,"15": 6 }
group17 = {"1": 0 ,"2": 2 ,"3": 6 ,"4": 0 ,"5": 0 ,"6":  0,"7": 0 ,"8": 0 ,"9": 0 ,"10": 0 ,"11": 0 ,"12": 0 ,"13": 0 ,"14": 0 ,"15": 4 }
group18 = {"1": 0 ,"2": 2 ,"3": 6 ,"4": 0 ,"5": 0 ,"6":  0,"7": 0 ,"8": 0 ,"9": 0 ,"10": 0 ,"11": 0 ,"12": 0 ,"13": 0 ,"14": 0 ,"15": 4 }
 
def Assign(): 
    while len(constellation) != teams: 
        current = np.random.randint (1,projects+1)
        if not current in constellation: 
            constellation.append(current)
    return constellation

def Epsilon(list):
    epsilon = 0
    for i in range(len(list)):
        epsilon += groups[i][str(list[i])]
    return epsilon

def pooling(constellation):

    for i in range(Iterations):
        backup = constellation.copy()
        constellation = Assign()

        epsilon_before = Epsilon(backup)
        epsilons.append(epsilon_before)
        epsilon_after = Epsilon(constellation)

        if epsilon_after > epsilon_before:
                constellation = backup

    return constellation

    


def solver(constellation):

    for i in range(Iterations):

        backup = constellation.copy()

        epsilon_before = Epsilon(backup)
        epsilons.append(epsilon_before)

        element1 = np.random.randint(0,teams)
        element2  = np.random.randint(0,teams)
        while element2 == element1:                      #swapping elements within the list
            element2 = np.random.randint(0,teams)

        backup[element1], backup[element2] = backup[element2], backup[element1]
        epsilon_after = Epsilon(backup)
    
        if epsilon_after > epsilon_before:
            constellation = backup

        '''
        
        backup = constellation.copy()

        epsilon_before = Epsilon(backup)
        epsilons.append(epsilon_before)

        rand = np.random.randint(1,projects)
        if not rand in backup:
            backup[np.random.randint(0,teams)] = rand                 # replacing elements

        epsilon_after = Epsilon(backup)
    
        if epsilon_after > epsilon_before:
            constellation = backup 
        
        '''
    
    return constellation

constellation = Assign()

#print("Found Constellation: ", solver(constellation))
print("Found Constellation: ", pooling(constellation))
print("Calculated expected Value: ", max(epsilons))
print("highest theoretical Value: ", teams*4)

fig, ax = plt.subplots()
plt.plot(epsilons,color = "pink")
plt.legend()
plt.show()
