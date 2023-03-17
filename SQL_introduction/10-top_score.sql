-- This is  a script that lists all records of the table second_table of the database hbtn_0c_0 in my MySQL server.
-- results are displayed both the score and the name (in this order) ordered by score (top first)
SELECT score, name FROM second_table ORDER BY score DESC;