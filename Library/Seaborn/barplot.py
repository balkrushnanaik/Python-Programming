import matplotlib.pyplot as plt # type: ignore
import seaborn as sns # type: ignore


# Sample data
df = sns.load_dataset('tips')
print(df.head()) # Head returns the first 5 rows of the dataset