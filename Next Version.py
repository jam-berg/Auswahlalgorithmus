import numpy as np
import random 
import matplotlib.pyplot as plt
import copy


## 4 for "Sehr gerne" 2 for "gerne"  0 for "egal" -2 for "nicht gerne" -6 for "gar nicht gerne"

teams = 15
projects = 15
Iterations = 10000
treshold = 33

constellation = []
epsilons = []
epsilons_solver =[]
trials = 25




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
 
persons = [{"1": 0 ,"2": -2 ,"3": 2 ,"4": 0 ,"5": 2 ,"6":  2,"7": -6 ,"8": -2 ,"9": 2 ,"10": 0 ,"11": -2 ,"12": 0 ,"13": 0 ,"14": 2 ,"15": 4 }
, {"1": 4 ,"2": 4 ,"3": 4 ,"4": 4 ,"5": -2 ,"6":  0,"7": 4 ,"8": 4 ,"9": 0 ,"10": 0 ,"11": 0 ,"12": 0 ,"13": -2,"14": 0 ,"15": 2 }
, {"1": -2 ,"2": 2 ,"3": -2 ,"4": -2 ,"5": 4 ,"6":  -2,"7": 2 ,"8": 2 ,"9": 0 ,"10": 2 ,"11": 4 ,"12": 0 ,"13": 0 ,"14": 0 ,"15": 4 }
, {"1": 0,"2": 2 ,"3": 0 ,"4": 4 ,"5": 2 ,"6": 2 ,"7": 0 ,"8": 4 ,"9": 4 ,"10": -6 ,"11": 0 ,"12": 2 ,"13": 2 ,"14": -6 ,"15": -6 }
, {"1": 0,"2": 4 ,"3": 2 ,"4": 2 ,"5": 0 ,"6":  4,"7": 0 ,"8": 6 ,"9": 2 ,"10": 0 ,"11": 0 ,"12": 2 ,"13": 0 ,"14": 0 ,"15": 2 }
]

person1 = {"1": 0 ,"2": -2 ,"3": 2 ,"4": 0 ,"5": 2 ,"6":  2,"7": -6 ,"8": -2 ,"9": 2 ,"10": 0 ,"11": -2 ,"12": 0 ,"13": 0 ,"14": 2 ,"15": 4 }
person2 = {"1": 4 ,"2": 4 ,"3": 4 ,"4": 4 ,"5": -2 ,"6":  0,"7": 4 ,"8": 4 ,"9": 0 ,"10": 0 ,"11": 0 ,"12": 0 ,"13": -2,"14": 0 ,"15": 2 }
person3 = {"1": -2 ,"2": 2 ,"3": -2 ,"4": -2 ,"5": 4 ,"6":  -2,"7": 2 ,"8": 2 ,"9": 0 ,"10": 2 ,"11": 4 ,"12": 0 ,"13": 0 ,"14": 0 ,"15": 4 }
person4 = {"1": 0,"2": 2 ,"3": 0 ,"4": 4 ,"5": 2 ,"6": 2 ,"7": 0 ,"8": 4 ,"9": 4 ,"10": -6 ,"11": 0 ,"12": 2 ,"13": 2 ,"14": -6 ,"15": -6 }
person5 = {"1": 0,"2": 4 ,"3": 2 ,"4": 2 ,"5": 0 ,"6":  4,"7": 0 ,"8": 6 ,"9": 2 ,"10": 0 ,"11": 0 ,"12": 2 ,"13": 0 ,"14": 0 ,"15": 2 }

def evaluate(): 
    match_index = []
    tested_combinations = []
    key = []
    for k, person in enumerate(persons):
        for i in range(0,len(persons)):
            counter = 0
            if person == persons[i]:
                continue
            if not np.exp(k)+np.exp(i) in tested_combinations:
                tested_combinations.append(np.exp(k)+np.exp(i)) 
                for j in range(1,len(person)+1):
                    if person[str(j)] == persons[i][str(j)]:
                        counter += 1
                match_index.append(counter)
                key.append([k,i])
    return match_index, key
                
