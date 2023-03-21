import sqlite3

conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Tracks')
cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', ('Wonderstruck', 15))
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', ('Your Way', 20))
conn.commit()

print('Tracks: ')
cur.execute('SELECT title FROM Tracks WHERE title=?', ('Your Wa', ))
x = 'lauwgf'
for row in cur:
    print(row)
    x = row
    break
print(x[0])
cur.execute('DELETE FROM Tracks WHERE plays < 100')

conn.commit()
conn.close()
