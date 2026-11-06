from data.database import get_db_connection
conn = get_db_connection()
conn.sql("SELECT * FROM media_logs").show()
conn.close()
