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
        scdb =  pickle.load(fH)
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
            if len(parse) != 4:
                print("Enter 'add name age score")
            else:
                record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
                scdb += [record]

        elif parse[0] == 'del':
            if len(parse) != 2:
                print("Enter 'del name'")
            else:
                for p in scdb:
                    if p['Name'] == parse[1]:
                        scdb.remove(p)

        elif parse[0] == 'show':
            sortKey ='Name' if len(parse) == 1 else parse[1]
            if sortKey in {'Name', 'Age', 'Score'}:
                showScoreDB(scdb, sortKey)
            else:
                print("Check sortkey")

        elif parse[0] == 'quit':
            break

        elif parse[0] == 'find':
            if len(parse) != 2:
                print("Enter 'find name'")
            else:
                for p in scdb:
                    if p['Name'] == parse[1]:
                        for i in p:
                            print(i + "=" + p[i], end=' ')
                        print()

        elif parse[0] == 'inc':
            if len(parse) != 3:
                print("Enter 'inc name amount'")
            else:
                for p in scdb:
                    if p['Name'] == parse[1]:
                        p['Score'] = str(int(p['Score']) + int(parse[2]))

        else:
            print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + p[attr], end=' ')
        print()


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
