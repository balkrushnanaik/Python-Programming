import pandas as pd

data = {
    "Student_ID": range(1, 21),

    "Name": [
        "Amit","Riya","Rahul","Sneha","Karan",
        "Priya","Rohit","Anjali","Vikas","Neha",
        "Arjun","Pooja","Sagar","Komal","Nikhil",
        "Meena","Yash","Isha","Dev","Tanvi"
    ],

    "Maths":  [78,85,90,66,88,92,75,80,70,89,95,60,84,73,91,77,68,82,87,79],
    "Science":[82,79,88,72,90,85,80,76,69,91,93,65,81,74,89,78,71,83,86,80],
    "English":[75,88,92,70,85,90,78,82,74,87,91,68,80,77,88,79,72,84,89,81],
    "Computer":[90,92,95,85,93,97,88,91,86,94,98,80,89,87,96,90,83,92,95,88]
}

df = pd.DataFrame(data)

print(df)

#Selecting Columns

#Multiple Columns
print(df[['Science','English','Computer']])

#Selectiing Rows
#Using Index
print(df.iloc[0])

__doc__='''Filtering Data in Pandas DataFrame \n'''
print(__doc__)

# print(df[df[['Science','Maths','English',"Computer"]]>80])

print(df[df['Name']=='Sneha'])
# print(df[df['Name']=='Riya'])
# print(df[df['Name']=='Rahul'])

__doc__='''Data Cleaning in Pandas \n'''
print(__doc__)

print(df.isnull())
print(df.duplicated())
