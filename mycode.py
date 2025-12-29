import pandas as pd
import os
# Create a sample with column names
data = {'Name':['Alice' , 'Bob' , 'Charlie'],
'Age' : [25, 30, 35],
'City': ['New York', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)

# Adding new row to df for V2
new_row_loc= {'Name': 'GF1', 'Age': 20, 'City': 'Cityl'}
df.loc[len(df)] = new_row_loc

# $ Adding row to df for V3
# new_row_loc2 = {'Name': 'V3', 'Age': 30,
# df.loc[len(df.index)] = new_row_loc2

#Ensurethe "data" directory exists at the root level
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

# Define the file path to save the CSV file
filepath = os.path.join(data_dir, 'sample_data.csv')

# save the to a CSV file, including column names
df.to_csv(filepath, index=False)

print(f"CSV file saved to {filepath}" )