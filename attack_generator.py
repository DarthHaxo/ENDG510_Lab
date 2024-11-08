# first of all import the socket library
import socket
import pandas as pd # in case of error, install pnadas using: pip install pandas
import numpy as np

import os
import re

def get_next_filename():
    # Regex pattern to find files with the format 'data_n.csv'
    pattern = re.compile(r"train_data_(\d+)\.csv")
    max_n = 0

    # Search through files in the current directory
    for filename in os.listdir('.'):
        match = pattern.match(filename)
        if match:
            n = int(match.group(1))
            max_n = max(max_n, n)

    # Create the next filename
    next_filename = f"data_{max_n + 1}.csv"
    return next_filename

# Run the function
print(get_next_filename())



# Create an empty Pandas DataFrame
df = pd.DataFrame(columns=['Temp', 'Humd', 'Label']) # Label: 1 means valid, 0 means invalid
df = pd.read_csv("data_1.csv")
df.head()
# next create a socket object

# coming from other computers on the network


# a forever loop until we interrupt it or
# an error occurs

i = 1000 # only 10 reading will be taken. Increase it to higher according to youplan.
while i>=0:

    temp= np.random.rand()*1000
    hum = np.random.rand()*1000
    new_data = {
    'Temp': temp,
    'Humd': hum,
    'Label': 0
    }
    df = df._append(new_data, ignore_index=True)
    i = i - 1
# Close the connection with the client
#Export data to CSV
name = get_next_filename()
df.to_csv(name, index=False)