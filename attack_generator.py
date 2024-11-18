# first of all import the socket library
import socket
import pandas as pd # in case of error, install pnadas using: pip install pandas
import numpy as np

import os
import re
path = r'C:\Users\levis\OneDrive\Documents\School_2024\ENDG_510\New folder\ENDG510_Lab'
os.chdir(path)
def get_next_filename(name):
    # Regex pattern to find files with the format 'data_n.csv'

    pattern = re.compile(name + r"(\d+)\.csv")
    max_n = 0

    # Search through files in the current directory
    for filename in os.listdir('.'):
        match = pattern.match(filename)
        if match:
            n = int(match.group(1))
            max_n = max(max_n, n)

    # Create the next filename
    next_filename = f"{name}_{max_n + 1}.csv"
    return next_filename

# Run the function



# Create an empty Pandas DataFrame
df = pd.DataFrame(columns=['Temp', 'Humd', 'Label']) # Label: 1 means valid, 0 means invalid
df = pd.read_csv("data_attack.csv")
df.head()
# next create a socket object

# coming from other computers on the network


# a forever loop until we interrupt it or
# an error occurs

for index, value in df['Temp'].items():
    df.at[index, 'Temp'] =float( value) +(np.random.rand()-0.5)
for index, value in df['Humd'].items():
    df.at[index, 'Humd'] =float( value) +(np.random.rand()-0.5)
# Close the connection with the client
#Export data to CSV
name = get_next_filename("data_attack_noisy")
df.to_csv(name, index=False)