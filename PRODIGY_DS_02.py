# Step 1: Import necessary libraries 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
# Step 2: Load the Titanic dataset 
url = 
'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv' df = pd.read_csv(url) 
# Display the first few rows of the dataset 
print(df.head()) 
# Step 3: Data Cleaning 
# Check for missing values 
print(df.isnull().sum()) 
# Fill missing values 
df['Age'].fillna(df['Age'].median(), inplace=True) 
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True) 
df.drop(columns=['Cabin'], inplace=True) # Too many missing values 
# Verify that missing values are handled 
print(df.isnull().sum()) 
# Step 4: Exploratory Data Analysis (EDA) 
# Describe the dataset 
print(df.describe(include='all')) 
# Univariate analysis: Distribution of Age 
plt.figure(figsize=(10, 6)) 
sns.histplot(df['Age'], kde=True, bins=30) 
plt.title('Age Distribution') 
plt.xlabel('Age') 
plt.ylabel('Frequency') 
plt.show()
# Univariate analysis: Survival Rate 
plt.figure(figsize=(10, 6)) 
sns.countplot(x='Survived', data=df) 
plt.title('Survival Count') 
plt.xlabel('Survived') 
plt.ylabel('Count') 
plt.show() 
# Bivariate analysis: Survival rate by Gender 
plt.figure(figsize=(10, 6)) 
sns.countplot(x='Sex', hue='Survived', data=df) 
plt.title('Survival Count by Gender') 
plt.xlabel('Sex') 
plt.ylabel('Count') 
plt.show() 
# Bivariate analysis: Survival rate by Class 
plt.figure(figsize=(10, 6)) 
sns.countplot(x='Pclass', hue='Survived', data=df) 
plt.title('Survival Count by Class') 
plt.xlabel('Pclass') 
plt.ylabel('Count') 
plt.show() 
# Bivariate analysis: Age distribution by Survived 
plt.figure(figsize=(10, 6)) 
sns.histplot(df[df['Survived'] == 1]['Age'], kde=True, color='green', bins=30, label='Survived') 
sns.histplot(df[df['Survived'] == 0]['Age'], kde=True, color='red', bins=30, label='Did not Survive') 
plt.title('Age Distribution by Survival Status') 
plt.xlabel('Age') 
plt.ylabel('Frequency') 
plt.legend() 
plt.show() 
# Multivariate analysis: Survival by Age, Sex, and Class 
plt.figure(figsize=(12, 6)) 
sns.scatterplot(x='Age', y='Fare', hue='Survived', style='Sex', size='Pclass', data=df) 
plt.title('Survival by Age, Sex, and Class') 
plt.xlabel('Age') 
plt.ylabel('Fare') 
plt.show() 
