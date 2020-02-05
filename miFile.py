import mysql.connector

conexion=mysql.connector.connect(user="root", password="jovi1Fonso",
                                 database="world_x")
cursor=conexion.cursor()
pais="\'"+input("Ingrese el Pais: ")+"\'"

query="SELECT * from city WHERE city.CountryCode LIKE {} ".format(pais)
print(query)

cursor.execute(query)

for Name in cursor:
    for item in Name:
        print(item)
    print()
    