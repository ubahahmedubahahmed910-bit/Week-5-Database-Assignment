DROP INDEX IdxPhone ON customers;
CREATE USER 'bob'@'localhost' IDENTIFIED BY 'S$cu3r3!';

ALTER USER 'bob'@'localhost' IDENTIFIED BY 'P$55!23';



-- Question 1: Drop the IdxPhone index from the customers table
DROP INDEX IdxPhone ON customers;

-- Question 2: Create user bob restricted to localhost
CREATE USER 'bob'@'localhost' IDENTIFIED BY 'S$cu3r3!';

-- Question 3: Grant INSERT privilege on salesDB to bob
GRANT INSERT ON salesDB.* TO 'bob'@'localhost';

-- Question 4: Change password for user bob
ALTER USER 'bob'@'localhost' IDENTIFIED BY 'P$55!23';