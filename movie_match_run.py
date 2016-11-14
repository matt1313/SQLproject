import psycopg2
import csv
conn = psycopg2.connect("dbname=movie_match user=mattjoyce host=/tmp/")

cur = conn.cursor()

table_info = ("""CREATE TABLE IF NOT EXISTS Movies (id serial PRIMARY KEY,
Title varchar(50), ReleaseYear int(4), Genre varchar(15),
Director varchar(50), Budget int(9), Gross int(9));""")

cur.execute(table_info)


conn.commit()

cur.close()
conn.close()
