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
            record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
            scdb += [record]

        elif parse[0] == 'del':
            if len(parse) == 2:
                for p in scdb:
                    if p['Name'] == parse[1]:
                        scdb.remove(p)
            else:
                print('Please enter name')

        elif parse[0] == 'show':
            sortKey ='Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb, sortKey)

        elif parse[0] == 'find':
            if len(parse) == 2:
                for p in scdb:
                    if p['Name'] == parse[1]:
                        for i in p:
                            print(i + "=" + p[i], end=' ')
                        print()
            else:
                print("Please enter name")

        elif parse[0] == 'inc':
            if len(parse) == 3:
                for p in scdb:
                    if p['Name'] == parse[1]:
                        p['Score'] = str(int(p['Score'])+int(parse[2]))
            else:
                print('Please enter name, amount')

        elif parse[0] == 'quit':
            break

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
