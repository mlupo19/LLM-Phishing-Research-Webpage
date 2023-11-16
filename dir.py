# Create 150 directories in the current directory, named 1 to 150.
# Copy the files index.html, style.css, and index.js into each directory.

import os

# Create 150 directories
for i in range(1, 151):
    os.mkdir(str(i))

# Copy files into each directory (Windows)
for i in range(1, 151):
    os.system('copy index.html ' + str(i))

# Print the number of directories created
print('Number of directories created: ' + str(len(os.listdir('.'))))