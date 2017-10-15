##Importing Data
#Let’s get the data to our local machines
wget https://raw.githubusercontent.com/lakshya90/learning-pandas/master/titanic.csv(curl -O <url> for mac)
#Let’s import relevant libraries
import pandas as pd
#Let’s read the file into a dataframe
df = pd.read_csv('titanic.csv') 

##Viewing/Inspecting Data
#Let’s see number of rows and columns
df.shape       # Output : 891,12
#Let’s see top 5 rows
df.head(5)
#Let’s see bottom 5 rows
df.tail(5)
#Let’s see some more information on the rows and columns
df.info()       # Output : 891,12
#Let’s see some statistics for numerical fields
df.describe()
#Let’s see unique counts for each columns
df['Sex'].value_counts(); 
df['Survived'].value_counts();
df['Pclass'].value_counts() 

##Selection
#Let’s see the type when we pick a column
d = df['PassengerId']; type(d)   #<class ‘pandas.core.series.Series’>       
#Let’s see any one row features (Pick any number between 0 and 890)
df.iloc[654,:]

##Data Cleaning
#A few columns have NaN values. How do I know?
df.describe() #Check count of all features
df_a = df; df_a['Age'] = df_a['Age'].fill na(df_a['Age'].mean())
df_a['Age'].count() #891 from previous 714
#Let’s drop some irrelevant columns
df.drop(['PassengerId','Name','Ticket', 'Cabin'], axis=1)
#Let’s see how many null values exist for a certain column
pd.isnull(df['Cabin'])
df[df['Embarked'].isnull()]

##Filter, Sort, Group By
#Let’s see the count of upper class values
df['Pclass'].value_counts(); s = df['Pclass'] < 2; s.value_counts()
#Let’s sort all ages in ascending order
df.sort_values('Age')
#Let’s see Survivors grouped by Sex.
df.groupby('Sex')['Survived'].value_counts()
df.groupby('Sex').Survived.mean()

##Statistics
#Let’s see some statistics for categorical fields
df.describe(include=['O'])
#Let’s see some statistics for a few columns
df['Age'].mean()    #Mean of all values of the feature ‘Age’
df['Cabin'].count()    #Count of all valid ‘Cabin’ values
df['Fare'].max()   #Maximum fare paid for the ticket

##Exporting the Data
#Let's write the data to a csv file
df.to_csv('output.csv')















