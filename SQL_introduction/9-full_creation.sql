-- This is a script that creates a table second_table in the database hbtn_0c_0 in my MySQL server and add multiples rows.
CREATE TABLE IF NOT EXISTS hbtn_0c_0.second_table (
    id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    score INT NOT NULL
);

INSERT INTO hbtn_0c_0.second_table (id, name, score) 
VALUES  (1, "John", 10),
        (2, "Alex", 3),
        (3, "Bob", 14),
        (4, "George", 8);
