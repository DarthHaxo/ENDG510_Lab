
import pandas as pd
import random

file_path = '/Users/SeleemB/Library/Mobile Documents/com~apple~CloudDocs/Desktop/BMEN_project_code/BMEN478_code/ENDG510/data_1.csv' 
df = pd.read_csv(file_path)

#df_test=pd.DataFrame([[1, 1, 1], [3, 4, 1], [6, 7, 1]], columns=['Column1', 'Column2', 'Column3'])

#print(df_test)
i=0

while i<=200:
    # Randomly select a row index (1-1000, but adjusted for 0-based indexing)
    row_index = random.randint(0, 999)  # Python's indexing is 0-based

    # Generate two random numbers (for example, between 0 and 100 for each)
    new_value1 = random.randint(0, 150)
    new_value2 = random.randint(0, 150)

    # Replace the selected row with new values
    #df_test.iloc[row_index] = [new_value1, new_value2, 0]
    df.iloc[row_index] = [new_value1, new_value2, 0]

    i+=1

print(df)

# Save the updated DataFrame back to the CSV file
df.to_csv('data_attack.csv', index=False)
