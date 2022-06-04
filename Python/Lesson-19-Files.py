inputfile = "user_names.txt"
outputfile = 'mypasswords.txt"'

password_tolookfor = "Vasyl"

myfile = open(inputfile, mode='r', encoding ='utf_8')
myfile2 = open(outputfile, mode='a', encoding='utf_8') #append (dodatu do failu)

for num, line in enumerate(myfile, 1):
    if password_tolookfor in line:      #if Petrovich in user_names.txt of 100000 users - see only Petrovich
        print("Line #: " + str(num) + " : " + line.strip()) #delete empty probel
        myfile2.write("Found Name: " + line)

myfile.close()
myfile2.close()
