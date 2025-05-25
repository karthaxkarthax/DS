# Pandas is a software library written for the Python programming language for data manipulation and analysis.
import pandas as pd
#NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays
import numpy as np

df = pd.read_excel('/Users/css145296/Desktop/Content/PyDev/Certify/F8.xlsx')
landing_outcomes=df['Outcome'].value_counts()
bad_outcomes=set(landing_outcomes.keys()[[1,3,5,6,7]])
landing_class=[]

for i in np.arange(len(df['Outcome'])):
    if (df['Outcome'][i] in bad_outcomes):
        landing_class.append(0)
    else:
        landing_class.append(1)


import pandas as pd
#NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays
import numpy as np
# Matplotlib is a plotting library for python and pyplot gives us a MatLab like plotting framework. We will use this in our plotter function to plot data.
import matplotlib.pyplot as plt
#Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics
import seaborn as sns

df = pd.read_excel('/Users/css145296/Desktop/Content/PyDev/Certify/F7.xlsx')

sns.catplot(y="PayloadMass", x="FlightNumber", hue="Class", data=df, aspect = 5)
plt.xlabel("Flight Number",fontsize=20)
plt.ylabel("Pay load Mass (kg)",fontsize=20)
plt.show()


# Plot a scatter sns.catplot(y="PayloadMass", x="FlightNumber", hue="Class", data=df, aspect = 5)
sns.catplot(y="LaunchSite", x="FlightNumber", hue="Class", data=df, aspect = 5)
plt.xlabel("Flight Number",fontsize=20)
plt.ylabel("Launch Site",fontsize=20)
plt.show()

sns.scatterplot(y="PayloadMass", x="LaunchSite", hue="Class", data=df)
plt.xlabel("Launch Site",fontsize=20)
plt.ylabel("Payload Mass",fontsize=20)
plt.show()

# Plot a scatter point chart with x axis to be FlightNumber and y axis to be the Orbit, and hue to be the class value
sns.scatterplot(y="Orbit", x="FlightNumber", hue="Class", data=df)
plt.xlabel("FlightNumber",fontsize=20)
plt.ylabel("Orbit",fontsize=20)
plt.show()

# Plot a scatter point chart with x axis to be Payload Mass and y axis to be the Orbit, and hue to be the class value
sns.scatterplot(y="Orbit", x="PayloadMass", hue="Class", data=df)
plt.xlabel("Payload Mass",fontsize=20)
plt.ylabel("Orbit",fontsize=20)
plt.show()


# Plot a scatter point chart with x axis to be FlightNumber and y axis to be the Orbit, and hue to be the class value


# A function to Extract years from the date
year=[]
df['Date']=pd.to_datetime(df["Date"])
def Extract_year():
    for i in df["Date"].dt.year:
        year.append(i)
    return year

Extract_year()
#df['Date'] = year
#df.head()

# Plot a line chart with x axis to be the extracted year and y axis to be the success rate
OrbitValues = df['Orbit'].value_counts()
print (":::",OrbitValues)
#for i in np.arange(len(OrbitValues)):
OrbitSuccessRate=df[df['Orbit']==OrbitValues[0]]

processedData = {'Year':[2010,2012,2013, 2014,2015,2016,2017,2018,2019,2020], 'SuccessRate':[0, 0, 0, 0.33, 0.33, 0.63, 0.83, 0.61, 0.90, 0.84]}
sns.lineplot(x='Year', y='SuccessRate', data=processedData)
#sns.scatterplot(y="Class", x="Orbit", hue= 'Class', data=df)
plt.xlabel("Year",fontsize=20)
plt.ylabel("Outcome",fontsize=20)
plt.show()

# A function to Extract years from the date
year=[]
df['Date']=pd.to_datetime(df["Date"])
def Extract_year():
    for i in df["Date"].dt.year:
        year.append(i)
    return year

Extract_year()
#df['Date'] = year
#df.head()

# Plot a line chart with x axis to be the extracted year and y axis to be the success rate
YearValues = df['Date'].value_counts()
YearSuccessRate=df[df['Date']==2020].mean()
print (YearSuccessRate)
sns.lineplot(y=YearSuccessRate, x="Date", data=df)
plt.xlabel("Payload Mass",fontsize=20)
plt.ylabel("Success Rate",fontsize=20)
plt.show()

features = df[['FlightNumber', 'PayloadMass', 'Orbit', 'LaunchSite', 'Flights', 'GridFins', 'Reused', 'Legs', 'LandingPad', 'Block', 'ReusedCount', 'Serial']]
features.head()

# HINT: Use get_dummies() function on the categorical columns
features_one_hot = pd.get_dummies (features, columns=['Orbit','LaunchSite', 'LandingPad', 'Serial', 'GridFins', 'Reused', 'Legs' ])

# HINT: use astype function
features_one_hot = features_one_hot.astype('float64')
