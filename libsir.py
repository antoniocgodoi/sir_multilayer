# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 15:33:19 2025

@author: Antônio Carlos Bastos de Godoi
"""


import gc
import os
import random
# import matplotlib.pyplot as plt
# from matplotlib.colors import LinearSegmentedColormap


class Cell(object):        
    def __init__(self, state):
        ps = ['S','I','R']
        if type(state) != str:
            raise ValueError('Initial state should be a string!')
        state = state.upper()
        if state not in ps:
            raise ValueError('Initial state should be S,I or R')
        self.st_ = state  # {s,i,r}
        self.neigh_ = []                
    def setstate(self, state):
        self.st_ = state         
    def state(self):
        return self.st_        
    def nb(self):
        return self.neigh_        
    def setnb(self, n):
        if list_depth1(n):
            self.neigh_ = n
        else:
            raise ValueError('Invalid neighborhood list!')            
    def __str__(self):
        return str(self.st_)       


def calc_next_state(cells=[]):    
    if type(cells) != list:
        raise ValueError('Input should be a list!')   
    if len(cells) == 0:
        for obj in gc.get_objects():
            if isinstance(obj, Cell):
                cells.append(obj)
    
    if len(cells) < 2:
        raise ValueError('Automata should have more than one cell!')
        
    next_state = []
    for i in range(len(cells)):
        next_state.append(cells[i].state())
    # Next state will be the same if no change occurs
    
    for i, c in enumerate(cells):        
        if c.state() == 'S':
        # Find the number of infected neighbors
            infected_neighbors = 0            
            for v in c.nb():
                if v.state() == 'I':
                    infected_neighbors += 1
                    
        # Transition rule from S to I
            for contacts in range(infected_neighbors):
                r = random.random()
                if r < c.beta:
                    next_state[i]='I'
        
        # Transition rule from I to R
        if c.state() == 'I':
            r = random.random()
            if r < c.gamma:
                next_state[i]='R'
                
    # Update all cells
    for i, c in enumerate(cells):
        c.setstate(next_state[i])


def save_plot(net_topology, fname):
    subfolder = 'plots' # Folder name 
    dir_path = os.path.dirname(os.path.realpath('libsir.py'))
    dir_path = dir_path+'\\'+str(subfolder)
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path) # Create "plots" folder to save graphs
    colors = ["#00ff00","#ff0000","#0000ff"] # S = Green / I = Red / R = Blue
    custom_cmap = LinearSegmentedColormap.from_list("custom_cmap", colors)
    dic = {'S':1, 'I':2, 'R':3}
    temp2 = []
    for y in range(len(net_topology)):
        temp=[]
        for x in range(len(net_topology[y])):
            temp.append(int(dic[net_topology[y][x].state()]))
        temp2.append(temp)
    plt.imshow(temp2, cmap=custom_cmap, vmin=1, vmax=3)
    plt.savefig(subfolder+"\\"+fname)
    plt.close()
    
def depth(x):
    if isinstance(x, Cell):
        return(1)
    elif type(x) != list:
        raise ValueError('Invalid neighborhood list!')
    else:
        return 1 + depth(x[0])

def list_depth1(x):
    count = 0
    for i in x:
        count += depth(i)
    return len(x) == count