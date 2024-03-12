-- This script lists all rows of the table first_table from the specified database
-- Use a session variable to store the database name
SET @db_name := '{{DATABASE_NAME}}';

-- Use the stored database name
USE @db_name;

-- Select all fields from the first_table
SELECT * FROM first_table;
