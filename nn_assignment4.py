
import pandas as pd
df=pd.read_csv('data.csv')
df.describe() #Basic statistical description of the data

df.isnull().sum() #checking if there are any null values

df['Calories'].fillna(df['Calories'].mean(),inplace=True)# replacing the null values with mean
df['Calories'].isnull().sum() #checking if null still exists

df.groupby(['Duration','Pulse']).agg({'Calories':['min','max','count','mean'],'Maxpulse':['min','max','count','mean']})#aggregation of duration,pulse using calories and Maxpulse

df[(df['Calories'].between(500,1000))]#calories between 500 and 1000 data

df[(df['Calories'] > 500) & (df['Pulse'] <= 100)]#calories >500 and pulse<100 data

df_modified=df.loc[:,df.columns!='Maxpulse']
df_modified#df without maxpulse

df.drop('Maxpulse',axis=1) #detlting Maxpulse in the main df

df['Calories']=df['Calories'].astype(int)#converting the data type to int
type(df['Calories'][0])

df.plot.scatter(x='Duration',y='Calories') #scatter plot

sdf=pd.read_csv('Salary_Data (1).csv')
sdf.describe()#salary data description

from sklearn.model_selection import train_test_split
x_train, x_test,y_train,y_test = train_test_split(sdf.iloc[:, :-1].values,sdf.iloc[:,1].values,test_size =0.2)
x_train#checking train data

from sklearn.linear_model import LinearRegression
m=LinearRegression()#linearregression
m.fit(x_train, y_train)#fitting the data for the linear regression

y_pred=m.predict(x_test)#predicting the data for testing using the uilt model
#y_pred*z+min(sdf['Salary'])

import math
from sklearn.metrics import mean_squared_error as ms
ms(y_pred,y_test)#mean square error

import matplotlib.pyplot as plt
plt.scatter(x_train,y_train)

plt.scatter(x_test,y_test)
