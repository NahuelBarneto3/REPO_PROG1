import sqlite3

class Sql():
    def __init__(self) -> None:
        with sqlite3.connect("bd_jueguito.db") as conexion:
            try:
                sentence = ''' create table players
                                (
                                    id integer primary key autoincrement,
                                    nombre text,
                                    vidas integer,
                                    score integer,
                                    tiempo integer
                                ) 
                            '''
                conexion.execute(sentence)
                print("table")
            except sqlite3.OperationalError:
                print("la table ya ta")

    def add_puntuacion(self,nombre,vidas,score, time):
        with sqlite3.connect("bd_jueguito.db") as conexion:
            if self.modify_players_score(nombre) != []:
                try:
                    conexion.execute("UPDATE players SET vidas=?,score=?,tiempo=? WHERE nombre=?",(vidas,score,time,nombre))
                    conexion.commit()

                except sqlite3.OperationalError as error:
                    print("Error: ",error)       
            else:
                try:
                    conexion.execute("insert into players(nombre,vidas,score,tiempo) values (?,?,?,?)",(nombre,vidas,score,time))
                    conexion.commit()
                    
                except sqlite3.OperationalError as error:
                    print("Error: ",error) 

    def modify_players_score(self,nombre):
        nombre = nombre
        with sqlite3.connect("bd_jueguito.db") as conexion:
            sentence = "SELECT * FROM players WHERE nombre=?"
            cursor = conexion.execute(sentence, (nombre,))
        return cursor.fetchall()

    def select(self):
        with sqlite3.connect("bd_jueguito.db") as conexion:
            cursor=conexion.execute("SELECT * FROM players")
            for fila in cursor:
                print(fila)

    def delete(self,id):
        id = id
        with sqlite3.connect("bd_jueguito.db") as conexion:
            sentence = "DELETE FROM players WHERE id=?"
            cursor=conexion.execute(sentence,(id,))
        return cursor.fetchall()
        


