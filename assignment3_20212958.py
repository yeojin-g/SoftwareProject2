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
    while (True):
        inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split(" ")
        if parse[0] == 'add':
            try:
                record = {'Name': parse[1], 'Age': parse[2], 'Score': parse[3]}
            except:
                print("invalid syntax: you have to enter three parameters.")
            else:
                if (record['Age'].isdigit() and record['Score'].isdigit()):
                    scdb += [record]
                else:
                    print("You have to input number on Age:# or Score:#")
        elif parse[0] == 'del':
            if (len(parse) != 2):
                print("invalid syntax: you have to enter one parameters.")
                continue
            deletePersonData(scdb, parse[1])
        elif parse[0] == 'show':
            if (len(parse) != 1):
                print("Command 'show' have no parameters.")
                continue
            sortKey = 'Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb, sortKey)
        elif parse[0] == 'find':
            if(len(parse) != 2):
                print("invalid syntax: you have to enter one parameters.")
                continue
            findPersonByName(scdb, parse[1])
        elif parse[0] == 'inc':
            if (len(parse) != 3):
                print("invalid syntax: you have to enter two parameters.")
                continue
            elif(parse[2].isdigit()):
                addScore(scdb, parse[1], parse[2])
            else:
                print("You have to enter integer in second parameter.")
        elif parse[0] == 'quit':
            if (len(parse) != 1):
                print("Command 'quit' have no parameters.")
                continue
            break
        else:
            print("Invalid command: " + parse[0])


def deletePersonData(scdb, name):
    for p in scdb:
        if p['Name'] == name:
            scdb.remove(p)
            if (deletePersonData(scdb, name)):
                return True
    return True


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + p[attr], end=' ')
        print()


def findPersonByName(scdb, name):
    for p in scdb:
        if (p['Name'] == name):
            for attr in sorted(p):
                print(attr + "=" + p[attr], end=' ')
            print()
            return
    print("There is no person named " + name)


def addScore(scdb, name, amount):
    for p in scdb:
        if (p['Name'] == name):
            p['Score'] = str(int(p['Score']) + int(amount))
            return
    print("There is no person named " + name)


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
