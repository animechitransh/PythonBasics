from importlib import import_module
import  pandas as py

data = ({'Animal': ['Falcon', 'Falcon', 'Parrot', 'Parrot','Falcon'],
                   'Max Speed': [380., 370., 24., 26.,380]})


df = py.DataFrame(data)

df['dup_number'] = df.groupby(list(df.columns)).cumcount()+1
k = 10
