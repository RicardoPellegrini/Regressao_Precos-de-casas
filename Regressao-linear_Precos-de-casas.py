
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


base = pd.read_csv('house_prices.csv')


# In[3]:


base.head()


# In[4]:


# Variáveis preditoras (previsores)
X = base.iloc[:, 3:19].values


# In[5]:


# Variável target (classe)
y = base.iloc[:, 2].values


# In[6]:


# Dividindo dataset entre treino e teste com 30% para teste
from sklearn.model_selection import train_test_split


# In[7]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)


# In[8]:


# Modelo de regressão linear
from sklearn.linear_model import LinearRegression


# In[9]:


regressor = LinearRegression()


# In[10]:


regressor.fit(X_train, y_train)


# In[15]:


# Calculando precisão do modelo treinado aplicado ao dataset de teste
score = regressor.score(X_test, y_test)
score


# In[16]:


previsoes = regressor.predict(X_test)


# In[17]:


# Calculando erro absoluto médio para o modelo
from sklearn.metrics import mean_absolute_error


# In[18]:


mae = mean_absolute_error(y_test, previsoes)
mae

