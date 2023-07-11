countries_file = open ("Python_Code/File Reading/countries.txt","r")
for line in countries_file:
    print (line.strip())

countries_file.close()
