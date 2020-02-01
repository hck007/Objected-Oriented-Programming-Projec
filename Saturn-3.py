fileToOpen = open("monsters.txt", "r")
monsters = fileToOpen.readlines()


def chooseMonster(n):
    """
    """
    return monsters[n].replace('\n','').replace(' ', '').split(',')

def monsterList():
    monsterList = []
    for x in range(0, len(monsters)):
        monsterList.append(chooseMonster(x))
    return (monsterList)

fileToOpen.close()

