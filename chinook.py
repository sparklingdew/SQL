import sqlite3
import numpy as np
import pandas as pd

print('Which artists compose their own songs?\n')

# Query using sqlite
conn = sqlite3.connect('chinook.db')
cur = conn.cursor()

cur.execute('''
SELECT ar.name as artist
FROM ((tracks t 
INNER JOIN albums al 
on t.albumid=al.albumid)
INNER JOIN artists ar
on al.artistid=ar.artistid)
WHERE INSTR(t.composer,ar.name)>0
GROUP BY artist
ORDER BY artist ASC ''')

artists= cur.fetchall()
print('Query using Sqlite: ')
print(np.array(artists).flatten())
cur.close()


# Query using pandas+sqlite
curr = sqlite3.connect("chinook.db")
df = pd.read_sql_query('''
SELECT ar.name as artist
FROM ((tracks t 
INNER JOIN albums al 
on t.albumid=al.albumid)
INNER JOIN artists ar
on al.artistid=ar.artistid)
WHERE INSTR(t.composer,ar.name)>0
GROUP BY artist
ORDER BY artist ASC ''', curr)

print('Query using Pandas + Sqlite: ')
print(df)
curr.close()