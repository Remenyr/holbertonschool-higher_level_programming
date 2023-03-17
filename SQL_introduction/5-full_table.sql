-- This is a script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.
SELECT column_name, column_type
FROM information_schema.columns
WHERE table_name = 'first_table'
AND table_schema = 'hbtn_0c_0';