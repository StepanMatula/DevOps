#Java Script Object Notation

import json

filename="user_settings.txt"
myfile=open(filename, mode='w', encoding='utf_8')

player1 = {
    'PlayerName': "Donald Trump",
    'Score': 345,
    'Awards': ["OR", "NV", "NY"]
}

player2 = {
    'PlayerName': "Bill Clinton",
    'Score': 410,
    'Awards': ["QW", "TX", "UI"]
}
myplayers=[]
myplayers.append(player1)
myplayers.append(player2)

 #------------------ SAVE by JSON ----------
json.dump(myplayers, myfile)
myfile.close()

#------------------ LOAD by JSON------------

myfile=open(filename, mode='r', encoding='utf_8')
json_data=json.load(myfile)

for user in json_data:
    print("Player Name is: " + str(user['PlayerName']))
    print("Player Score is: " +str(user['Score']))
    print("Player Award #1: " + str(user['Awards'][0]))
    print("Player Award #1: " + str(user['Awards'][1]))
    print("Player Award #1: " + str(user['Awards'][2]))
    print("-------------------------------------\n")
