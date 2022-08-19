import openpyxl
import mysql.connector

#wb=openpyxl.load_workbook("leasebook.xlsx")

#a=wb.get_sheet_names();

#print(a)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="secret",
  database="mydatabase"
)

print(mydb)
mycursor = mydb.cursor()


sql = "SELECT * FROM customers ORDER BY name"

mycursor.execute(sql)

myresult = mycursor.fetchall()
f = open("myfile.txt", "w")

for x in myresult:
  print(x)
  f.write(str(x))
  
f.close()

