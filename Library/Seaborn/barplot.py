import matplotlib.pyplot as plt # type: ignore
import seaborn as sns # type: ignore


# Sample data
df = sns.load_dataset('tips')
# print(df.head()) # Head returns the first 5 rows of the dataset

# Create a bar plot
sns.barplot(x='total_bill', y='tip', data=df, ci=None) # ci=None removes the confidence interval
# Set the title and labels
plt.title('Total Bill vs Tip by Day')
plt.xlabel('Total Bill')
plt.ylabel('Tip')
# Show the plot 
plt.show()