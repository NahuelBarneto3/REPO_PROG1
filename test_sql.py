from sql import *


create_table()


sqlConnect = sqlite3.connect("bd_jueguito.db")
sql_insert_query = """Select * FROM players """
sqlConnect.execute(sql_insert_query)
sqlConnect.commit()
print(retrieve_info())




