import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import interactive

# -------------------------------------------------
# CSCI 127, Lab 13                                |
# November 26, 2019                               |
# Kristoff Finley                                 |
# -------------------------------------------------

def main(file_name):
    # read the file_name into a pandas dataframe
    count = 2 #initilaize count to help later with assigning the x and y axis from the data 
    data = pd.read_csv(file_name)
    for line in data:
        if count%2 == 0: #the "first" column in the data is the x axis
            x_axis = line
        else:
            y_axis = line #the "second" column in the data is the y axis 
        count +=1 
    # plot the dataframe using arguments "title", "legend", "x", "y", "kind" and "color"
    data.plot(x=x_axis, y = y_axis, kind = "bar", color = ["blue", "gold"],legend = False, title = file_name[:-4])
    plt.subplots_adjust(bottom=0.3)
    # The only four statements that may use the matplotlib library appear next.
    # Do not modify them.
    plt.xlabel(x_axis)      # Note: x-axis shou ld be determined above
    plt.ylabel(y_axis)      # Note: y-axis should be determined above
    interactive(True)       # This allows multiple figures to be displayed simultaneously
    plt.show()

# -------------------------------------------------

main("MSU College Enrollments.csv")
main("CS Faculty.csv")
