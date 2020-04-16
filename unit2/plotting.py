# Imports the pylab library with a custom name so we can quickly refer to it for plotting.
import pylab as plt

# Data setup.
# Simply creating linear, quadratic, cubic and exponential data sets for numbers
# 1 - 29, inclusive.
mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)

# Lets me start editing a figure named line with future calls to plt.
plt.figure('line')
# Clears any information that might already be a part of the active
# figure.
plt.clf()
# Adds a label to the x-axis of the currently open figure.
plt.xlabel('X Values')
# Adds a label to the y-axis of the currently open figure.
plt.ylabel('Linear Values')
# Adds a title to the currently open figure.
plt.title('Linear')
# Sets the y-min and y-max for the currently open figure.
plt.ylim(0, 1000)
# Adds the data to the plot, with a label for the series.
# mySamples = x-values, myLiner = y-values
plt.plot(mySamples, myLinear, label = "Linear")
# Tells pylab to include a legend for the active plot.
# Can also specify a location, like 'upper left', if desired.
plt.legend()

# A more advanced plot, perhaps.
plt.figure('quad cub')
plt.clf()
# I can specify options, like 'b-' or 'ro' to customize how the data is displayed.
# I can also change the linewidth
plt.plot(mySamples, myQuadratic, 'b-', label='Quadratic', linewidth=4.0)
plt.plot(mySamples, myCubic, 'ro', label='Cubic', linewidth=5.0)
plt.legend(loc='upper left')
plt.title('Linear vs. Quadratic')

# Even more advanced, because of subplots.
plt.figure('lin quad')
plt.clf()
# Arguments here are in the form rci
# r = number of rows
# c = number of columns
# i = index
# So here we are creating a plot with 2 rows of subplots, and 1 column.
# The first subplot we specify will be index one of these plots.
plt.subplot(211)
plt.ylim(0, 900)
plt.plot(mySamples, myLinear, 'b-', label='Linear')
plt.subplot(212)
plt.ylim(0, 900)
plt.plot(mySamples, myQuadratic, 'ro', label='Quadratic')
plt.legend('upper left')
plt.title('Linear vs. Quadratic')

# Renders all the plots that have been configured in their own windows.
plt.show()