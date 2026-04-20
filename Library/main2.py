import pandas as pd # type: ignore


df = pd.DataFrame({
    'Name':['Barack','Obama','Donald','Balkrushna'],
    'Age':[21,22,23,24],
    'Gender':['Female','Male','Female','Male'],

})

# df.to_csv('Data.csv', index=False)
# df.to_excel('Data.xlsx', index=False)

# Create a dataframe for products

df2 = pd.DataFrame({
    'Product':['Laptop','Smartphone','Tablet','Headphones'],
    'Price':[1000, 500, 300, 150],
    'Stock':[50, 200, 150, 300]
})

print(df)
print(df2)

# Writing Multiple Sheets to Excel

with pd.ExcelWriter('Products.xlsx') as writer:
    df.to_excel(writer, sheet_name='Students', index=False)
    df2.to_excel(writer, sheet_name='Products', index=False)


# Appending Data to Existing Files

