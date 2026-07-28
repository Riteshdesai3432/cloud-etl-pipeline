from sqlalchemy import create_engine
from config.config import DB_CONFIG

def load_data(df):

    """
       Load cleaned employee data into PostgreSQL.
    """

    print("\n" + "=" * 50)
    print("LOAD PHASE")
    print("=" * 50)

    try:
        connection_string = (
            f"postgresql+psycopg2://"
            f"{DB_CONFIG['user']}:"
            f"{DB_CONFIG['password']}@"
            f"{DB_CONFIG['host']}:"
            f"{DB_CONFIG['port']}/"
            f"{DB_CONFIG['database']}"
        )

        engine = create_engine(connection_string)

        df.to_sql(
            name= "employees_clean",
            con=engine,
            if_exists="replace",
            index=False
        )

        print("Data loaded successfully into PostgreSQL.")
        print(f"Rows Loaded:{len(df)}")

    except Exception as e:
        print("Load Failed")
        print(e)