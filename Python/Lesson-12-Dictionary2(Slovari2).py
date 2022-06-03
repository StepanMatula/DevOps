enemy = {
#    (keys)   (value)
    'loc_x': 70,
    'loc_y': 50,
    'color': 'green',
    'health': 100,
    'name': 'BOT',
    'iamge': ['image1.jpg', 'image2.jpg', 'image3.jpg']
}

all_enemies =[]
all_enemies.append(enemy)
all_enemies.append(enemy)
all_enemies.append(enemy)

for x in range (0, 10):
    all_enemies.append(enemy.copy())

for ene in all_enemies:
    print(ene)

all_enemies[5]['health'] = 30 #change info in 5 str
all_enemies[8]['name'] = 'Baby Bot' #change info in 8 str
all_enemies[2]['loc_x'] +=10 #plus 10 to loc_x



print("-------------------")
for ene in all_enemies:
    print(ene)