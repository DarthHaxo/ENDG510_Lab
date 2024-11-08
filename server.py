# first of all import the socket library
import socket
import pandas as pd # in case of error, install pnadas using: pip install pandas


import os
import re

def get_next_filename():
    # Regex pattern to find files with the format 'data_n.csv'
    pattern = re.compile(r"data_(\d+)\.csv")
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
# next create a socket object
s = socket.socket()
print ("Socket successfully created")
# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 8000
# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))
print ("socket binded to %s" %(port))
# put the socket into listening mode
s.listen(5)
print ("socket is listening")
# Establish connection with client.
c, addr = s.accept()
print ('Got connection from', addr)
# a forever loop until we interrupt it or
# an error occurs
i = 1000 # only 10 reading will be taken. Increase it to higher according to youplan.
while i>=0:
    #receive data from client
    client = c.recv(1024)
    data = client.decode()
    temp = data.split(" ")[0]
    hum = data.split(" ")[1]
    new_data = {
    'Temp': temp,
    'Humd': hum,
    'Label': 1
    }
    df = df._append(new_data, ignore_index=True)
    #print it
    print(data)
    i = i - 1
# Close the connection with the client
c.close()
#Export data to CSV
name = get_next_filename()
df.to_csv(name, index=False)