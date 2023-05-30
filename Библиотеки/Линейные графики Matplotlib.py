import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(r'C:\Users\Aleksey\Desktop\real_estate.csv',index_col=0, parse_dates=True)

dataset['Transact Date'].plot()
plt.ylabel('Transact Date')
plt.show()

dataset['Age'].plot()
plt.ylabel('Age')
plt.show()

dataset['Distance To Transport'].plot()
plt.ylabel('Distance To Transport')
plt.show()

dataset['Shops'].plot()
plt.ylabel('Shops')
plt.show()

dataset['Latitude'].plot()
plt.ylabel('Latitude')
plt.show()

dataset['Longitude'].plot()
plt.ylabel('Longitude')
plt.show()

dataset['Price'].plot()
plt.ylabel('Price')
plt.show()

