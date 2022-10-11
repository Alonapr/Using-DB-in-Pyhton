import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password,
            database = db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection
connection = create_connection("127.0.0.1", "root", "2153fktyf", "dance studio")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

insert_clients = """
INSERT INTO
  `clients` (`pass`, `name`, `surname`, `date_of_birth`, `phone_number`, `regular_client`, `active_discount`)
VALUES
  (5, 'James', 'Smith', '2000-03-21', '0983457236', 'false', 1);
"""
#execute_query(connection, insert_clients)


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

select_levels_teachers = """
SELECT l.name_level AS level, COUNT(t.id_teacher) AS teachers
FROM levels l
INNER JOIN teachers t
ON t.level = l.id_level
GROUP BY t.level"""
levels_teachers = execute_read_query(connection, select_levels_teachers)
#for i in levels_teachers:
#    print(i)

select_clients_groups = """
SELECT c.name AS client_name, c.surname AS client_surname,
((YEAR(CURRENT_DATE) - YEAR(c.date_of_birth)) -                             
(DATE_FORMAT(CURRENT_DATE, '%m%d') < DATE_FORMAT(c.date_of_birth, '%m%d'))) AS client_age,
t.name AS teacher, s.style, g.age_restrictions, g.timetable, g.time
FROM groups g
INNER JOIN clients c
ON c.id_client = g.client
INNER JOIN teachers t
ON g.techer = t.id_teacher
INNER JOIN styles s
ON g.style = s.id_style
WHERE g.age_restrictions LIKE "1%8"
ORDER BY c.name"""
clients_groups = execute_read_query(connection, select_clients_groups)
#for i in clients_groups:
#    print(i)


update_client_name ="""
UPDATE
  clients
SET
  name = "Natala"
WHERE
  id_client = 5
"""
#execute_query(connection,  update_client_name)

delete_client = "DELETE FROM clients WHERE id_client = 20"
execute_query(connection, delete_client)