class Hero():
    "Class to Create Hero for our Game"
    def __init__(self, name, level, race):
        "Initiate our hero"
        self.name = name
        self.level = level
        self.race = race
        self.health = 100

    def show_hero(self):
        "Print all parameters of this Hero"
        discription = (self.name + " Level is: " + str(self.level) + "\nRace is:" + self.race + "\nHealth is:" + str(self.health))
        print(discription)
    def level_up(self):
        "Upgrade Level of Hero"
        self.level +=1

    def  move(self):
        "Start moving hero"
        print("Hero " + self.name + " start moving...")
    def set_health(self, new_health):
        self.health = new_health
#####112312312
12312312