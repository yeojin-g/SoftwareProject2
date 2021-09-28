import pickle

dbfilename = 'test3_4.dat'

def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb = pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()


def doScoreDB(scdb):
    while(True):
        inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split(" ")
        if parse[0] == 'add':
            record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
            scdb += [record]
        elif parse[0] == 'del':
            for p in scdb:
                if p['Name'] == parse[1]:
                    scdb.remove(p)
        elif parse[0] == 'show':
            sortKey ='Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb, sortKey)
        elif parse[0] == 'find':
            findScoreDB(scdb, parse[1])
        elif parse[0] == 'inc':
            incScoreDB(scdb, parse[1], parse[2])
        elif parse[0] == 'quit':
            break
        else:
            print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + p[attr], end=' ')
        print()

def findScoreDB(scdb, name):
    exist = False
    for p in sorted(scdb, key=lambda person: person['Name']):
        if p['Name'] == name:
            for attr in sorted(p):
                print(attr + "=" + p[attr], end=' ')
            print()
            exist = True
    if exist == False: print("Name is not exist.")

def incScoreDB(scdb, name, amount):
    exist = False
    for p in sorted(scdb, key=lambda person: person['Name']):
        if p['Name'] == name:
            p['Score'] = str(int(p['Score']) + int(amount))
            exist = True
    if exist == False: print("Name is not exist.")

scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
