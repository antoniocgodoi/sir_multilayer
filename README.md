Simulation Tool for calculating Pr(N) and Pi(N) using the Monte Carlo method.
This repository contains the source code for the simulation tool presented in the article:

"Optimal connectivity of multilayer networks: Enhancing robustness and security"

Authors: Antonio Godoi, Cristiane Batistela and José R. C. Piqueira


Overview

This simulation tool was developed to support the results and experiments discussed in the above article. 
It allows researchers and practitioners to reproduce the simulations, explore parameter configurations, and build upon the presented methodology.

We recommend using PyPy to speed up the simulation (the program was tested with PyPy 7.3.17)

Usage

pypy3 run_parallel.py x y

where x and y are the beta and gamma parameters, respectively

The program performs 15000 simulation runs and save the results in the file sim_results.txt

Run read.py to open sim_results.txt and plot the graphs (we suggest using Spyder to run read.py)
