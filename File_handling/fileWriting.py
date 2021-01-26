
# w parameter will always overwrite the data
file = open(r'C:\Users\tusha\Documents\PYTHON_programs\File_handling\fileWrite','w')

file.write('are you')

file.close()

# a to append the data till the last cursor of the file
file = open(r'C:\Users\tusha\Documents\PYTHON_programs\File_handling\fileWrite','a')

file.write('Tushar here , appending the data')

file.close()

