# The following program calculates SNR from from source brightness, exposure time, and distance to the source.
# The commented functions were plannes but since dropped

import sys
import numpy as np
import math
import matplotlib.pyplot as plt
import scipy
# define parameters
q = 0.7
n_p = 4
ss = 10
sd = 0.0011
rn = 3

calculate = str(input("What would you like to calculate? (S for SNR, T for time required to reach SNR = 5, or G for a "
                      "graph of SNR against exposure time): (T and G currently do not work) "))

def calculate_snr():
    t = float(input("What is the exposure time (in s)? ")) #take inputs
    source_brightness = float(input("What is the source brightness (in J/s)? "))
    dist = float(input("What is the distance to the source (in m)? "))
    so_space = source_brightness / (6.63e-34 * 3e8 / 500e-9) # convert to photons per second
    so = so_space / (4 * np.pi * dist**2)
    snr = ((so * (math.sqrt(q * t)))/math.sqrt(so + n_p * (ss + (sd/q) + ((rn ** 2)/(q * t))))) # run through formula
    print("The SNR is " + str(np.round(snr, 2)))

# def calculate_t_exp():
#     source_brightness = float(input("What is the source brightness (in J/s)? "))
#     so = source_brightness / (6.63e-34 * 3e8 / 500e-9)
#     snr = 5
#     t = 2
#     print("The time taken to reach a SNR of 5 is " + str(t))
#
# def draw_snr_graph():
#     source_brightness = float(input("What is the source brightness (in J/s)? "))
#     so = source_brightness / (6.63e-34 * 3e8 / 500e-9)


if calculate == "S":
    calculate_snr()
elif calculate == "T":
#    calculate_t_exp()
    print("Not working yet.")
elif calculate == "G":
#    draw_snr_graph()
    print("Not working yet.")
else:
    print("Invalid input.")