# This program uses premade data (in differing formats for different graphs) to draw H-R graphs for them.
# Adding your own data to the csv works, just don't add text or the program breaks (converts all entries to float).
# The original sheets from which the data has been taken are in the same directory, they have the same name but without the 2.
# Note that entries missing certain data were removed entirely, as well as stars in spectral class D,
# and all spectral class entries containing only a letter were changed to [letter equivalent number]0, i.e. B => 10

import numpy as np
import matplotlib.pyplot as plt
import csv
import matplotlib as mpl
import matplotlib.cm as cm
from matplotlib.colors import Normalize
import sys
import matplotlib.cbook as cbook
import pandas as pd

def bright():
    results = []
    with open("BrightestStars2.csv") as csvfile:
        reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
        for column in reader: # each row is a list
            results.append(column)
    # print(results) # use to check that the array listing is working
    x_list = [item[2] for item in results] # compiling arrays for later plotting (b-v colour column)
    y_list = [item[1] for item in results] # absolute magnitude column
    area_list = [item[0] for item in results] # apparent magnitude column
    color_list = [(item **2)**(1/8)*np.sign(item)*-1 for item in area_list] # adjusting values to suitable colours
    area_list_big = [((item * 5)**2) for item in area_list] # adjusting values to suitable areas
    x = x_list
    y = y_list
    area = area_list_big
    norm = mpl.colors.Normalize(vmin=-1.5, vmax=2.8) # setting normalisation boundaries on the colour map
    cmap = cm.hot # choosing colourmap
    m = cm.ScalarMappable(norm=norm, cmap=cmap)
    colors = m.to_rgba(color_list) # applying colourmap
    plt.ylim(17, -10) # setting axes limits and titles
    plt.title("Absolute Magnitude Against B-V Colour for the Brightest Stars")
    plt.xlabel("B-V Colour")
    plt.ylabel("Absolute Magnitude")
    plt.scatter(x, y, s=area, c=colors, alpha=0.5) # plotting happens here
    plt.show()

###############################################################################################################################
# The following two functions are very similar to the above one, so the functions do the same things unless otherwise specified
###############################################################################################################################

def near():
    results = []
    with open("NearestStars2.csv") as csvfile:
        reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)  # change contents to floats
        for column in reader:  # each row is a list
            results.append(column)
    x_list = [item[3] for item in results] # spectral class column (O=0, B=1, A=2, etc., second digit comes from the number after the letter)
    y_list = [item[2] for item in results] # absolute magnitude
    area_list = [item[0] for item in results] # distance column (lightyears)
    color_list = [(item) for item in x_list]
    area_list_big = [(50/(item**(1/3))) for item in area_list]
    x = x_list
    y = y_list
    area = area_list_big
    norm = mpl.colors.Normalize(vmin=0, vmax=70)
    cmap = cm.jet # blue to red
    m = cm.ScalarMappable(norm=norm, cmap=cmap)
    colors = m.to_rgba(color_list)
    plt.scatter(x, y, s=area, c=colors, alpha=0.5, label="area $\propto (Distance from Earth) ^{-0.33}$")
    plt.ylim(17, -10)
    plt.xlim(0,70)
    plt.title("H-R Diagram for the Nearest Stars, with Colour Representing Their Colour in Real Life")
    plt.xlabel("Spectral Class")
    plt.ylabel("Absolute Magnitude")
    lgnd = plt.legend(scatterpoints=1, frameon=True, labelspacing=1, title='Point Size', prop={"size": 8}) # plot legend
    lgnd.legendHandles[0]._sizes = [40] # set dot size in the legend
    plt.show()

def mixed():
    results = []
    with open("MixedStars2.csv") as csvfile:
        reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)  # change contents to floats
        for column in reader:  # each row is a list
            results.append(column)
    x_list = [item[4] for item in results] # spectral class column (same as in near)
    y_list = [item[1] for item in results] # absolute magnitude column
    area_list = [item[2] for item in results] # distance column (parsecs)
    color_list = [(item) for item in x_list]
    area_list_big = [(100/(item**0.75)) for item in area_list]
    x = x_list
    y = y_list
    area = area_list_big
    norm = mpl.colors.Normalize(vmin=0, vmax=70)
    cmap = cm.jet # blue to red
    m = cm.ScalarMappable(norm=norm, cmap=cmap)
    colors = m.to_rgba(color_list)
    plt.scatter(x, y, s=area, c=colors, alpha=0.5, label="area $\propto (Distance from Earth) ^{-0.75}$")
    plt.ylim(17, -10)
    plt.xlim(0,70)
    plt.title("H-R Diagram for a Range of Stars, with Colour Representing Their Colour in Real Life")
    plt.xlabel("Spectral Class")
    plt.ylabel("Absolute Magnitude")
    lgnd = plt.legend(scatterpoints=1, frameon=True, labelspacing=1, title='Point Size', prop={"size": 8})
    plt.show()


def choose_graph():
    graph = input(
        "B for brightest stars (absolute magnitude against B-V colour), N for nearest stars, M for mixed stars: ")
    # asking the user which result they want
    if graph == "B": # if statements to decide what to draw based off user input
        bright()
    elif graph == "N":
        near()
    elif graph == "M":
        mixed()
    else:
        print("Invalid input. Please try again.")
        choose_graph() # retry input
choose_graph()
