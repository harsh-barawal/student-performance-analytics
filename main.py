"""
main.py
Student Performance Analytics System
Runs the complete analysis and displays the final output.
"""

import numpy as np
import pandas as pd
from functions import (SUBJECTS, PASS_MARK, load_data, process_students,
                       overall_performance, subject_analysis, top_performers)

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 20)


def print_heading(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


# ---------------- Step 2: Read the data ----------------
students = load_data("students.csv")

print_heading("1. DATASET OVERVIEW")
print("Number of records :", students.shape[0])
print("Number of columns :", students.shape[1])
print("Columns           :", list(students.columns))
print("\nFirst 5 records:")
print(students.head())
print("\nBasic information:")
students.info()

# ---------------- Step 3: Process the data ----------------
result = process_students(students)

print_heading("2. STUDENT RESULT SHEET")
print(result[["Student_ID", "Name", "Department", "Total", "Average",
              "Grade", "Result", "Attendance"]].to_string(index=False))

# ---------------- Step 4: Perform analysis ----------------
best, worst, class_average = overall_performance(result)

print_heading("3. OVERALL PERFORMANCE")
print(f"Highest average : {best['Name']} ({best['Average']})")
print(f"Lowest average  : {worst['Name']} ({worst['Average']})")
print(f"Class average   : {class_average}")
print(f"Average attendance : {round(float(np.mean(result['Attendance'])), 2)}%")

print_heading("4. GRADE DISTRIBUTION")
grade_counts = result["Grade"].value_counts()
for grade in ["A+", "A", "B", "C", "D", "F"]:
    count = grade_counts.get(grade, 0)
    print(f"Grade {grade:<2} : {count} student(s)")

print_heading("5. PASS / FAIL STATISTICS")
total_students = len(result)
passed = int((result["Result"] == "Pass").sum())
failed = total_students - passed
print(f"Rule (pass)   : at least {PASS_MARK} marks in every subject")
print(f"Total students: {total_students}")
print(f"Passed        : {passed}")
print(f"Failed        : {failed}")
print(f"Pass percent  : {round(passed / total_students * 100, 2)}%")
print("\nFailed students:")
print(result[result["Result"] == "Fail"][["Student_ID", "Name", "Department",
                                          "Average"]].to_string(index=False))

print_heading("6. SUBJECT-WISE PERFORMANCE")
subject_table = subject_analysis(result)
print(subject_table.to_string(index=False))

print_heading("7. TOP 5 PERFORMING STUDENTS")
top = top_performers(result, 5)
rank = 1
for index, row in top.iterrows():
    print(f"Rank {rank}: {row['Name']:<16} {row['Department']:<11} "
          f"Total = {row['Total']}  Average = {row['Average']}  Grade = {row['Grade']}")
    rank += 1

# ---------------- Final answers ----------------
best_subject = subject_table.loc[subject_table["Average"].idxmax()]
weak_subject = subject_table.loc[subject_table["Average"].idxmin()]

print_heading("8. FINAL SUMMARY (ANSWERS)")
print(f"Student with highest average : {best['Name']} ({best['Average']})")
print(f"Subject with best average    : {best_subject['Subject']} ({best_subject['Average']})")
print(f"Subject with lowest average  : {weak_subject['Subject']} ({weak_subject['Average']})")
print(f"Students passed              : {passed} out of {total_students}")
print(f"Overall class average        : {class_average}")
