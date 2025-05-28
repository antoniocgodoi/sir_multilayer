# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 22:50:05 2025

@author: Antônio Carlos Bastos de Godoi
"""

import sys
import concurrent.futures
import time
from func_simulation import run_simulation

param = 150 # Simulation runs
max_links = 7

beta = float(sys.argv[1])
gama = float(sys.argv[2])


# Functions to save and read dict of integers from file
def save_dict(filename, dictionary):
    with open(filename, 'w') as file:
        for key, value in dictionary.items():
            file.write(f'{key}: {value}\n')
 



if __name__ == '__main__':
    
    res_list = []; tmp_list = []
    
    start = time.perf_counter()
    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = [executor.submit(run_simulation, param, n_lnk, beta, gama) for n_lnk in range(1,max_links+1)]
        
        for f in concurrent.futures.as_completed(results):
            tmp_list.append(f.result())
            
    # get an ordered list of result dictionaries of N_Link from 1 to max_list+1
    # tmp_list is an unordered list
    # res_list is the ordered list of tmp_list
    temp, index = 1, 0
    while True:
        if tmp_list[index]['t_links']==temp:
            res_list.append(tmp_list[index])
            temp += 1
            if temp > len(tmp_list):
                break
        if index == len(tmp_list)-1:
            index = 0
        else:
            index += 1
    
    # Process the ordered list res_list
    
    l_links = []
    l_P_nI = []
    l_P_nL = []
    S_av = [0 for _ in range(len(res_list[0]['S']))]
    I_av = [0 for _ in range(len(res_list[0]['I']))]
    R_av = [0 for _ in range(len(res_list[0]['R']))]
    
    
    for temp in range(len(res_list)):
        
        # Calculate the probability of Cluster 2 not infected
        P_nI = 100*(param-res_list[temp]['c2 infections'])/param  
        P_nI = float("{:.2f}".format(P_nI)) # Format with 2 decimals

        # Calculate the probability of C2 not affected and C1 links remained not hit
        P_nL = 100*(res_list[temp]['r_not_hit'])/param
        P_nL = float("{:.2f}".format(P_nL)) # Format with 2 decimals
        
        l_links.append(res_list[temp]['t_links'])
        l_P_nI.append(P_nI)
        l_P_nL.append(P_nL)
        
        # Add S, I and R from the simulations for all number of links
        S_av = [S_av[i]+res_list[temp]['S'][i] for i in range(len(res_list[temp]['S']))]
        I_av = [I_av[i]+res_list[temp]['I'][i] for i in range(len(res_list[temp]['I']))]
        R_av = [R_av[i]+res_list[temp]['R'][i] for i in range(len(res_list[temp]['R']))]
        
    # Calculate the average of S,I and R by dividing by the number of links
    S_av = [S_av[i]/len(res_list) for i in range(len(S_av))]    
    I_av = [I_av[i]/len(res_list) for i in range(len(I_av))]    
    R_av = [R_av[i]/len(res_list) for i in range(len(R_av))]    


    dic_result = {'dimensions':res_list[0]['dims'], 'Beta_C1':res_list[0]['Beta_C1'], 'Gama_C1':res_list[0]['Gama_C1'], 'Beta_C2': res_list[0]['Beta_C2'], 'Gama_C2':res_list[0]['Gama_C2'], 'I(0)':res_list[0]['I0'], 'n':l_links, 'P_nI':l_P_nI, 'P_nL':l_P_nL, 'runs':param, 't':res_list[0]['t'], 'S':S_av, 'I':I_av, 'R':R_av}
    save_dict('sim_results.txt', dic_result)
    
    stop = time.perf_counter()
    
    print(f'\n* Processing finished in {round(stop-start, 2)} seconds')
    print(f'** Average processing speed is {round(param*max_links/(stop-start),2)} Parts/sec')