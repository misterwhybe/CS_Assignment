# Wiebe Jelsma, 12468223
# code to plot this

# import everything
import pandas
import matplotlib.pyplot as plt
# read in data
data = pandas.read_csv("istherecorrelation.csv", delimiter = ';')

# get the right data
x = data['WO [x1000]']
y = data['NL Beer consumption [x1000 hectoliter]']

# get everything to plot and safe it
plt.figure(dpi=300)
plt.plot(x,y, color = 'orange')

plt.xlabel('Amount of students (x1000)')
plt.ylabel('Hectoliters of beer (x1000)')
plt.title('Beer consumption of the dutch students')
# not really beautiful but it works
plt.savefig('picture.pdf')
plt.show()