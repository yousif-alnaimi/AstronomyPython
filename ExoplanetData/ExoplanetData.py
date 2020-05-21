# This program draws a graph incorporating planet mass, radius, orbital period and detection method for confirmed exoplanets
#
import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import matplotlib.cm as cm
from matplotlib.colors import Normalize
from numpy import ma

data_dir = "." + os.sep + "data" + os.sep # find directory containing csv
filename = "ConfirmedPlanets.csv" # choose csv
# print(data_dir + filename)
df = pd.read_csv(data_dir + filename) #read_csv loads the file
df.head(5) #df is now a dataframe object
color_list = df['pl_discmethod'].tolist() #generate list
color_list_unique = ["Pulsar Timing", "Transit", "Microlensing", "Radial Velocity", "Imaging", "Orbital Brightness Modulation",
                     "Transit Timing Variations", "Eclipse Timing Variations", "Pulsation Timing Variations",
                     "Disk Kinematics", "Astrometry"]
color_list_numeric = color_list
for n, i in enumerate(color_list_numeric): # convert text to numbers for cmap
    if i == "Pulsar Timing":
        color_list_numeric[n] = 0 # I could have used list entries here and color_list_unique = list(set(color_list))
    if i == "Transit": # but that would cause a random change in what colours mean what method every time you run it
        color_list_numeric[n] = 1/11
    if i == "Microlensing":
        color_list_numeric[n] = 2/11
    if i == "Radial Velocity":
        color_list_numeric[n] = 3/11
    if i == "Imaging":
        color_list_numeric[n] = 4/11
    if i == "Orbital Brightness Modulation":
        color_list_numeric[n] = 5/11
    if i == "Transit Timing Variations":
        color_list_numeric[n] = 6/11
    if i == "Eclipse Timing Variations":
        color_list_numeric[n] = 7/11
    if i == "Pulsation Timing Variations":
        color_list_numeric[n] = 8/11
    if i == "Disk Kinematics":
        color_list_numeric[n] = 9/11
    if i == "Astrometry":
        color_list_numeric[n] = 10/11
# print(color_list_unique) # checking lists
# print(color_list_numeric)
norm = mpl.colors.Normalize(vmin=0, vmax=1) # normalisation for colormap
cmap = cm.hsv # cyclic rainbow pattern (can change to others if you want to)
m = cm.ScalarMappable(norm=norm, cmap=cmap) # apply cmap and norm
colors = m.to_rgba(color_list_numeric) # generate colours for later plotting
# colors = cmap(np.linspace(0, 1, len(color_list))) # random colour generation - not helpful
# print(len(color_list)) # checking length

def choose_graph(): # function to choose start and end points to focus on
    x_start = input("Set the starting point for x: ")
    x_end = input("Set the ending point for x: ")
    y_start = input("Set the starting point for y: ")
    y_end = input("Set the ending point for y: ")
    if x_start and x_end != "":
        if x_start == x_end or y_start == y_end: # bug prevention
            print("Start and end points cannot be the same.")
            choose_graph() # loop if failed
        else:
            print("")
            plt.xlim(x_start, x_end)
    else:
        print("Using default x boundaries.")
    if y_start and y_end != "":
        if x_start == x_end or y_start == y_end: # bug prevention
            print("Start and end points cannot be the same.")
            choose_graph() # loop if failed
        else:
            print("")
            plt.ylim(y_start, y_end)
    else: # default to fit all if no entries are recorded
        print("Using default y boundaries.")
choose_graph()

x_raw = df["pl_bmassj"].to_numpy() # read lists to arrays
y_raw = df["pl_radj"].to_numpy()
area_raw = df["pl_orbper"].to_numpy()
x = np.log(x_raw) # take logs of x and y data
y = np.log(y_raw)

# print(np.nanmean(x)) # checking mean function
def best_fit_slope_and_intercept(x, y): # setting line parameters
    m = (((np.nanmean(x) * np.nanmean(y)) - np.nanmean(x * y)) /
         ((np.nanmean(x) * np.nanmean(x)) - np.nanmean(x * x)))

    b = np.nanmean(y) - m * np.nanmean(x)

    return m, b

m, b = best_fit_slope_and_intercept(x, y)

# print(m, b) # check line parameters
regression_line = [(m*xi)+b for xi in x]
plt.plot(x, regression_line,aa=True)


area = np.sqrt(area_raw) * 1.5 # normalise areas to prevent jarring differences
plt.xlabel("ln(Planet Mass (Jupiter Masses))") # apply titles and axis labels
plt.ylabel("ln(Planet Radius (Jupiter Radii))")
plt.title("A Graph of Confirmed Planet Radius against Planet Mass, with Colour "
          "Representing Detection Method and Size Representing Orbital Period")
