import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="testscrapping"
)
cursor = connection.cursor()

cursor.execute("SELECT SUM(Price) FROM books")
total_price = cursor.fetchone()[0]
print("Somme des prix de tous les livres:", total_price)


cursor.execute("SELECT COUNT(*) FROM books")
total_books = cursor.fetchone()[0]
print("Nombre total de livres:", total_books)

cursor.execute("SELECT MIN(Price) FROM books")
min_price = cursor.fetchone()[0]
print("Prix minimum parmi tous les livres:", min_price)


cursor.execute("SELECT MAX(Price) FROM books")
max_price = cursor.fetchone()[0]
print("Prix maximum parmi tous les livres:", max_price)


cursor.execute("SELECT AVG(Price) FROM books")
average_price = cursor.fetchone()[0]
print("Prix moyen des livres:", average_price)

cursor.close()
connection.close()
