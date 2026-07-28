from pipeline.extract import extract_data
from pipeline.validate import validate_data
from pipeline.transform import transform_data
from pipeline.load import load_data
from pipeline.logger import write_log
from pathlib import Path


def main():
    print("=" * 60)
    print("EMPLOYEE DATA ETL PIPELINE")
    print("=" * 60)

    # CSV File Path
    BASE_DIR = Path(__file__).resolve().parent.parent

    RAW_DATA = BASE_DIR / "data" / "raw" / "employees_large.csv"
    PROCESSED_DATA = BASE_DIR / "data" / "processed" / "employees_clean.csv"

    # ------------------------
    # EXTRACT
    # ------------------------
    df = extract_data(RAW_DATA)

    if df is None:
        write_log("ETL Failed - Could not extract data.")
        return

    write_log("Extract Phase Completed Successfully")

    # ------------------------
    # VALIDATE
    # ------------------------
    report = validate_data(df)

    print("\nValidation Report")
    print("-" * 40)

    for key, value in report.items():
        print(f"{key:<30}: {value}")

    write_log("Validation Phase Completed Successfully")

    # ------------------------
    # TRANSFORM
    # ------------------------
    cleaned_df = transform_data(df)

    cleaned_df.to_csv(PROCESSED_DATA, index=False)

    print("\nCleaned CSV Saved Successfully")

    write_log("Transform Phase Completed Successfully")

    # ------------------------
    # LOAD
    # ------------------------
    load_data(cleaned_df)

    write_log(f"Rows Loaded: {len(cleaned_df)}")

    print("\n" + "=" * 60)
    print("ETL PIPELINE COMPLETED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    main()