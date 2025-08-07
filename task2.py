# Task 2: Exploratory Data Analysis - Titanic Dataset


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")


df = pd.read_csv("titanic.csv")


print("First 5 rows of dataset:")
print(df.head())

print("\nDataset Shape:", df.shape)
print("\nData Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())


df["Age"].fillna(df["Age"].median(), inplace=True)

df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)


df.drop("Cabin", axis=1, inplace=True)


df["Sex"] = df["Sex"].map({"male": 0, "female": 1})

df = pd.get_dummies(df, columns=["Embarked"], drop_first=True)


print("\nDescriptive Statistics:")
print(df.describe())




df.hist(figsize=(12, 10), bins=20)
plt.suptitle("Histogram of Numeric Features", fontsize=16)
plt.tight_layout()
plt.show()


plt.figure(figsize=(7, 5))
sns.boxplot(x="Survived", y="Age", data=df)
plt.title("Age Distribution by Survival")
plt.show()


plt.figure(figsize=(7, 5))
sns.boxplot(x="Pclass", y="Fare", data=df)
plt.title("Fare Distribution by Class")
plt.show()


plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()


sns.pairplot(df[["Survived", "Age", "Fare", "Pclass", "Sex"]])
plt.suptitle("Pairplot of Key Features", y=1.02)
plt.show()


print("\nSkewness of Numeric Features:")
print(df.skew(numeric_only=True))


df.to_csv("cleaned_titanic_dataset.csv", index=False)
print("\nCleaned data saved as 'cleaned_titanic_dataset.csv'")