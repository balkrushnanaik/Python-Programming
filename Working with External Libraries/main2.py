import pandas as pd 

data = {
   "Name": ["Vaibhav","Ganesh", "Rahul","Mahesh","Sunil","Narayan","Mahi","Soumya","Diksha","Aarya","Shivani","Shirly"],
   "Age": [22,23,24,23,56,24,34,25,26,27,28,26]
}

df = pd.DataFrame(data)
# print(df)

print(df.head())


