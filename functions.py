"""
functions.py
Reusable calculation and processing functions for the
Student Performance Analytics System.
"""

import numpy as np
import pandas as pd

# Subject columns present in students.csv
SUBJECTS = ["Maths", "Physics", "Chemistry", "English", "Computer"]

# A student passes only if every subject mark is at least this value
PASS_MARK = 40


def load_data(file_path):
    """Read the student CSV file into a Pandas DataFrame."""
    return pd.read_csv(file_path)


def calculate_total(marks):
    """Return total marks for one student (marks is a list/array)."""
    return int(np.sum(marks))


def calculate_average(marks):
    """Return average marks for one student, rounded to 2 decimals."""
    return round(float(np.mean(marks)), 2)


def assign_grade(average):
    """
    Grading rule (based on average marks):
        90 and above  -> A+
        80 to 89.99   -> A
        70 to 79.99   -> B
        60 to 69.99   -> C
        50 to 59.99   -> D
        below 50      -> F
    """
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def check_result(marks):
    """
    Pass/Fail rule: a student is 'Pass' only if the marks in
    EVERY subject are greater than or equal to PASS_MARK (40).
    """
    if np.all(np.array(marks) >= PASS_MARK):
        return "Pass"
    return "Fail"


def process_students(df):
    """
    Loop through every student and calculate total, average,
    grade and result. Returns a new DataFrame with these columns added.
    """
    totals = []
    averages = []
    grades = []
    results = []

    for index, row in df.iterrows():
        marks = row[SUBJECTS].values.astype(int)   # NumPy array of marks
        total = calculate_total(marks)
        average = calculate_average(marks)
        totals.append(total)
        averages.append(average)
        grades.append(assign_grade(average))
        results.append(check_result(marks))

    processed = df.copy()
    processed["Total"] = totals
    processed["Average"] = averages
    processed["Grade"] = grades
    processed["Result"] = results
    return processed


def overall_performance(df):
    """Return highest, lowest and average performance of the class."""
    best = df.loc[df["Average"].idxmax()]
    worst = df.loc[df["Average"].idxmin()]
    class_average = round(float(np.mean(df["Average"])), 2)
    return best, worst, class_average


def subject_analysis(df):
    """
    Loop through each subject and calculate average, highest,
    lowest marks and number of students who scored >= PASS_MARK.
    """
    rows = []
    for subject in SUBJECTS:
        marks = df[subject].values
        rows.append({
            "Subject": subject,
            "Average": round(float(np.mean(marks)), 2),
            "Highest": int(np.max(marks)),
            "Lowest": int(np.min(marks)),
            "Passed": int(np.sum(marks >= PASS_MARK)),
        })
    return pd.DataFrame(rows)


def top_performers(df, count=5):
    """Return the top 'count' students sorted by average marks."""
    return df.sort_values(by="Average", ascending=False).head(count)
