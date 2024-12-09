import psycopg2

def get_db_connection():
    
    conn = psycopg2.connect(
        database="fastapi",      
        user="postgres",         
        password="admin@123", 
        host="localhost",        
        port="5432" 
    )
    return conn