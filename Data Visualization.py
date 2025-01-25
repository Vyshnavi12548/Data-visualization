import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = sns.load_dataset('tips')

# Inspect the data
print(df.head())
print(df.isnull().sum())

# Filter data: Female customers
female_tips = df[df['sex'] == 'Female']
print(female_tips.head())

# Group data: Sum of total_bill and tip by day
grouped_by_day = df.groupby('day', observed=False).agg({'total_bill': 'sum', 'tip': 'sum'})
print(grouped_by_day)
# Add a new calculated column: Tip percentage
df['tip_percentage'] = (df['tip'] / df['total_bill']) * 100

# Data visualization
# Histogram of Total Bill
plt.hist(df['total_bill'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Total Bill')
plt.xlabel('Total Bill')
plt.ylabel('Frequency')
plt.show()

# Boxplot of Tip by Time
sns.boxplot(x='time', y='tip', data=df)
plt.title('Tip Distribution by Time (Lunch vs. Dinner)')
plt.show()

# Scatter plot of Total Bill vs Tip
sns.scatterplot(x='total_bill', y='tip', data=df)
plt.title('Total Bill vs Tip')
plt.show()

# Barplot of Average Tip Percentage by Day
avg_tip_percentage = df.groupby('day', observed=False)['tip_percentage'].mean().reset_index()
sns.barplot(x='day', y='tip_percentage', data=avg_tip_percentage)
plt.title('Average Tip Percentage by Day')
plt.show()

# Save the modified data to CSV
df.to_csv('modified_tips.csv', index=False)

# Save a plot
plt.hist(df['total_bill'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Total Bill')
plt.xlabel('Total Bill')
plt.ylabel('Frequency')
plt.savefig('total_bill_histogram.png')
