import pandas as pd # type: ignore

# Create a dataframe for eccommerce products
df = pd.DataFrame({
    'Product':['Laptop','Smartphone','Tablet','Headphones','Smartwatch'],
    'Price':[1000, 500, 300, 150,200],
    'Stock':[50, 200, 150, 300, 250],
    'Category':['Electronics','Electronics','Electronics','Accessories','Wearables'],
    'Rating':[4.5, 4.2, 4.0, 4.3, 4.1],
    'Reviews':[150, 300, 200, 250, 180]

    })


df.to_csv('Eccomerce_Products.csv', index=False, mode='a', header=False)
