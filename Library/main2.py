import pandas as pd

df = pd.DataFrame({
    'Name':['Barack','Obama','Donald','Balkrushna'],
    'Age':[21,22,23,24],
    'Gender':['Female','Male','Female','Male'],

})

df.to_csv('Data.csv', index=False)
