import sqlite3

connection = sqlite3.connect("/Users/luchicla/Downloads/Chinook_Sqlite.sqlite")
cursor = connection.cursor()

raw_results = cursor.execute("select * from Artist")
results = [r for r in raw_results]
import sys 
print(sys.getsizeof(results))

# print(results[0])
# print(results[0][1])

# acdc_albums = cursor.execute("""select al.Title, ar.Name from Album as al
# join Artist as ar on ar.ArtistId = al.ArtistId where ar.Name like 'AC/%'""")
# print(list(acdc_albums))

# cursor.execute("insert into Artist values (10002, 'Sample artist')")
# cursor.execute("insert into Artist values (10001, 'Sample artist 2')")
# connection.commit()
