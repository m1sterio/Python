import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
dataset = pd.read_csv(r'C:\Users\Aleksey\Desktop\real_estate.csv')
sns.countplot(data=dataset, x='Transact Date')
plt.show()
sns.countplot(data=dataset, x='Age')
plt.show()
sns.countplot(data=dataset, x='Distance To Transport')
plt.show()
sns.countplot(data=dataset, x='Shops')
plt.show()
sns.countplot(data=dataset, x='Latitude')
plt.show()
sns.countplot(data=dataset, x='Longitude')
plt.show()
sns.countplot(data=dataset, x='Price')
plt.show()
