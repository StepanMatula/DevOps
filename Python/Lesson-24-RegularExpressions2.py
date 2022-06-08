import re
input_filename = "./data_emails.html"
result_filename = "./result_emailss.txt"

inputfile = open(input_filename, mode='r', encoding='utf_8')
resultfile = open(result_filename, mode='w', encoding='utf_8')

mytext = inputfile.read()

lookfor = r"[\w._-]+@[\w._-]+\.[\w.]+" #best regular expression for email adresses

results = re.findall(lookfor, mytext)

for item in results:
    print(item)
    resultfile.write(item + "\n")

print("total: " + str(len(results)))
