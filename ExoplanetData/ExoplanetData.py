# This program draws a graph incorporating planet mass, radius, orbital period and detection method for confirmed exoplanets
#
import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import matplotlib.cm as cm
from matplotlib.colors import Normalize
import pathlib

data_dir = str(pathlib.Path(__file__).parent.absolute()) + os.sep + "data" + os.sep  # find directory containing csv
filename = "ConfirmedPlanets.csv"  # choose csv
df = pd.read_csv(data_dir + filename)  # read_csv loads the file
df = df.dropna(subset=["pl_bmassj", "pl_radj"])
color_list = df['pl_discmethod'].tolist()  # generate list
color_list_unique = ["Pulsar Timing", "Transit", "Microlensing", "Radial Velocity", "Imaging",
                     "Orbital Brightness Modulation",
                     "Transit Timing Variations", "Eclipse Timing Variations", "Pulsation Timing Variations",
                     "Disk Kinematics", "Astrometry"]
color_list_numeric = color_list
color_list_dict = {color_list_unique[i]: i / 11 for i in range(len(color_list_unique))}
for n, i in enumerate(color_list_numeric):
    color_list_numeric[n] = color_list_dict[i]

norm = mpl.colors.Normalize(vmin=0, vmax=1)  # normalisation for colormap
cmap = cm.hsv  # cyclic rainbow pattern (can change to others if you want to)
m = cm.ScalarMappable(norm=norm, cmap=cmap)  # apply cmap and norm
colors = m.to_rgba(color_list_numeric)  # generate colours for later plotting


def choose_graph():  # function to choose start and end points to focus on
    x_start = input("Set the starting point for x: ")
    x_end = input("Set the ending point for x: ")
    y_start = input("Set the starting point for y: ")
    y_end = input("Set the ending point for y: ")
    if x_start and x_end != "":
        if x_start == x_end or y_start == y_end:  # bug prevention
            print("Start and end points cannot be the same.")
            choose_graph()  # loop if failed
        else:
            print()
            plt.xlim(x_start, x_end)
    else:
        print("Using default x boundaries.")
    if y_start and y_end != "":
        if x_start == x_end or y_start == y_end:  # bug prevention
            print("Start and end points cannot be the same.")
            choose_graph()  # loop if failed
        else:
            print()
            plt.ylim(y_start, y_end)
    else:  # default to fit all if no entries are recorded
        print("Using default y boundaries.")


choose_graph()

x_raw = list(df["pl_bmassj"])
y_raw = list(df["pl_radj"])
area_raw = df["pl_orbper"].to_numpy()
x = np.log(x_raw)  # take logs of x and y data
y = np.log(y_raw)

lobf, cov = np.polyfit(x, y, 1, cov=True)
line_fit = np.poly1d(lobf)
plt.plot(x, line_fit(x), aa=True)

area = np.sqrt(area_raw) * 1.5  # normalise areas to prevent jarring differences
plt.xlabel("ln(Planet Mass (Jupiter Masses))")  # apply titles and axis labels
plt.ylabel("ln(Planet Radius (Jupiter Radii))")
plt.title("A Graph of Confirmed Planet Radius against Planet Mass, with Colour "
          "Representing Detection Method and Size Representing Orbital Period")
plt.grid(b=True, which='major', color='#666666', linestyle='-')  # draw major gridlines
plt.minorticks_on()  # draw minor gridlines
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
# plt functions above will only draw the area dot in the legend

# below is the drawing function - full of cosmetic changes to make it look good
for i in range(11):
    plt.scatter(x, y, alpha=0.04, s=area, label=color_list_unique[i], c=colors)
    # the plt scatters occur 12 times, so alpha is 0.04 so that it is around 0.5 once all have been plotted
plt.scatter(x, y, alpha=0.04, s=area, label='area $\propto \sqrt{Orbital Period}$', c=colors)  # label for area
lgnd = plt.legend(scatterpoints=1, frameon=True, labelspacing=1, title='Point Colour and Size', prop={"size": 9}
                  #                  , loc = "center right", bbox_to_anchor=(0.15, 0.5) # change location of legend, commented = default
                  )  # draw legends
for i in range(12):
    lgnd.legendHandles[i]._sizes = [80]  # apply sizes to dots in the legend
    lgnd.legendHandles[i].set_alpha(0.5)  # set transparency of legend points(would be barely visible otherwise)
    if i == 11:
        lgnd.legendHandles[11].set_color("#222222")
    else:
        lgnd.legendHandles[i].set_color(cmap(i / 11))  # set legend point colours

plt.show()
