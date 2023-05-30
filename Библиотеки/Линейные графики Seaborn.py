import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv(r'C:\Users\Aleksey\Desktop\real_estate.csv')
sns.lineplot(data=dataset, x='No', y='Transact Date')
plt.show()
sns.lineplot(data=dataset, x='No', y='Age')
plt.show()
sns.lineplot(data=dataset, x='No', y='Distance To Transport')
plt.show()
sns.lineplot(data=dataset, x='No', y='Shops')
plt.show()
sns.lineplot(data=dataset, x='No', y='Latitude')
plt.show()
sns.lineplot(data=dataset, x='No', y='Longitude')
plt.show()
sns.lineplot(data=dataset, x='No', y='Price')
plt.show()
