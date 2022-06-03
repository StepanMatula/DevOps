x=25

if x == 25:
    print("YES, you Right!")
else:
    print("No, you are wrond")

age=13

if age <= 4:
    print("You are baby")
elif age >4 and age <13:
    print("You are kid")
elif age >12 and age <23:
    print("You are teenager")
else:
    print("You are old")

print("========END=======\n")

all_cars = ['chevrolet', 'lada', 'vaz', 'vw', 'bmw', 'seat', 'audi']
german_cars = ['bmw', 'vw', 'audi']
if 'vw' in all_cars:
    print("Yes, LADA is in the list")
else:
    print("LADA Not in the list")

print("========END=======\n")

for xxx in all_cars:
    if xxx in german_cars:
        print(xxx + " is German Car")
    else:
        print(xxx + " is not German Car")

