import pandas as pd


def extract_data(file_path):
    """
    Reads a CSV file and returns a Pandas DataFrame.
    """

    try:
        df = pd.read_csv(file_path)

        print("=" * 50)
        print("EXTRACT PHASE")
        print("=" * 50)
        print(f"File Loaded Successfully")
        print(f"Rows    : {df.shape[0]}")
        print(f"Columns : {df.shape[1]}")

        return df

    except FileNotFoundError:
        print(f"ERROR: File not found -> {file_path}")
        return None

    except pd.errors.EmptyDataError:
        print("ERROR: CSV file is empty.")
        return None

    except Exception as e:
        print(f"Unexpected Error: {e}")
        return None