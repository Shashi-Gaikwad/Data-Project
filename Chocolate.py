import mysql.connector

cnx = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='awesome chocolates')
cursor = cnx.cursor()
if cnx:
    print('connection sucess')

query = ("select Geo, Region, GeoID from geo;")
cursor.execute(query)

for(Geo, Region, GeoID) in cursor:
     print ("{}, {},{} ".format ( Geo, Region, GeoID
    ))









cursor.close()

cnx.close()
