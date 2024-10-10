import pandas as pd
import matplotlib.pyplot as plt

courselist = ["CCIT","CCDM","CCNS"]
courseID= [101,102,103]

#tp use panda's Dataframe function
#create a dictionary
courseDict = {'course':coursrlist,'ID':courseID}

#Use function--> DATAFRAME
myvariable = pd.DataFrame(courseDict)
#print(myvariable)

#panda series
myvariable2 = pd.Series(courseDict)
#print(myvariable2)

#reading csv files
pulsedata = pd.read_csv('pulse.csv')
#print(myvariable3)

undate1 = pulsedata.dropna()
#print(undate1)

#chamging data format
undate2 = pd.read_csv('pulse.csv')
undate2['Date'] = pd.to_datetime['Date']
#print(undate2)

            
