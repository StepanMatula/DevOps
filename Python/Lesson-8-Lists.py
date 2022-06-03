cities =['Lutsk', 'Kyiv', 'Lviv', 'Odesa', 'Ternopil']
print(cities)
print(len(cities)) #len - dlina
print(cities[0])
print(cities[-1])
print(cities[2].title())

cities.append('111') #add city
cities.append('222')
print(cities)

cities.insert(0, '333') #zamist Lutsk - 333
print(cities)

del cities [-1]
print(cities)

cities.remove('Kyiv')
print(cities)

deleted_city = cities.pop()
print("Deleted city is: " +deleted_city)
print(cities)

cities.sort()
print(cities)
cities.reverse()
print(cities)