# plt.scatter(x,y,alpha=0.5,s=area,label='area $\propto \sqrt{Orbital Period}$',c=colors)
plt.grid(b=True, which='major', color='#666666', linestyle='-') # draw major gridlines
# lgnd = plt.legend(scatterpoints=1, frameon=True, labelspacing=1, title='Point Size', prop={"size": 6})
plt.minorticks_on() # draw minor gridlines
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
# lgnd.legendHandles[0]._sizes = [30]
# plt functions above will only draw the area dot in the legend

#below is the drawing function - full of cosmetic changes to make it look good
plt.scatter(x,y,alpha=0.04,s=area,label=color_list_unique[0],c=colors) # the plt scatters occur 12 times, so alpha is
plt.scatter(x,y,alpha=0.04,s=area,label=color_list_unique[1],c=colors) # 0.04 so that it is around 0.5 once all have
plt.scatter(x,y,alpha=0.04,s=area,label=color_list_unique[2],c=colors) # been plotted
plt.scatter(x,y,alpha=0.04,s=area,label=color_list_unique[3],c=colors)
plt.scatter(x,y,alpha=0.04,s=area,label=color_list_unique[4],c=colors)
plt.scatter(x,y,alpha=0.04,s=area,label=color_list_unique[5],c=colors)
plt.scatter(x,y,alpha=0.04,s=area,label=color_list_unique[6],c=colors)
plt.scatter(x,y,alpha=0.04,s=area,label=color_list_unique[7],c=colors)
plt.scatter(x,y,alpha=0.04,s=area,label=color_list_unique[8],c=colors)
plt.scatter(x,y,alpha=0.04,s=area,label=color_list_unique[9],c=colors) # ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.scatter(x,y,alpha=0.04,s=area,label=color_list_unique[10],c=colors)
plt.scatter(x,y,alpha=0.04,s=area,label='area $\propto \sqrt{Orbital Period}$',c=colors) # label for area
lgnd = plt.legend(scatterpoints=1, frameon=True, labelspacing=1, title='Point Colour and Size', prop={"size": 9}
#                  , loc = "center right", bbox_to_anchor=(0.15, 0.5) # change location of legend, commented = default
                  ) # draw legends
lgnd.legendHandles[0]._sizes = [80] # apply sizes to dots
lgnd.legendHandles[1]._sizes = [80]
lgnd.legendHandles[2]._sizes = [80]
lgnd.legendHandles[3]._sizes = [80]
lgnd.legendHandles[4]._sizes = [80]
lgnd.legendHandles[5]._sizes = [80]
lgnd.legendHandles[6]._sizes = [80]
lgnd.legendHandles[7]._sizes = [80]
lgnd.legendHandles[8]._sizes = [80]
lgnd.legendHandles[9]._sizes = [80]
lgnd.legendHandles[10]._sizes = [80]
lgnd.legendHandles[11]._sizes = [80]
rgba0 = cmap(0) # set colour values to be used in defining point colour
rgba1 = cmap(1/11)
rgba2 = cmap(2/11)
rgba3 = cmap(3/11)
rgba4 = cmap(4/11)
rgba5 = cmap(5/11)
rgba6 = cmap(6/11)
rgba7 = cmap(7/11)
rgba8 = cmap(8/11)
rgba9 = cmap(9/11)
rgba10 = cmap(10/11)
lgnd.legendHandles[0].set_color(rgba0) # set legend point colours
lgnd.legendHandles[1].set_color(rgba1)
lgnd.legendHandles[2].set_color(rgba2)
lgnd.legendHandles[3].set_color(rgba3)
lgnd.legendHandles[4].set_color(rgba4)
lgnd.legendHandles[5].set_color(rgba5)
lgnd.legendHandles[6].set_color(rgba6)
lgnd.legendHandles[7].set_color(rgba7)
lgnd.legendHandles[8].set_color(rgba8)
lgnd.legendHandles[9].set_color(rgba9)
lgnd.legendHandles[10].set_color(rgba10)
lgnd.legendHandles[11].set_color("#222222")
lgnd.legendHandles[0].set_alpha(0.5) # set transparency of legend points(would be barely visible otherwise)
lgnd.legendHandles[1].set_alpha(0.5)
lgnd.legendHandles[2].set_alpha(0.5)
lgnd.legendHandles[3].set_alpha(0.5)
lgnd.legendHandles[4].set_alpha(0.5)
lgnd.legendHandles[5].set_alpha(0.5)
lgnd.legendHandles[6].set_alpha(0.5)
lgnd.legendHandles[7].set_alpha(0.5)
lgnd.legendHandles[8].set_alpha(0.5)
lgnd.legendHandles[9].set_alpha(0.5)
lgnd.legendHandles[10].set_alpha(0.5)
lgnd.legendHandles[11].set_alpha(0.5)

plt.show()
