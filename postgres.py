import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()



pghost=os.environ["PGHOST"]
pguser=os.environ["PGUSER"]
pgpassword=os.environ["PGPASSWORD"]
def get_connection():
    conn = psycopg2.connect(
    host=pghost,
    database="postgres",
    user=pguser,
    password=pgpassword)
    return conn

# print(host)
# create_user("")