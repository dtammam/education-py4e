'''
Single Table CRUD

    - Create, insert another row into the table
    - Retrieve, retrieves a group of records, you can either retrieve all the records or a subset of the records 
    - Update, allows the updating of a field with a where clause
    - Delete, delete a row in a table based on a selection criteria
'''
##### Create a table, set our contract
# CREATE TABLE Users (
# 	name VARCHAR(128),
# 	email VARCHAR(128)
# )

##### SQL: Create
# Insert another row into the table
# INSERT INTO Users (name, email) VALUES ('Kristin', 'kf@umich.edu')

##### SQL: Delete
# Delete a row in a table based on a selection criteria
# DELETE FROM Users WHERE email='fred@umich.edu'

##### SQL: Update
# Allows the updating of a field with a where clause
# UPDATE Users SET name='Charles' WHERE email='csev@umich.edu'

##### SQL: Retrieving Records
# The select statement retrieves a group of records, you can either retrieve all the records or a subset of the records with a WHERE clause
# SELECT * FROM Users
# SELECT * FROM Users WHERE email='csev@umich.edu'

##### SQL: Sorting with ORDER BY
# You can add an ORDER BY clause to SELECT statements to get the results sorted in ascending or descending order
# SELECT * FROM Users ORDER BY email
# SELECT * FROM Users ORDER BY name

##### SQL Summary
# INSERT INTO Users (name, email) VALUES ('Kristin', 'kf@umich.edu')
# DELETE FROM Users WHERE email='ted@umich.edu'
# UPDATE Users SET name="Charles" WHERE email='csev@umich.edu'
# SELECT * FROM Users
# SELECT * FROM Users WHERE email='csev@umich.edu'
# SELECT * FROM Users ORDER BY email