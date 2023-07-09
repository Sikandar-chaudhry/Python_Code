countries_file = open ("d:/Coding/WEB DEVELOPMENT/CS50W/lecture2/Python_Code/File Reading/countries.txt","r")
for line in countries_file:
    print (line.strip())

countries_file.close()