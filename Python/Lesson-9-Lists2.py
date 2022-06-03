#         0      1     2       3
cars = ["bwm", "vw", "seat", "alfa"]

for x in cars:
    print(x.upper())

for x in range(1, 6):
    print(x)

mynumber_list = list(range(0,10))
print(mynumber_list)
print("=========================")

for x in mynumber_list:
    x = x *3
    print(x)

mynumber_list.sort(reverse=True)
print(mynumber_list)

print("Max number is: " + str(max(mynumber_list)))
print("Max number is: " + str(min(mynumber_list)))
print("Sum of lists is: " + str(sum(mynumber_list)))

print("==========================")
#         0      1     2       3
cars = ["bwm", "vw", "seat", "alfa"]
mycars = cars[1:4]
print(mycars)
mycars = cars[-4:]
print(mycars)

#         0      1     2       3
cars = ["bwm", "vw", "seat", "alfa"]
mycars = cars[:] #copy module
