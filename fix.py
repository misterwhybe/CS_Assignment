import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv("istherecorrelation.csv", delimiter = ';')
data = pandas.DataFrame(data)
# print(data['WO [x1000]'])
x = data['WO [x1000]']
y = data['NL Beer consumption [x1000 hectoliter]']
plt.figure(dpi=300)
plt.plot(x,y, color = 'orange')

plt.xlabel('Amount of students')
plt.ylabel('Hectoliters of beer (x1000)')
plt.title('Beer consumption of the dutch students')
plt.savefig('picture.pdf')
plt.show()