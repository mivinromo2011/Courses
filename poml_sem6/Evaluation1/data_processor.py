#%%
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sb
from scipy.stats import iqr

#%%
data=pd.read_csv(r'heart.csv')

#%%
print(data.shape)
print(data.info)

#%%
print(data.isna().sum())

#%%
print(data.mean())

#%%
print(data.mode())
print(data.median())
print(data.std())
print(data.var())

#%%
for(cname,cvalue) in data.iteritems():
	print(cname,' : ',iqr(cvalue.values))

#%%
data.describe()

#%%
data.target.value_counts()

#%%
affected = data[data['target']==1]
not_affected = data[data['target']==0]

#%%
affected.describe()

#%%
not_affected.describe()

#%%
plt.style.use('ggplot')

#%%
sb.lineplot(data['age'], data['cp'])
plt.xlabel('Age')
plt.ylabel('Chest Pain Type')
plt.show()

#%%
sb.lineplot(data['cp'], data['chol'])
plt.xlabel('Chest Pain Type')
plt.ylabel('serum cholestoral')
plt.show()

#%%
sb.lineplot(data['age'], data['thal'])
plt.xlabel('Age')
plt.ylabel('Thal')
plt.show()

#%%
sb.lineplot(data['sex'], data['cp'])
plt.xlabel('Sex')
plt.ylabel('Chest Pain Type')
plt.show()