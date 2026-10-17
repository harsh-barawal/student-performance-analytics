# 1. Project Title

## Student Performance Analytics System

| Field | Details |
|---|---|
| **Project Title** | Student Performance Analytics System |
| **Course** | Python with AI – EWB Courses |
| **Student Name** | `<Your Full Name>` |
| **Enrollment / Batch** | `<Your Enrollment No. / Batch>` |
| **Email** | `<Your Email>` |
| **Technology** | Python, NumPy, Pandas |
| **Submission Deadline** | 15 October 2026 |

---

# 2. Objective

In any college or institute, teachers hold marks of many students across many subjects. Checking totals, averages, grades, and pass/fail status by hand is slow and mistakes are easy to make. It is also hard to answer simple questions such as *"Which subject is the weakest?"* or *"Who are the top students?"* just by looking at a table of marks.

This project solves that problem. The **Student Performance Analytics System** reads student records from a CSV file, processes them using **NumPy** and **Pandas**, and automatically produces:

- Total marks and average marks of every student
- Grade of every student (based on a clearly defined grading rule)
- Pass / Fail result (based on a clearly defined condition)
- Highest, lowest and average performance of the class
- Subject-wise performance analysis
- List of top-performing students

The project is a Python **data-analysis** project and uses only the concepts covered in class: variables, data types, loops, functions, NumPy and Pandas. No machine learning is used.

---

# 3. Technologies Used

| Technology | Purpose in this project |
|---|---|
| **Python 3** | Core programming language (variables, data types, loops, conditions, functions) |
| **NumPy** | Numerical calculations: `sum`, `mean`, `max`, `min`, `all` on marks arrays |
| **Pandas** | Loading the CSV, creating the DataFrame, adding columns, sorting, filtering, `value_counts` |

No other library or tool has been used.

**How to run the project**

```bash
pip install numpy pandas
python main.py
```

---

# 4. Dataset Description

The dataset is stored in `students.csv`. It contains **20 student records** and **9 columns**. The data is a fictional but realistic set of students from five departments (CSE, ECE, IT, Mechanical and Civil), created for this project. It includes toppers, average students and two students who fail, so that the analysis shows meaningful results.

| Column | Description | Type |
|---|---|---|
| `Student_ID` | Unique ID of the student (S001 to S020) | Text |
| `Name` | Name of the student | Text |
| `Department` | CSE, ECE, IT, Mechanical or Civil | Text |
| `Maths` | Marks out of 100 | Integer |
| `Physics` | Marks out of 100 | Integer |
| `Chemistry` | Marks out of 100 | Integer |
| `English` | Marks out of 100 | Integer |
| `Computer` | Marks out of 100 | Integer |
| `Attendance` | Attendance percentage | Integer |

**Sample of the dataset**

| Student_ID | Name | Department | Maths | Physics | Chemistry | English | Computer | Attendance |
|---|---|---|---|---|---|---|---|---|
| S001 | Aarav Sharma | CSE | 88 | 92 | 85 | 78 | 95 | 94 |
| S002 | Priya Verma | CSE | 76 | 81 | 72 | 85 | 90 | 91 |
| S003 | Rohan Gupta | ECE | 65 | 58 | 62 | 70 | 68 | 82 |
| S004 | Sneha Singh | IT | 92 | 89 | 94 | 90 | 97 | 96 |
| S005 | Vikram Yadav | Mechanical | 45 | 38 | 42 | 55 | 50 | 68 |

(All 20 records are available in `students.csv`.)

---

# 5. Implementation

## 5.1 Project Structure

```
student-performance-analytics/
│
├── main.py              # Runs the project and displays the final analysis
├── functions.py         # Reusable calculation / processing functions
├── students.csv         # Student records (20 students)
├── README.md            # Project documentation (this file)
└── screenshots/         # Output screenshots used in this documentation
```

## 5.2 Step 1 – Prepare the Dataset

A CSV file `students.csv` was created with 20 student records. Each record has the Student ID, Name, Department, marks in five subjects and attendance. Marks are between 34 and 98 and attendance between 62% and 97%, which is realistic for a class.

## 5.3 Step 2 – Read the Data

The function `load_data()` uses `pd.read_csv()` to read the file into a Pandas **DataFrame**. In `main.py` the program then displays the number of records and columns, the column names, the first five rows (`head()`) and basic information (`info()`), so the dataset is checked before processing.

```python
def load_data(file_path):
    return pd.read_csv(file_path)
```

## 5.4 Step 3 – Process the Data

The main processing is done by `process_students()`. It uses a **loop** to go through each student row, converts the five subject marks into a **NumPy array**, and calls small reusable functions:

```python
for index, row in df.iterrows():
    marks = row[SUBJECTS].values.astype(int)   # NumPy array
    total = calculate_total(marks)             # np.sum
    average = calculate_average(marks)         # np.mean
    grades.append(assign_grade(average))
    results.append(check_result(marks))        # np.all
```

The calculated values are stored in lists and added to the DataFrame as new columns: `Total`, `Average`, `Grade` and `Result`.

### Grading Rule (based on average marks)

| Average Marks | Grade |
|---|---|
| 90 and above | A+ |
| 80 to 89.99 | A |
| 70 to 79.99 | B |
| 60 to 69.99 | C |
| 50 to 59.99 | D |
| Below 50 | F |

The rule is written with `if / elif / else` conditions inside the function `assign_grade()`.

### Pass / Fail Condition

A student is **Pass** only if the marks in **every subject are at least 40**. If even one subject is below 40, the student is **Fail**. This is checked with `np.all(marks >= 40)` inside `check_result()`.

## 5.5 Step 4 – Perform Analysis

