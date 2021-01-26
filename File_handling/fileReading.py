
#use open function with argument as file name with the type of reading format

# putting the whole path
file = open(r'C:\Users\tusha\Documents\PYTHON_programs\File_handling\data.txt', 'r')

for line in file:
    print(line)


print("###Character printing below it ####")
#READING THE FILE AS PER CHARACTER BASICS
#put the value = {How many character inside read() functions}
char_read = file.read(20)
print(char_read)

file.close()