import random
from Saturn import monsterList

class character(object):
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.health = 20
        self.attack = 5
        self.defense = 5
        self.experience = 0
        self.escape = 1
    def get_name(self):
        return self.name
    def get_level(self):
        return self.level
    def get_health(self):
        return self.health
    def get_attack(self):
        return self.attack
    def get_defense(self):
        return self.defense
    def get_experience(self):
        return self.experience
    def get_escape(self):
        return self.escape
    def set_health(self, newHealth):
        self.health = newHealth
    def add_level(self):
        while self.experience >= 30:
            self.level += 1
            self.experience -= 30
            self.attack += random.randrange(0, 5)
            self.defense += random.randrange(0, 5)
            self.health += 10
            self.escape += 1
    def subtract_level(self):
        self.level -= 1
    def add_exp(self, n):
        self.experience += n
    def add_health(self, n):
        self.health += n
    def subtract_health(self, n):
        self.health -= n
    def add_attack(self, n):
        self.attack += n
    def add_defense(self, n):
        self.defense += n
    def change_escape(self):
            self.escape -= 1
    def __str__(self):
        return self.name + " " + "<Health: " + str(self.get_health()) + "> " +\
     "<Level: " + str(self.get_level()) + "> " + "<Experience: " + str(self.get_experience())\
    + "> " + "<Attack: " + str(self.get_attack()) + ">" + \
    " <Defense: " + str(self.get_defense()) + ">"
    
    
    

class monster(object):
     def __init__(self, name, health, hero):
         """
         hero: an object
         
         """
         self.health = health
         self.name = name
         self.attack = hero.get_attack()
         self.defense = hero.get_defense()
     def get_health(self):
         return self.health
     def get_name(self):
         return self.name
     def get_attack(self):
         return self.attack + random.randrange(-2, 2)
     def get_defense(self):
         return self.defense + random.randrange(-2, 2)
     def get_damage(self):
         self.damage = abs(self.get_attack() - 0.2 * hero.get_defense()) + 1.5
         return self.damage
     def subtract_health(self, n):
         self.health -= n
     def speak(self):
         return hero.get_name(self) + " die die die"
     def __str__(self):
         return "Boss " + "Health: " + str(self.health)


class easyMonster(monster):
    def __init__(self, name, health, attack, defense, experience, hero):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.experience = experience
    def get_health(self):
         return self.health    
    def get_attack(self):
        return self.attack
    def get_name(self):
        return self.name
    def get_defense(self):
        return self.defense
    def get_damage(self):
        self.damage = abs(self.attack - 0.2 * hero.get_defense()) + 2
        return self.damage
    def get_experience(self):
        return self.experience
    def speak(self):
        return hero.get_name(self) + " hahaha"
    def __str__(self):
         return self.name + " " + "Health: " + str(self.health)
    
#hero = character("John")
#monster = monster("James", 20, hero)    


def exert_damage(hero, monster):
    """
    A function designed for hero. 
    Exerting damage to monster
    
    """
    monsterDefense = monster.get_defense()
    damage = abs(hero.get_attack() - 0.2 * monsterDefense)
    monster.subtract_health(damage)
    

def fightBoss(hero, monster):
    """
   fighting between hero(object) and boss(object)
   The fighting cannot end until either monster or hero dies or hero escapes
    
    """
    record = None
    while True:
        userInput = input("enter 'a' to attack or enter 'e' to escape ")

        if userInput == "e":
            if hero.get_escape() > 0:
                hero.change_escape()
                break
            else:
                print("no chance for escape, keep fighting for honor!")
                

        elif userInput == "a":
            exert_damage(hero, monster)
            print(monster)
            if monster.get_health() <= 0:
                record = Record(monster)
                print("You win!")
                break
            damage = monster.get_damage()
            hero.subtract_health(damage)
            print("Your current info: " + hero.__str__())
#            print(hero)
            if hero.get_health() <= 0:
                hero.subtract_level()
                hero.set_health(50)
                print("Your info after 1 death: " + hero.__str__()) 
                if hero.get_level() == 0:
                    print("You are dead! Game over!")
                    break
        else:
            hero.subtract_health(5)
            if hero.get_health() > 0:
                print("enter a valid letter")
                print(hero)
            else:
                if hero.get_level() > 1:
                    hero.set_health(50)
                    hero.subtract_level()
                    print("Read game report again!")
                else:
                    hero.subtract_level()
                    print("You are dead! Game over")
                    break
    return record
#print(fightBoss(hero, monster))


def chooseMonster(n):
    """
    choose a easyMonster(object)
    
    """
    allMonsters = monsterList()
    try:
        monster = allMonsters[n]
        return monster
    except IndexError:
        return chooseMonster(n % 5)   

#print(chooseMonster(6))

def fightEasyMonster(hero):
    """
    fight between esayMonster and hero(object)
    
    """
    record = None
    n = random.randint(0, 100)
    info = chooseMonster(n)
    monster = easyMonster(info[0], int(info[1]), int(info[2]), \
                          int(info[3]), int(info[4]), hero)
    while True:
        userInput = input("enter 'a' to attack: ")
        if userInput == "a":
            exert_damage(hero, monster)
            print(monster)
            if monster.get_health() <= 0:
                record = Record(monster)
                hero.add_exp(monster.get_experience())
                hero.add_level()
                print("You win!")
                break
            hero.subtract_health(monster.get_damage())
            print("Your current info: " + hero.__str__())
#            print(hero)
            if hero.get_health() <= 0:
                hero.subtract_level()
                hero.set_health(50)
                print("Your info after 1 death: " + hero.__str__())
                if hero.get_level() == 0:
                    print("You are dead! Game over")
                    break
        else:
            hero.subtract_health(5)
            if hero.get_health() > 0:
                print("enter a valid letter")
                print(hero)
            else:
                if hero.get_level() > 1:
                    hero.set_health(50)
                    hero.subtract_level()
                    print("Read game report again!")
                else:
                    hero.subtract_level()
                    print("You are dead! Game over")
                    break
    return record
#print(fightEasyMonster(hero))
#print(hero.get_experience())
#print(hero.get_level())

def Direction(hero):
    """
    User chooses direction
    
    """
    userInput = input("enter 'k' to keep going or enter 'r' to rest: ")
    if userInput == "r":
        hero.add_health(20)
    elif userInput == "k":
        pass
    else:
        print("Your health is deducted due to stupid mistake!")
        hero.subtract_health(5)


def Record(monster):
    """
    Record the easyMonsters you killed in the whole game
    
    """
    if monster.get_name() not in MonstersKilled:
        MonstersKilled[monster.get_name()] = 1
    else:
        MonstersKilled[monster.get_name()] += 1
    return MonstersKilled


userInput = input("come up with your hero's name: ")
hero = character(userInput)
print("Please look at your hero's original property")
print(hero)
MonstersKilled = {}
count = 2
while count > 0 and hero.get_level() >= 1:
    health = hero.get_health()
    diff = random.randint(0, 2)
    bossHealth = health + diff
    Boss = monster("Boss", bossHealth, hero)
    x = random.randint(0, 100)
    if x % 2 == 0:
        print("An easyMonster found you!")
        record = fightEasyMonster(hero)
    if x % 2 == 1:
        Direction(hero)
        print("A Boss found you!")
        record = fightBoss(hero, Boss)
        count -= 1
f = open("MonstersKilled.txt", "w+")
f.write("Monsters you killed in the game" + "\n")
if record is not None:
    for keys in record:
        f.write(keys + " killed " + str(record[keys]) + " times." + "\n")
f.close()
        
        
    
    

    
    

 
    
    
    
    