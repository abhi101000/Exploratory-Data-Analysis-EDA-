#Task 2: Exploratory Data Analysis (EDA) - Titanic Dataset

## 📌 Objective
The goal of this task is to explore, analyze, and clean the Titanic dataset using Exploratory Data Analysis (EDA) techniques. This step helps us understand data distribution, identify patterns, detect outliers, and handle missing values, which are essential before applying machine learning models.

---

## 📁 Dataset Description

The dataset contains information about passengers aboard the RMS Titanic. It includes features such as:

- *PassengerId*: Unique identifier
- *Survived*: 0 = No, 1 = Yes
- *Pclass*: Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd)
- *Name, Sex, Age*
- *SibSp*: # of siblings/spouses aboard
- *Parch*: # of parents/children aboard
- *Ticket, Fare, Cabin, Embarked*

---

## 🔧 Steps Performed

### 1. Data Loading
- Loaded the dataset using Pandas from .xlsx and converted to .csv.

### 2. Data Cleaning
- Filled missing values in Age with median.
- Filled missing values in Embarked with mode.
- Dropped the Cabin column (too many missing values).
- Encoded Sex (0 = male, 1 = female).
- One-hot encoded the Embarked feature.

### 3. Data Visualization
Used Matplotlib and Seaborn to explore the data:
- 📊 *Histograms* of numeric features
- 🧊 *Boxplots* to compare Age/Fare with Survived/Pclass
- 🔥 *Heatmap* to show feature correlations
- 🔄 *Pairplot* to show multi-feature relationships

### 4. Feature Distribution and Skewness
- Checked for skewed features using .skew()

### 5. Data Export
- Saved cleaned dataset as cleaned_titanic_dataset.csv

---

## 📈 Key Insights

- *Survival Rate* was higher among *females* and *1st class* passengers.
- *Age and Fare* showed moderate variation and some skewness.
- Strong negative correlation between *Pclass* and *Fare*.
- Most passengers embarked from *Southampton*.

---

## 🧪 Tools & Libraries Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

## 📎 Files Included

- titanic.csv – Original dataset
- cleaned_titanic_dataset.csv – Cleaned dataset
- task2_eda.py– EDA code
- README.md – This documentation

---

## ✅ Conclusion

This EDA process provided a detailed understanding of the Titanic dataset and cleaned it for future modeling. The visualizations helped identify key patterns that will improve model performance in future tasks.
