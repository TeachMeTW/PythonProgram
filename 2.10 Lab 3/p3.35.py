
from matplotlib import pyplot
import pandas as pd
import numpy as np
# You need to pip install numpy for the equation I used

def main():
    # Create a label array/list
    labels = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    # High temperatures measured
    high = [1.1,10.0,25.4,44.5,61.0,71.6,72.7,65.9,54.6,31.9,10.9,4.8]
    # Low temperatures measured
    low =  [-16.9,-12.7,-2.5,20.6,37.8,49.3,52.3,46.4,35.1,16.5,-5.7,-12.9]

    # arrange the data via numpy
    data1 = np.arange(len(high))
    # create spacing between data points
    data2 = [x+0.3 for x in data1]
    
    # Plot the bars using the arrays; high temp is red, low is green, label them
    pyplot.bar(data1, high, color = 'red', width=0.3, label='High Avg')
    pyplot.bar(data2, low, color = 'green', width=0.3, label='Low Avg')

    # x axis
    pyplot.xlabel('Months in the year')
    # y axis
    pyplot.ylabel('Temperature (Farenheight)')
    # graph title
    pyplot.title('Average temperatures in Fairbanks')

    # Add label of data above the bar
    pyplot.bar_label(pyplot.bar(data1, high, color = 'red', width=0.3, label='High Avg'), padding=3)
    pyplot.bar_label(pyplot.bar(data2, low, color = 'green', width=0.3, label='Low Avg'), padding=3)

    # Add tick marks to the graph
    pyplot.xticks([y + 0.3 for y in range(len(high))], labels)

    # Create legend
    pyplot.legend(['High', 'Low'])
    pyplot.show()

main()