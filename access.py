import pyodbc

trackz = ['PC114221265BY','PC114221225BY','PC114221217BY','PC114221203BY']

def connect_to_access_db() -> pyodbc.Connection:
    """Устанавливает соединение с базой данных Access."""
    connection_string = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\1amper\1amper_be.accdb;')
    return pyodbc.connect(connection_string)
varsa = 'PC114221319BY'
conn =  pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\1amper\1amper_be.accdb;')
cursor = conn.cursor()
cursor.execute(f"UPDATE Zakaz SET Zakaz.zStatus = 1 WHERE [Zakaz]![zTrackNum]='*{varsa}*';")
# cursor.execute("SELECT Zakaz.zFIO FROM Zakaz WHERE (([Zakaz]![zTrackNum]='*PC114221319BY*'));")

# for row in cursor.fetchall():
    # print(row)


conn.commit()
conn.close()
#SELECT *
# FROM Zakaz
# WHERE [zTrackNum] Like '*PC114221265BY*';

# UPDATE Zakaz SET Zakaz.zStatus = 2 2 забрал
# WHERE (([Zakaz]![zTrackNum]="*PC114221265BY*"));
