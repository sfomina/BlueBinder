import sqlite3

f = "discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

peepsCreate = "CREATE TABLE peeps_avg (id INTEGER, avg DECIMAL);"

def findAvg(arr):
    sum1 = 0
    numValues = 0
    for value in arr:
        sum1 += value
        numValues += 1
    return (sum1 * 1.0)/numValues
    
    


def dictAvg():
    tableGrades =  c.execute("SELECT students.id,mark FROM students,courses WHERE students.id = courses.id;")
    dict = {} # keys are names and values are arrays of grades
    for row in tableGrades:
        if not(dict.has_key(row[0])):
            dict[row[0]] = [row[1]]
        else:
            dict[row[0]].append(row[1])
    #print dict


    for key in dict:
        dict[key] = findAvg(dict[key])

    return dict


def display(d):
    arrNames = []
    for key in d:
        name = c.execute("SELECT name FROM students WHERE students.id =" + str(key) + ";")
        for x in name:
            print x[0] + ": "
        print "id = " + str(key) + ", " + "GPA = " +  str(d[key]) + "\n"


def insertIntoTable(d):
    for key in d :
        print key
        print d[key]
        c.execute( 'INSERT INTO peeps_avg VALUES ("%d", %d)' %(key,d[key]) + ";")




def updateAvg(newAvg,stuid):
    c.execute("UPDATE peeps_avg SET avg =" + str(newAvg) + " WHERE id =" + str(stuid) + ";")

def addRowsCourses (code,mark,id):
    c.execute("INSERT INTO courses VALUES ('%s', %d, %d)" % (code,mark,id) + ";")

    
dictAvgs = dictAvg()
display(dictAvgs)
c.execute(peepsCreate)
insertIntoTable(dictAvgs)
updateAvg(99,1)
addRowsCourses("poetry", 100 ,3) 

db.commit()
db.close()








