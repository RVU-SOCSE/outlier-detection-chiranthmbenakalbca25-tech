##A
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:/Users/manub/Desktop/CHIRU/PYTHON/laptop.csv")


num_cols = df.select_dtypes(include=['int64', 'float64']).columns


plt.figure(figsize=(10, 5))
df[num_cols].boxplot()
plt.title("Boxplot using Matplotlib")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 5))
sns.boxplot(data=df[num_cols])
plt.title("Boxplot using Seaborn")
plt.xticks(rotation=45)
plt.show()


##B

for col in num_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    outliers = df[(df[col] < lower) | (df[col] > upper)]

    print(f"\nColumn: {col}")
    print(f"Lower Bound: {lower}, Upper Bound: {upper}")
    print(f"Number of Outliers: {len(outliers)}")
    print(outliers[[col]])
