import mysql.connector
from mysql.connector import cursor

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='salasana',
         autocommit=True,
         collation='utf8mb4_general_ci'
         )



def fetch_airport_by_icao(code):
    sql = (f"SELECT name, municipality "
           f"FROM airport WHERE ident = '{code}'")
    #print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result_now = cursor.fetchone()
    print(result_now)
    return result_now
airport = fetch_airport_by_icao("ZYTH")
if airport:
    print(f"Haettu lentokenttä: {airport[0]}, {airport[1]}.")
else:
    print("lentokenttä ei löydetty annetulla koodilla")



def add_airport(icao,name,municipality):
    sql = (f"INSERT INTO airport (id,ident,name, municipality) "
           f"Values (999,'{icao}', 'oma kenttä', 'espoo')")
    cursor = connection.cursor()
    cursor.execute(sql)


icao = input("anna uusi ICAO: ")
name = input("anna uuden kentän nimi: ")
municipality = input("ja paikkakunta:")
add_airport(icao,name,municipality)






