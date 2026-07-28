import pandas as pd

def transform_data(df):

    """
       Clean and transform the employee dataset.
    """

    print("\n" + "=" * 50)
    print("TRANSFORM PHASE")
    print("=" * 50)

    # 1. Fill Missing Department

    df["Department"] = df["Department"].fillna("Unknown")

    # 2. Remove Duplicate EmployeeNumber

    before = len(df)

    df = df.drop_duplicates(subset="EmployeeNumber",keep="first")

    removed_duplicates = before - len(df)

    # 3. Fix Negative MonthlyIncome

    df["MonthlyIncome"] = df["MonthlyIncome"].abs()

    # 4. Standardize Gender

    df["Gender"] = (
        df["Gender"]
        .str.strip()
        .str.title()
    )

    # 5. Standardize BusinessTravel

    df["BusinessTravel"] = (
        df["BusinessTravel"]
        .str.strip()
        .str.replace({
            "travel_rarely" : "Travel_Rarely"
        })
    )

    # 6. Standardize Attrition

    df["Attrition"] = (
        df["Attrition"]
        .str.strip()
        .str.title()
    )

    # 7. Remove Invalid Age

    df = df[
        (df["Age"] >= 18)
        &
        (df["Age"] <= 60)
    ]

    # 8. Salary Category

    df["SalaryCategory"] = pd.cut(
        df["MonthlyIncome"],
        bins=[0,5000,10000,float("inf")],
        labels=["Low","medium","High"]
    )

    # 9. Experience Level

    df["ExperienceLevel"] = pd.cut(
        df["TotalWorkingYears"],
        bins=[-1, 5, 10, float("inf")],
        labels=["Junior", "Mid", "Senior"]
    )

    # 10. Bonus

    df["Bonus"] = (df["MonthlyIncome"] * 0.10).round(2)

    print(f"Removed Duplicate Employees : {removed_duplicates}")
    print(f"Rows After Cleaning         : {len(df)}")

    return df