The analysis answers practical questions using NumPy and Pandas operations:

| Question | How it is calculated |
|---|---|
| Which student has the highest / lowest average? | `idxmax()` and `idxmin()` on the `Average` column |
| What is the overall class average? | `np.mean()` on the `Average` column |
| How many students passed? | Counting rows where `Result == "Pass"` |
| What is the grade distribution? | `value_counts()` on the `Grade` column |
| Which subject has the best average? | Loop over subjects using `np.mean()`, `np.max()`, `np.min()` in `subject_analysis()` |
| Who are the top performers? | `sort_values(by="Average", ascending=False).head(5)` in `top_performers()` |

## 5.6 Step 5 – Final Output

`main.py` prints the results in eight clearly labelled sections with headings, so the output can be understood without reading the code. Screenshots of the output are given in Section 7.

---

# 6. Key Features

| # | Feature / Function | File | Description |
|---|---|---|---|
| 1 | `load_data()` | functions.py | Loads the CSV file into a Pandas DataFrame |
| 2 | `calculate_total()` | functions.py | Total marks of a student using `np.sum` |
| 3 | `calculate_average()` | functions.py | Average marks of a student using `np.mean` |
| 4 | `assign_grade()` | functions.py | Assigns grade by a clearly defined grading rule |
| 5 | `check_result()` | functions.py | Pass/Fail using `np.all` and the 40-mark condition |
| 6 | `process_students()` | functions.py | Loops over all students and adds Total, Average, Grade, Result |
| 7 | `overall_performance()` | functions.py | Finds highest, lowest and class average performance |
| 8 | `subject_analysis()` | functions.py | Subject-wise average, highest, lowest and pass count |
| 9 | `top_performers()` | functions.py | Returns the top-N students by average marks |
| 10 | `main.py` | main.py | Runs everything and displays the final analysis |

**Requirement coverage**

| Project requirement (from assignment) | Implemented in |
|---|---|
| Dataset with ID, Name, Department, subject marks, Attendance | `students.csv` |
| Load and organise data with Pandas DataFrame | `load_data()` |
| NumPy for numerical calculations | `np.sum`, `np.mean`, `np.max`, `np.min`, `np.all` |
| Reusable functions | `functions.py` |
| Loops where iteration is required | `process_students()`, `subject_analysis()`, ranking and grade printing in `main.py` |
| Total and average marks per student | `calculate_total()`, `calculate_average()` |
| Grades by a defined rule | `assign_grade()` |
| Pass/Fail by a defined condition | `check_result()` |
| Highest, lowest, average performance | `overall_performance()` |
| Subject-wise analysis | `subject_analysis()` |
| Top-performing students | `top_performers()` |

---

# 7. Output / Screenshots

### 7.1 Dataset Overview
Shows number of records, columns, first five rows and basic information.

![Dataset Overview](screenshots/01_dataset_overview.png)

### 7.2 Student Result Sheet
Total, average, grade and pass/fail result for each of the 20 students.

![Result Sheet](screenshots/02_result_sheet.png)

### 7.3 Overall Performance, Grade Distribution and Pass/Fail Statistics

![Overall Performance](screenshots/03_overall_grades_passfail.png)

### 7.4 Subject-wise Performance, Top 5 Students and Final Summary

![Subject Wise and Top Performers](screenshots/04_subjects_top5_summary.png)

---

# 8. Final Outcome

The project runs without errors and successfully analyses the data of all 20 students. The main results obtained are:

| Question | Result |
|---|---|
| Student with the highest average | Pooja Reddy (94.8) |
| Student with the lowest average | Rahul Joshi (42.0) |
| Overall class average | 71.83 |
| Average attendance | 83.35% |
| Students passed | 18 out of 20 (90%) |
| Students failed | 2 – Vikram Yadav and Rahul Joshi |
| Subject with the best average | English (74.95) |
| Subject with the lowest average | Chemistry (69.40) |
| Top 3 students | Pooja Reddy, Sneha Singh, Kavya Menon |

**Grade distribution:** A+ = 2, A = 7, B = 2, C = 3, D = 4, F = 2.

**What the project achieved**

- Converted raw marks data into meaningful information automatically.
- Implemented every required feature of the assignment: totals, averages, grades, pass/fail, highest/lowest/average performance, subject-wise analysis and top performers.
- Used functions, loops, NumPy and Pandas in a clean and reusable way.
- Produced an output that is easy to read and understand without opening the code.

---

# 9. Challenges & Learning

| Challenge | How it was solved | What was learned |
|---|---|---|
| Deciding the pass/fail condition | Defined a clear rule: at least 40 marks in every subject. This also catches students who have a high total but fail one subject. | A clear rule makes results fair and the code easy to explain. |
| Applying NumPy on each student's marks | Converted the subject columns of each row to a NumPy array with `.values.astype(int)`. | NumPy functions work easily on arrays and Pandas rows can be converted to arrays. |
| Keeping the code organised | Moved all calculations to `functions.py` and kept only the flow and printing in `main.py`. | Reusable functions make a project clean, readable and easy to test. |
| Getting subject-wise results | Used a loop over the subject list and NumPy functions on each column. | Loops reduce repeated code. Only the list of subjects needs to change to add a new subject. |
| Presenting readable output | Used section headings, formatted f-strings and `to_string(index=False)`. | Good output formatting is as important as correct calculation. |

**Overall learning:** This project gave practical experience of the complete data-analysis flow: loading data, processing it, analysing it and presenting the results, using Python, NumPy and Pandas.

---

# 10. GitHub Repository

**Repository link:** `<Paste your GitHub repository URL here>`

Example: `https://github.com/<your-username>/student-performance-analytics`
