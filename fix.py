# Wiebe Jelsma, 12468223
# Code to plot this

# Import everything
import pandas
import matplotlib.pyplot as plt
# Read in data
data = pandas.read_csv("istherecorrelation.csv", delimiter = ';')

# Get the right data
x = data['WO [x1000]']
y = data['NL Beer consumption [x1000 hectoliter]']

# Get everything to plot and safe it
plt.figure(dpi=300)
plt.plot(x,y, color = 'orange')

plt.xlabel('Amount of students')
plt.ylabel('Hectoliters of beer (x1000)')
plt.title('Beer consumption of the dutch students')
plt.savefig('picture.pdf')
plt.show()