def grouping(): 
    matches, key = evaluate()
    backup = key.copy()
    new_groups = []
    used_up_people = []
    lonely_people = []
    for i in range(len(matches)):
        if max(matches) >= (projects/100)*treshold:
            if key[matches.index(max(matches))][0] not in used_up_people:   
                if key[matches.index(max(matches))][1] not in used_up_people:
                    rand = np.random.choice(key[matches.index(max(matches))])
                    groups.append(persons[rand])
                    new_groups.append(key[matches.index(max(matches))])
                    used_up_people.append(key[matches.index(max(matches))][0])
                    used_up_people.append(key[matches.index(max(matches))][1])
                    key.remove(key[matches.index(max(matches))])
                    matches.remove(max(matches))
                else: 
                    key.remove(key[matches.index(max(matches))])
                    matches.remove(max(matches))
                    
            else: 
                key.remove(key[matches.index(max(matches))])
                matches.remove(max(matches))

    for i in range(len(backup)):
        Bool0 = []
        Bool1 = []
        for j in range(len(new_groups)):
            Bool0.append(backup[i][0] not in new_groups[j])
            Bool1.append(backup[i][1] not in new_groups[j])
        if np.all(Bool0) == True and backup[i][0] not in lonely_people:
                lonely_people.append(backup[i][0])
        if np.all(Bool1) == True and backup[i][1] not in lonely_people:
                lonely_people.append(backup[i][1]) 

    return lonely_people, new_groups

            

            

def Assign():
    assignment = []
    while len(assignment) != teams: 
        current = np.random.randint (1,projects+1)
        if not current in assignment: 
            assignment.append(current)
    return assignment 

def Epsilon(list):
    epsilon = 0
    for i in range(len(list)):
        epsilon += groups[i][str(list[i])]
    return epsilon

def pooling(constellation):
    
    backup = constellation.copy()
    for i in range(Iterations):
        constellation = []
        constellation = Assign()

        epsilon_before = Epsilon(backup)
        epsilons.append(epsilon_before)
        epsilon_after = Epsilon(constellation)

        if epsilon_after > epsilon_before:
                backup = constellation

    return constellation

    


def solver(constellation):

    for i in range(Iterations):

        backup = constellation.copy()

        epsilon_before = Epsilon(backup)
        epsilons_solver.append(epsilon_before)

        element1 = np.random.randint(0,teams)
        element2  = np.random.randint(0,teams)
        while element2 == element1:                      #swapping elements within the list
            element2 = np.random.randint(0,teams)

        backup[element1], backup[element2] = backup[element2], backup[element1]
        epsilon_after = Epsilon(backup)
    
        if epsilon_after > epsilon_before:
            constellation = backup

            
        
        backup = constellation.copy()

        epsilon_before = Epsilon(backup)
        epsilons_solver.append(epsilon_before)

        rand = np.random.randint(1,projects)
        if not rand in backup:
            backup[np.random.randint(0,teams)] = rand                 # replacing elements

        epsilon_after = Epsilon(backup)
    
        if epsilon_after > epsilon_before:
            constellation = backup
    return constellation, epsilon_after

def Iterate():
    epsilon_results = []
    constellation_results = []
       
    for i in range(trials): 
        constellation = Assign()
        epsilon_results.append(solver(constellation)[1])
        constellation_results.append(solver(constellation)[0])
        print(constellation_results)
    return max(epsilon_results), constellation_results[epsilon_results.index(max(epsilon_results))]


print(Iterate())
'''
constellation = Assign()
print(evaluate())
print(grouping())


print("Found Constellation: ", solver(constellation))
print("Found Constellation: ", pooling(constellation))
print("Calculated expected Value: ", max(epsilons_solver))
print("highest theoretical Value: ", teams*4)

fig, ax = plt.subplots()
ax.plot(epsilons,color = "pink", label = "pooling")
ax.plot(epsilons_solver, label = "solver")
fig.legend()
plt.show()
'''