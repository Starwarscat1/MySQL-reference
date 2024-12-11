"""
/*
    Creating a Database
    Multi-line comment example
*/
CREATE DATABASE BookStore;

-- Selecting the Database
USE BookStore;

-- Creating a Table with various datatypes and all kinds of constraints
CREATE TABLE Books (
    BookID INT AUTO_INCREMENT PRIMARY KEY, -- PRIMARY KEY constraint
    Title VARCHAR(255) NOT NULL, -- NOT NULL constraint
    Author VARCHAR(255),
    AuthorEmail VARCHAR(100) UNIQUE, -- UNIQUE constraint
    PublishedDate DATE,
    ISBN VARCHAR(20) NOT NULL, -- Adding NOT NULL for illustration
    Price DECIMAL(10,2) CHECK (Price > 0), -- CHECK constraint on single column
    Genre ENUM('Fiction', 'Non-Fiction', 'Sci-Fi', 'Fantasy', 'Mystery', 'Educational'),
    InStock BOOLEAN DEFAULT TRUE, -- DEFAULT constraint
    PageCount INT,
    CONSTRAINT fk_Author FOREIGN KEY (Author) REFERENCES Authors(Name), -- FOREIGN KEY constraint
    CONSTRAINT chk_PageCount CHECK (PageCount > 0 AND PageCount < 5000) -- CHECK constraint for range
);

-- Inserting Data into the Table
INSERT INTO Books (Title, Author, PublishedDate, ISBN, Price, Genre, PageCount)
VALUES ('The Great Gatsby', 'F. Scott Fitzgerald', '1925-04-10', '1234567890123', 14.99, 'Fiction', 180);

/*
    Examples of all kinds of operators in comments
*/

-- Comparison operators
-- SELECT * FROM Books WHERE Price > 15; -- Greater Than
-- SELECT * FROM Books WHERE PageCount >= 500; -- Greater Than or Equal
-- SELECT * FROM Books WHERE ISBN = '1234567890123'; -- Equal
-- SELECT * FROM Books WHERE Title != 'Moby Dick'; -- Not Equal
-- SELECT * FROM Books WHERE PublishedDate < '2000-01-01'; -- Less Than
-- SELECT * FROM Books WHERE Genre <> 'Sci-Fi'; -- Not Equal (alternative syntax)
-- SELECT * FROM Books WHERE Price <= 20; -- Less Than or Equal

-- Logical operators
-- SELECT * FROM Books WHERE InStock = TRUE AND PageCount > 100; -- AND
-- SELECT * FROM Books WHERE Genre = 'Fiction' OR Genre = 'Fantasy'; -- OR
-- SELECT * FROM Books WHERE NOT (Price > 20); -- NOT

-- Other operators
-- SELECT Title, Price, Price * 1.1 AS PriceIncrease FROM Books; -- Arithmetic operator *
-- SELECT * FROM Books WHERE Genre IN ('Fiction', 'Non-Fiction'); -- IN
-- SELECT * FROM Books WHERE Genre NOT IN ('Sci-Fi'); -- NOT IN
-- SELECT * FROM Books WHERE Title LIKE 'The%'; -- LIKE
-- SELECT * FROM Books WHERE Title NOT LIKE 'War%'; -- NOT LIKE
-- SELECT * FROM Books WHERE Author IS NULL; -- IS NULL
-- SELECT * FROM Books WHERE Author IS NOT NULL; -- IS NOT NULL
-- SELECT * FROM Books WHERE Price BETWEEN 10 AND 20; -- BETWEEN ... AND ...

-- Updating Data in the Table
UPDATE Books SET Price = Price * 1.1 WHERE BookID = 1; -- Arithmetic operator example

-- Deleting a Row from the Table
DELETE FROM Books WHERE BookID = 1;

-- Altering a Table to Add a Column (Commented Out)
-- ALTER TABLE Books ADD COLUMN ReviewRating DECIMAL(3,2) DEFAULT 0;

-- Dropping a Table (Commented Out)
-- DROP TABLE Books;

-- Dropping a Database (Commented Out)
-- DROP DATABASE BookStore;

"""

import mysql.connector as sql
import os

try:

  hostName = "sql5.freemysqlhosting.net"
  my_db_name = os.getenv("DB_NAME")
  my_username = os.getenv("DB_USERNAME")
  my_password = os.getenv("DB_PASSWORD")
  connection = sql.connect(host = hostName, user = my_username, password = my_password, database = my_db_name)
  cursor = connection.cursor()
  """
  cursor.execute("SHOW TABLES")
  result = cursor.fetchall()
  for tuple in result:
    print(tuple[0])
  query = ("CREATE TABLE People ( "
     "ID INT AUTO_INCREMENT PRIMARY KEY, "
     "First_Name VARCHAR(50) NOT NULL, "
     "Last_Name VARCHAR(50), "
     "Age INT"
     ");")
  """

  isDeleteTable = False
  isCreate = False
  isInsert = False
  isShow = True

  if isDeleteTable:

    query = "DROP TABLE People;"
    cursor.execute(query)
    connection.commit()
  
  if isCreate:

    query = ("CREATE TABLE People ( "
             "ID INT AUTO_INCREMENT PRIMARY KEY, "
             "First_Name VARCHAR(50) NOT NULL, "
             "Last_Name VARCHAR(50), "
             "Age INT"
             ");")
    cursor.execute(query)
    connection.commit()
  
  if isInsert:
  
    query = ("INSERT INTO People (First_Name, Last_Name, Age) "
             "VALUES ('Tim', 'Phone', 27);")
    #print(f"query: {query}")
    cursor.execute(query)
    connection.commit()

  if isShow:

    query = "SELECT * FROM People;"
    cursor.execute(query)
    result = cursor.fetchall()
    for (id, first_name, last_name, age) in result:
      print(f"id: {id}, first_name: {first_name}, last_name: {last_name}, age: {age}")

except Exception as e:
  print(f"The following error occurred: {e}")
finally:
  try:
    cursor.close()
  except NameError as e:
    print(f"The following error occurred: {e}")
  try:
    connection.close()
  except NameError as e:
    print(f"The following error occurred: {e}")
