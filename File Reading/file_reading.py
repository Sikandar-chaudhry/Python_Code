countries_file = open ("countries.txt","r")
for line in countries_file:
    print (line.strip())

countries_file.close()
