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

#parse[]는 띄어쓰기를 기준으로 문장을 나눈 것.
def doScoreDB(scdb):
    while(True):
        inputstr = (input("Score DB > "))
        if (inputstr == ""): continue
        parse = inputstr.split(" ")
        while "" in parse: # 공백 입력값 리스트에서 제거 -> "add     " == "add"
            parse.remove("")
        if parse[0] == 'add':
            try:
                record = {'Name':parse[1], 'Age':int(parse[2]), 'Score':int(parse[3])}
                if (record["Age"] <= 0):  # 나이값이 1보다 작을 때
                    print("Age must be a value greater than zero.")
                    continue
                if (record["Score"] < 0):  # 점수가 0보다 작을 때
                    print("Score should be positive.")
                    continue
                scdb += [record]
            except IndexError: # 값을 다 안 입력했을 때
                print("You must enter all thing.")
            except ValueError: # 나이 혹은 점수를 숫자로 입력하지 않았을 때
                print("Age and score have to enter as a number.")
        elif parse[0] == 'del':
            try:
                if len(parse) > 2: # 여러 이름 입력했을 경우
                    print("Enter only one name.")
                    continue
                before = len(scdb)
                for p in scdb:
                    if p['Name'] == parse[1]:
                        scdb.remove(p)
                after = len(scdb)
                if before == after: print("\"%s\" is not in the list."% parse[1]) # del한 대상이 없을 경우
            except IndexError: # 이름을 입력하지 않은 경우
                print("Enter the name.")
        elif parse[0] == 'show':
            try:
                sortKey ='Name' if len(parse) == 1 else parse[1]
                showScoreDB(scdb, sortKey)
            except KeyError: #정렬키 값이 잘못되었을 경우
                print("\"%s\" is a wrong sortkey."%parse[1])
        elif parse[0] == 'find':
            findScoreDB(scdb, parse[1])
        elif parse[0] == 'inc':
            try:
                incScoreDB(scdb, parse[1], parse[2])
            except IndexError: # 값을 다 안 입력했을 때
                print("You must enter all thing.")
        elif parse[0] == 'quit':
            break
        else:
            print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + str(p[attr]), end=' ')
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
