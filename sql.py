import sqlite3

def create_table():
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

def add_puntuacion(nombre,vidas,score, time):
    with sqlite3.connect("bd_jueguito.db") as conexion:
        try:
            conexion.execute("insert into players(nombre,vidas,score,tiempo) values (?,?,?,?)",(nombre,vidas,score,time))
        except sqlite3.OperationalError as error:
            print("Error ",error)

def retrieve_info():
    with sqlite3.connect("bd_jueguito.db") as conexion:
        cursor= conexion.execute('''SELECT id, nombre, vidas,score, tiempo
                                    FROM players
                                    ORDER BY score DESC
                                    LIMIT 5       
                                ''')       
        list_top_5 = []
        for fila in cursor:
            list_top_5.append(fila)
            return list_top_5