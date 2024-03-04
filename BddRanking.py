import pandas as pd
from sqlalchemy import create_engine

def integrate_csv_to_mysql(csv_file, mysql_username, mysql_password, mysql_host, mysql_database, table_name):

    engine = create_engine(f'mysql+pymysql://{mysql_username}:{mysql_password}@{mysql_host}/{mysql_database}')

    df = pd.read_csv(csv_file)

    df.to_sql(table_name, engine, if_exists='replace', index=False)

    df.to_sql(table_name, con=engine, if_exists='append', index=False)

    print("Les données ont été intégrées dans la base de données MySQL.")

if __name__ == "__main__":
    csv_file = 'ranking.csv'
    mysql_username = 'root'
    mysql_password = ''  # Remplacez par votre mot de passe MySQL
    mysql_host = 'localhost'
    mysql_database = 'testscrapping'
    table_name = 'ranking'

    integrate_csv_to_mysql(csv_file, mysql_username, mysql_password, mysql_host, mysql_database, table_name)
