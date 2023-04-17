import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='original data', zorder=1)

    # Create first line of best fit
    bf = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    extra = []
    for i in range(2013,2050,1):
        extra.append(i)
        
    ext_years = pd.concat([pd.DataFrame(extra), df['Year']])
    plt.plot(ext_years[0], bf.intercept + bf.slope*ext_years[0], 'k', label='best-fit line', zorder=2)

    # Create second line of best fit
    newmillenia = df[df['Year']>1999]
    bf2 = linregress(newmillenia['Year'], newmillenia['CSIRO Adjusted Sea Level'])
    extra2 = []
    for j in range(2013,2050,1):
        extra2.append(j)
        
    ext_years2 = pd.concat([pd.DataFrame(extra2), newmillenia['Year']])
    plt.plot(ext_years2[0], bf2.intercept + bf2.slope*ext_years2[0], 'r', label='best-fit line', zorder=3)

    # Add labels and title
    xmin, xmax = plt.xlim()
    plt.xlim(xmin * 1, xmax = 2060)
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.legend()
    plt.show()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()