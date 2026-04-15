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