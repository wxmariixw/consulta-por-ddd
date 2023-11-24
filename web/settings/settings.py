import psycopg2


db_config = {
    'dbname': 'grandfinale',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'port': '5432'
}

conn = psycopg2.connect(**db_config)