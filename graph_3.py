import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('sales.csv','r') as sales_csv:
    plots = csv.reader(sales_csv, delimiter=',')
    for row in plots:
        x.append(row[1])
        y.append(row[3])

plt.plot(x,y, label='Loaded from file!')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
