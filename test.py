import mysql.connector

db = mysql.connector.connect(
  host="brettmusser.cikeys.com",
  user="brettmus_StephenBerks",
  passwd="k,4i17Xl@]HG",
  database="brettmus_COMP420_DolphinDollarsProject"
)

cursor = db.cursor()

cursor.execute("SELECT AuthenticateEmployee(1234, 'password1234')")

for i in cursor:
    for j in i:
        print(j)
