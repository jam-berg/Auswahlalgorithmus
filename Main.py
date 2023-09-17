#!/usr/bin/python3
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import csv

Iterations = 2000
trials = 200
inputFileName = 'Preference Semesterprojekt (Responses) - Form Responses 1.csv'
file_content = []
with open(inputFileName, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    file_content = list(csvreader)
project_names = file_content[0][2:]
group_names = [row[1] for row in file_content[1:]]
preferences = [[int(entry) for entry in row[2:]] for row in file_content[1:]]
print(project_names)
print(group_names)
print(preferences)
project_count = len(project_names)
group_count = len(group_names)

epsilons = []
def Assign():
    assignment = []
    while len(assignment) != group_count: 
        current = np.random.randint (0,project_count)
        if not current in assignment: 
            assignment.append(current)
    return assignment 

def Epsilon(listing):
    epsilon = 0
    for i in range(len(listing)):
        epsilon += preferences[i][listing[i]]
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

        rand = np.random.randint(0,project_count)
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
max_value = group_count*5 

print("Found Constellation: {} with an expected Value of {} (theoretical maximum {})".format(final_constellation, final_epsilon, max_value) )
print("add +1 for project number")

result_string = ""
for i in range(len(final_constellation)):
    result_string += "Gruppe " + group_names[i] + " macht " + project_names[final_constellation[i]] + '\n'
result_string += 'Durchschnittlicher Zufriedenheitswert=' + str(final_epsilon/group_count)
print(result_string)
with open('resulting_constellation.txt', 'w') as f:
    f.write(result_string)

'''
fig, ax = plt.subplots()
plt.plot(epsilons,color = "pink", label = "solver")
fig.legend()
plt.show()
'''


