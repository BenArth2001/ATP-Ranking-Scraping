import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root@localhost/testscrapping')

df = pd.read_csv('books.csv')

table_name = 'books'

df.to_sql(table_name, con=engine, if_exists='append', index=False)

print("Les données ont été intégrées dans la base de données MySQL.")
