import sqlite3

f = "discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

peepsCreate = "CREATE TABLE peeps_avg (id INTEGER, avg DECIMAL);"

#def calcAvg():
tableGrades =  c.execute("SELECT name,mark FROM students,courses WHERE students.id = courses.id;")

#print tableGrades 
for row in tableGrades:
    print row
     
    
    
    
