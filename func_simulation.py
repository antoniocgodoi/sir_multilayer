# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 11:53:20 2025

@author: Antônio Carlos Bastos de Godoi
"""

#------------------------------------------ Simulation-----------------------

import random
from libsir import Cell, calc_next_state

x_dim = 32; y_dim = 32 # cluster dimensions
infect0 = .9 # proportion of infected in cluster 1, at t = 0

Beta_Cluster1 = 0
Gama_Cluster1 = 0.1

Beta_Cluster2 = 0
Gama_Cluster2 = 0.1

class Cell_in_cluster_1(Cell):
    def __init__(self, state):
        Cell.__init__(self, state)
        self.beta = Beta_Cluster1 # Probability of getting infected
        self.gamma = Gama_Cluster1 # Probability of recovering    
        
class Cell_in_cluster_2(Cell):
    def __init__(self, state):
        Cell.__init__(self, state)
        self.beta = Beta_Cluster2 # Probability of getting infected
        self.gamma = Gama_Cluster2 # Probability of recovering   

# helper function to get random tuples
def get_tuple():
    i = round(random.random()*(y_dim-1))
    j = round(random.random()*(x_dim-1))
    return (i, j)


def set_clusters(n_links):
    # Set initial states of cluster 1
    # Only infect0 % are infected at t = 0
    state_cluster_1 = []
    for i in range(y_dim):
        temp = []
        for j in range(x_dim):
            if random.random() < infect0:
                temp.append('I')
            else:
                temp.append('S')
        state_cluster_1.append(temp)
    
    # Set initial states of cluster 2
    # All cells are susceptible at t = 0
    state_cluster_2 = []
    for i in range(y_dim):
        temp = []
        for j in range(x_dim):
            temp.append('S')
        state_cluster_2.append(temp)
    
    # Create cluster 1 with x_dim x y_dim dimensions
    c1 = []
    for i in range(y_dim):
        temp = []
        for j in range(x_dim):
            t = Cell_in_cluster_1(state_cluster_1[i][j])
            temp.append(t)
        c1.append(temp)
    
    # Create cluster 2 with x_dim x y_dim dimensions
    c2 = []
    for i in range(y_dim):
        temp = []
        for j in range(x_dim):
            t = Cell_in_cluster_2(state_cluster_2[i][j])
            temp.append(t)
        c2.append(temp)
    
    # Set the neighborhood of cluster 1 - Use Moore Neighborhood (8 neighbors)
    for i in range(1, y_dim-1):
        for j in range(1, x_dim-1):
            c1[i][j].setnb([c1[i-1][j],c1[i-1][j+1],c1[i][j+1],c1[i+1][j+1],c1[i+1][j],c1[i+1][j+1],c1[i+1][j],c1[i+1][j-1],c1[i][j-1],c1[i-1][j-1],c1[i-1][j]])
    # Set the four corners
    c1[0][0].setnb([c1[0][1],c1[1][1],c1[1][0]])
    c1[y_dim-1][0].setnb([c1[y_dim-2][0],c1[y_dim-2][1],c1[y_dim-1][1]])
    c1[0][x_dim-1].setnb([c1[0][x_dim-2],c1[1][x_dim-2],c1[1][x_dim-1]])
    c1[x_dim-1][y_dim-1].setnb([c1[y_dim-1][x_dim-2],c1[y_dim-2][x_dim-2],c1[y_dim-2][x_dim-1]])
    # Set neighborhood for i=0 and j in 1...x_dim-1
    for j in range(1,x_dim-1):
        c1[0][j].setnb([c1[0][j-1],c1[1][j-1],c1[1][j],c1[1][j+1],c1[0][j+1]])
    # Set neighborhood for i=y_dim-1 and j in 1...x_dim-2
    for j in range(1,x_dim-1):
        c1[y_dim-1][j].setnb([c1[y_dim-1][j-1],c1[y_dim-2][j-1],c1[y_dim-2][j],c1[y_dim-2][j+1],c1[y_dim-1][j+1]])
    # Set neighborhood for i in 1..y_dim-2 and j = 0
    for i in range(1,y_dim-1):
        c1[i][0].setnb([c1[i-1][0],c1[i-1][1],c1[i][1],c1[i+1][1],c1[i+1][0]])
    # Set neighborhood for i in 1...y_dim-2 and j = x_dim-1
    for i in range(1,y_dim-1):
        c1[i][x_dim-1].setnb([c1[i-1][x_dim-1],c1[i-1][x_dim-2],c1[i][x_dim-2],c1[i+1][x_dim-2],c1[i+1][x_dim-1]])
    
    
    
    # Set the neighborhood of cluster 2 - Use Moore Neighborhood (8 neighbors)
    for i in range(1, y_dim-1):
        for j in range(1, x_dim-1):
            c2[i][j].setnb([c2[i-1][j],c2[i-1][j+1],c2[i][j+1],c2[i+1][j+1],c2[i+1][j],c2[i+1][j+1],c2[i+1][j],c2[i+1][j-1],c2[i][j-1],c2[i-1][j-1],c2[i-1][j]])
    # Set the four corners
    c2[0][0].setnb([c2[0][1],c2[1][1],c2[1][0]])
    c2[y_dim-1][0].setnb([c2[y_dim-2][0],c2[y_dim-2][1],c2[y_dim-1][1]])
    c2[0][x_dim-1].setnb([c2[0][x_dim-2],c2[1][x_dim-2],c2[1][x_dim-1]])
    c2[x_dim-1][y_dim-1].setnb([c2[y_dim-1][x_dim-2],c2[y_dim-2][x_dim-2],c2[y_dim-2][x_dim-1]])
    # Set neighborhood for i=0 and j in 1...x_dim-1
    for j in range(1,x_dim-1):
        c2[0][j].setnb([c2[0][j-1],c2[1][j-1],c2[1][j],c2[1][j+1],c2[0][j+1]])
    # Set neighborhood for i=y_dim-1 and j in 1...x_dim-2
    for j in range(1,x_dim-1):
        c2[y_dim-1][j].setnb([c2[y_dim-1][j-1],c2[y_dim-2][j-1],c2[y_dim-2][j],c2[y_dim-2][j+1],c2[y_dim-1][j+1]])
    # Set neighborhood for i in 1..y_dim-2 and j = 0
    for i in range(1,y_dim-1):
        c2[i][0].setnb([c2[i-1][0],c2[i-1][1],c2[i][1],c2[i+1][1],c2[i+1][0]])
    # Set neighborhood for i in 1...y_dim-2 and j = x_dim-1
    for i in range(1,y_dim-1):
        c2[i][x_dim-1].setnb([c2[i-1][x_dim-1],c2[i-1][x_dim-2],c2[i][x_dim-2],c2[i+1][x_dim-2],c2[i+1][x_dim-1]])
        
    
    # Ramdonly connect Cluster 1 and Cluster 2, with n links

    links = {}
    
    # get dict of random links (x1,y1):(x2,y2)
    while len(links.items()) < n_links:
        (i1, j1) = get_tuple()
        if (i1, j1) not in links.keys():
            while True:
                (i2, j2) = get_tuple()
                if (i2, j2) not in links.values():
                    links.update({(i1, j1):(i2, j2)})
                    break

    # communicate Cluster 1 with Cluster 2 
    for t1, t2 in links.items():
        i1 = t1[0]; j1=t1[1]; i2=t2[0]; j2=t2[1]
        
        l = list(c1[i1][j1].nb()) # neighbors of c1
        l.append(c2[i2][j2]) # add a neighbor in c2
        c1[i1][j1].setnb(l)
        
        l = list(c2[i2][j2].nb()) # neighbors of c2
        l.append(c1[i1][j1]) # add a neighbor in c1
        c2[i2][j2].setnb(l)
        
    return c1,c2,links
 

#-----------------------------------------------------------------------------
# Functions to get the number of S, I and R of the clusters

def S(c):
    result = 0
    for i in range(len(c)):
        for j in range(len(c[i])):
            if c[i][j].state() == 'S':
                result += 1
    return(result)

def I(c):
    result = 0
    for i in range(len(c)):
        for j in range(len(c[i])):
            if c[i][j].state() == 'I':
                result += 1
    return(result)

def R(c):
    result = 0
    for i in range(len(c)):
        for j in range(len(c[i])):
            if c[i][j].state() == 'R':
                result += 1
    return(result)

#-----------------------------------------------------------------------------

# Function to save integer list in a file
def save_list(lista, name_file):
    with open(name_file, 'w') as filehandle:
        for listitem in lista:
            filehandle.write(f'{listitem}\n')

# Function to read integer list from file
def read_list(lista, name_file):
    out = []; res = []
    with open(name_file, 'r') as filehandle:
        for line in filehandle:
            curr_place = line[:-1]
            out.append(curr_place)
        for i in out:
            res.append(int(i))
    return (res)


# Run the simulation for t = t_max
def run_simulation(n_times, x_links, Beta, Gama):
    
    Beta_Cluster1 = Beta
    Beta_Cluster2 = Beta
    Gama_Cluster1 = Gama
    Gama_Cluster2 = Gama
    
    t_max = 300 # time interval
    x = [i for i in range(t_max)]
    
    # St, It and Rt are the list of average S,I and R
    St = [0 for x in range(t_max)]
    It = [0 for x in range(t_max)]
    Rt = [0 for x in range(t_max)]
    
    InfectionCluster2 = 0 # Number of times Cluster 2 is infected
    remained = 0 # Number of runs that at least one link remained not hit and Cluster 2 not infected
    
    for _ in range(n_times):
        # Set Cluster 1, Cluster 2 and their links
        c1, c2, links = set_clusters(x_links)
        
        all_cells = []
        for a_ in range(y_dim):
            for b_ in range(x_dim):
                all_cells.append(c1[a_][b_])
                all_cells.append(c2[a_][b_])        
        
        St1, It1, Rt1 = [], [], []
        St2, It2, Rt2 = [], [], []
        print('[ Links =',str(x_links),']  Run: ',str(_))
        for t1 in range(t_max):
            St1.append(S(c1)); It1.append(I(c1)); Rt1.append(R(c1))
            St2.append(S(c2)); It2.append(I(c2)); Rt2.append(R(c2))
            # if (t1+1)%(t_max/5) == 0:
            #     print(' ',round(100*(t1+1)/(t_max)),'%', end = '')
            # if (t1+1)%t_max == 0:
            #     print(' ---> Processed Part',_+1,'of',n_times, end = '')
            #     if (_+1 == n_times):
            #         print('\n')                              
            calc_next_state(all_cells)
        # After each simularion run
        # Calculate the number of not hit links (s_links)
        s_links = 0
        for (i,j) in links.keys():
            if c1[i][j].state() == 'S':
                s_links += 1
        total_links = len(links.items())
        # Add 1 if at least one link remained not hit and Cluster 2 not infected
        if (s_links > 0) and (Rt2[t_max-1]==0 and It2[t_max-1]==0):
            remained += 1
            
        if (Rt2[t_max-1]>0 or It2[t_max-1]>0):
            InfectionCluster2 += 1
        for p1 in range(t_max):
            St[p1] = St[p1] + St1[p1]
            It[p1] = It[p1] + It1[p1]
            Rt[p1] = Rt[p1] + Rt1[p1]
    # Calculate average of S, I and R
    for j in range(t_max):
        St[j] = St[j]/n_times
        It[j] = It[j]/n_times
        Rt[j] = Rt[j]/n_times              
        
    return {'Beta_C1':Beta_Cluster1, 'Gama_C1':Gama_Cluster1, 'Beta_C2':Beta_Cluster2, 'Gama_C2':Gama_Cluster2, 'dims':[x_dim,y_dim], 'I0':infect0, 't':x, 'S':St, 'I':It, 'R':Rt, 'c2 infections': InfectionCluster2, 'r_not_hit': remained, 't_links': total_links}