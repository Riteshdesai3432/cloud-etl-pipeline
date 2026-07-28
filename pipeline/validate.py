import pandas as pd

def validate_data(df):
    """
    Validate the dataset and return a dictionary
    containing all validation results.
    """

    report = {}

    report["Total Rows"] = len(df)

    report["Missing Department"] = df["Department"].isnull().sum()

    report["Duplicate EmployeeNumber"] = (
        df["EmployeeNumber"].duplicated().sum()
     )

    report["Duplicate Rows"] = df.duplicated().sum()

    report["Neagative MonthlyIncome"] = (
        df["MonthlyIncome"] < 0
    ).sum()

    report["Invalid Gender"] = (
        ~df["Gender"].isin(["Male","Female"])
    ).sum()

    report["Invalid BusinessTravel"] = (
        ~df["BusinessTravel"].isin(
            [
                "Travel_Rarely",
                "Travel_Frequently",
                "Non-Travel",
            ]
        )
    ).sum()

    report["Invalid Attrition"] = (
        ~df["Attrition"].isin(["Yes", "No"])
    ).sum()

    report["Invalid EmployeeCount"] = (
            df["EmployeeCount"] != 1
    ).sum()

    report["Invalid StandardHours"] = (
            df["StandardHours"] != 80
    ).sum()

    report["Invalid Age"] = (
            (df["Age"] < 18) | (df["Age"] > 60)
    ).sum()

    return report