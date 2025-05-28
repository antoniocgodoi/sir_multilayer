# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 17:54:14 2025

@author: Antônio Carlos Bastos de Godoi
"""

import matplotlib.pyplot as plt
import os
from tkinter import filedialog
import tkinter as tk

dir_path = os.path.dirname(os.path.realpath('read.py'))

root = tk.Tk()
root.title('Plot Simulation File')

root.filename = filedialog.askopenfilename(initialdir=dir_path, title='Select a Simulation File', filetypes=[("txt files", "*.txt")])

def read_dict(filename):
    dictionary = {}
    with open(filename, 'r') as file:
        for line in file:
            key, value = line.strip().split(': ')
            try:
                dictionary[key] = int(value)
            except ValueError:
                dictionary[key] = eval(value)
    return dictionary

res = read_dict(root.filename)

plt.figure('S, I and R')
plt.plot(res['t'],res['S'], color='g', label='susceptible')
plt.plot(res['t'],res['I'], color='r', label='infected')
plt.plot(res['t'],res['R'], color='b', label = 'removed')
plt.xlabel('t')
plt.title('S(t), I(t) and R(t) of External Network')
plt.legend()
plt.figure('Probabilities')

plt.title(r'P${}_{I}$(N) and P${}_{R}$(N)')
plt.xlabel(r'P${}_{R}$(N) [%]')
plt.ylabel(r'P${}_{I}$(N) [%]')
plt.axis([0,100,0,100])
plt.scatter(res['P_nL'][0], res['P_nI'][0], color='blue', label='N=1')
plt.scatter(res['P_nL'][1], res['P_nI'][1], color='green', label='N=2')
plt.scatter(res['P_nL'][2], res['P_nI'][2], color='orange', label='N=3')
plt.scatter(res['P_nL'][3], res['P_nI'][3], color='black', label='N=4')
plt.scatter(res['P_nL'][4], res['P_nI'][4], color='red', label='N=5')
plt.scatter(res['P_nL'][5], res['P_nI'][5], color='cyan', label='N=6')
plt.scatter(res['P_nL'][6], res['P_nI'][6], color='violet', label='N=7')
plt.legend()

print('Number of simulation runs =', res['runs'])
print('List of links:', res['n'])
print('Dimensions: ',res['dimensions'])
print('Proportion of Infected at t=0: ', res['I(0)'])
print('External Network: [ Beta1:',res['Beta_C1'],'   Gama1:',res['Gama_C1'],']')
print('Local Network: [ Beta2:',res['Beta_C2'],'   Gama2:',res['Gama_C2'],']')
print('List of Probability of Local Network not infected:', res['P_nI'])
print('List of Probability of Local Network not infected and remaining links:', res['P_nL'])

root.destroy()