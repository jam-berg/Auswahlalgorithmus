#!/usr/bin/python3
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

Iterations = 2000
trials = 200
inputFileName = 'InputProjektePräferenz.csv'
with open(inputFileName) as x:
    ncols = len(x.readline().split(','))

csv_file = pd.read_csv(inputFileName, usecols=range(1,ncols))
groups = csv_file.iloc[:,:1]['Gruppe'].values.tolist()
praeferenzen = csv_file.iloc[:, 1:]
project_count= len(praeferenzen.columns)
group_count = len(praeferenzen.index)
projects = list(map(str, range(1,project_count+1)))

groups_choice = []
for index, row in praeferenzen.iterrows():
    row_dict = dict(zip(projects, row))
    groups_choice.append(row_dict)
    
epsilons = []

def Assign():
    assignment = []
    while len(assignment) != group_count: 
        current = np.random.randint (1,project_count+1)
        if not current in assignment: 
            assignment.append(current)
    return assignment 

def Epsilon(listing):
    epsilon = 0
    for i in range(len(listing)):
        epsilon += groups_choice[i][str(listing[i])]
    return epsilon


def solver(constellation):
    for i in range(Iterations):
        backup = constellation.copy()
        epsilon_before = Epsilon(backup)
        epsilons.append(epsilon_before)

        element1 = np.random.randint(0,group_count)
        element2  = np.random.randint(0,group_count)
        while element2 == element1:                      #swapping elements within the list
            element2 = np.random.randint(0,group_count)

        backup[element1], backup[element2] = backup[element2], backup[element1]
        epsilon_after = Epsilon(backup)
    
        if epsilon_after > epsilon_before:
            constellation = backup
        backup = constellation.copy()

        epsilon_before = Epsilon(backup)
        epsilons.append(epsilon_before)

        rand = np.random.randint(1,project_count+1)
        if not rand in backup:
            backup[np.random.randint(0,group_count)] = rand                 # replacing elements

        epsilon_after = Epsilon(backup)
    
        if epsilon_after > epsilon_before:
            constellation = backup
    return constellation, epsilon_after

def Iterate():
    epsilon_results = []
    constellation_results = []
    # lonely_people, new_groups, groups = grouping()
    for i in range(trials): 
        constellation = Assign()
        const,epsil = solver(constellation)
        epsilon_results.append(epsil)
        constellation_results.append(const)
    found_epsilon, found_constellation = max(epsilon_results), constellation_results[epsilon_results.index(max(epsilon_results))] 
    return found_constellation, found_epsilon

final_constellation, final_epsilon = Iterate()
max_value = group_count*4 

print("Found Constellation: {} with an expected Value of {} (theoretical maximum {})".format(final_constellation, final_epsilon, max_value) )

'''

print("Found Constellation: ", solver(constellation))
print("Calculated expected Value: ", max(epsilons))
print("highest theoretical Value: ", group_count*4)

result_string = ""
for i in range(len(constellation)):
    result_string += "Gruppe " + groups[i] + " macht Projekt " + str(constellation[i]) + '\n'
result_string += 'Zufriedenheitswert=' + str(max(epsilons))
with open('resulting_constellation.txt', 'w') as f:
    f.write(result_string)

fig, ax = plt.subplots()
plt.plot(epsilons,color = "pink", label = "solver")
fig.legend()
plt.show()

'''