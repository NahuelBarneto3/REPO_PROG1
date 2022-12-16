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
                                    tiempo integer,
                                    lvl integer
                                ) 
                            '''
                            
                conexion.execute(sentence)
                print("table")
            except sqlite3.OperationalError:
                print("la table ya ta")

def add_puntuacion(nombre,vidas,score, time,lvl):
    #with sqlite3.connect("bd_jueguito.db") as conexion:
        try:
            sqlConnect = sqlite3.connect("bd_jueguito.db")
            cursor = sqlConnect.cursor()
            sql_insert_query = """INSERT INTO players
            (nombre,vidas,score,tiempo,lvl) VALUES (?,?,?,?,?)"""

            cursor.execute(sql_insert_query,(nombre,vidas,score,time,lvl))
            sqlConnect.commit()
            cursor.close()
            print(retrieve_info())
            # conexion.execute('''insert into players(nombre,vidas,score,tiempo) values (?,?,?,?)''',(nombre,vidas,score,time))
            # conexion.commit()
            # print(nombre,vidas,score,time)
            # print(retrieve_info())
        except sqlite3.OperationalError as error:
            print("Error ",error)

def retrieve_info():
    with sqlite3.connect("bd_jueguito.db") as conexion:
        sql_select = "SELECT * FROM players ORDER BY score DESC LIMIT 5"
        cur = conexion.cursor()
        res = cur.execute(sql_select)
        print("res",res.fetchall())
        return cur.execute(sql_select).fetchall()        
        # cursor= conexion.execute('''SELECT * FROM players''')
        # list_top_5 = []
        # for fila in cursor:
        #     list_top_5.append(fila)
        #     return list_top_5