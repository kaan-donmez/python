import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_excel('data.xlsx')
years = data['Year']
populationBillions = data['Population']

plt.figure()
plt.plot(years, populationBillions, marker='o', linestyle='-', color='green')

plt.xlabel('Year')
plt.ylabel('Population (Billions)')
plt.title('World Population Growth (1951-2023)')

plt.gca().yaxis.set_major_locator(plt.MaxNLocator(10))

plt.grid(True, which='both', linestyle='--', linewidth=0.5)

plt.show()
