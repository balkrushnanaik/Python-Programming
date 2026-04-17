# Reading CSV & Excel Files with Pandas

import pandas as pd

try:
    df = pd.read_csv('data.csv')

    print(df.to_string())

    #Select all whose experience is greater than 17

    Experience = df[df['Experience_Years']>18]
    print(Experience.to_string())


except Exception as e:
    print(e)
