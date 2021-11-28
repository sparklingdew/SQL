/* Which artists compose their own songs? */
SELECT ar.name as artist
FROM ((tracks t 
INNER JOIN albums al 
on t.albumid=al.albumid)
INNER JOIN artists ar
on al.artistid=ar.artistid)
WHERE INSTR(t.composer,ar.name)>0
GROUP BY artist
ORDER BY artist ASC