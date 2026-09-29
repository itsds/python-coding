# PySpark Interview Practice Kit

12 hands-on PySpark coding problems covering the patterns most frequently asked in Data Engineering interviews. Solve them locally in PyCharm, then validate your output against expected results.

---

## Setup

### Prerequisites
- Python 3.8+
- Java 8 or 11 (required by Spark)
- PySpark (`pip install pyspark`)

### Quick Start
```bash
# 1. Install PySpark
pip install pyspark

# 2. Verify it works
python -c "from pyspark.sql import SparkSession; print('PySpark OK')"

# 3. Open the project in PyCharm and start with q01!
```

### PyCharm Configuration
1. Open this folder as a project in PyCharm
2. Set the Python interpreter (with PySpark installed)
3. Mark the project root as "Sources Root" (right-click folder → Mark Directory as → Sources Root) — this ensures `from validate import check` works
4. Run any question file directly (right-click → Run)

---

## Project Structure

```
pyspark-interview-practice/
├── data/                          ← Input CSVs
│   ├── employee.csv               (15 employees, with manager hierarchy)
│   ├── salary.csv                 (180 records, 2024-2025, with edge cases)
│   └── department.csv             (4 departments)
├── questions/                     ← YOUR workspace (solve here)
│   ├── q01_below_avg_quarter.py
│   ├── q02_top_earners_per_dept.py
│   ├── ...
│   └── q12_broadcast_salary_bands.py
├── solutions/                     ← Reference answers (peek if stuck)
│   ├── q01_below_avg_quarter_solution.py
│   ├── ...
│   └── q12_broadcast_salary_bands_solution.py
├── expected_output/               ← Ground-truth CSVs for validation
│   ├── q01_below_avg_quarter.csv
│   ├── ...
│   └── q12_broadcast_salary_bands.csv
├── validate.py                    ← PASS/FAIL checker
└── README.md                      ← You are here
```

---

## How to Solve

1. Open a question file in `questions/` (e.g., `q01_below_avg_quarter.py`)
2. Read the problem statement in the docstring
3. Write your PySpark code in the `YOUR CODE BELOW` section
4. Name your final DataFrame `result`
5. Uncomment the validation lines at the bottom and run:
   ```python
   from validate import check
   check(result, "q01_below_avg_quarter")
   ```
6. Fix until you see `*** PASS ***`

---

## The 12 Questions

| # | File | Pattern | Difficulty |
|---|------|---------|------------|
| 01 | `q01_below_avg_quarter` | GroupBy + Avg + Filter | Easy-Medium |
| 02 | `q02_top_earners_per_dept` | Window — dense_rank | Medium |
| 03 | `q03_month_over_month_change` | Window — lag() | Medium |
| 04 | `q04_cumulative_salary` | Window — running sum | Medium |
| 05 | `q05_earning_more_than_manager` | Self-Join | Medium |
| 06 | `q06_employees_with_no_salary` | Anti-Join (left_anti) | Easy |
| 07 | `q07_deduplicate_salary_records` | Deduplication (row_number) | Medium |
| 08 | `q08_pivot_quarterly_salary` | Pivot / Reshape | Medium |
| 09 | `q09_yoy_salary_growth` | YoY Comparison | Medium-Hard |
| 10 | `q10_salary_gap_detection` | Cross Join + Anti-Join | Medium-Hard |
| 11 | `q11_conditional_dept_stats` | Conditional Aggregation (F.when) | Medium |
| 12 | `q12_broadcast_salary_bands` | Broadcast Join + CASE WHEN | Medium |

### Recommended Order
- **Warm-up:** Q01, Q06
- **Core window functions:** Q02, Q03, Q04
- **Join patterns:** Q05, Q09
- **Data quality & reshaping:** Q07, Q08, Q10
- **Advanced aggregation:** Q11, Q12

---

## Edge Cases in the Data

The input data is deliberately seeded with edge cases you'll encounter in real interviews:

- **Employee 113 (Rohan Das)** — has ZERO salary records (tests anti-join, null handling)
- **Employee 107, Feb 2025** — has a DUPLICATE salary record (tests deduplication)
- **Employee 109 (Suresh Kumar)** — has NO manager (manager_id is null, CEO)
- **2025 data is partial** — only Q1 for 4 employees (tests YoY comparison)
- **Employee 103 earns more than their manager** — (tests self-join filtering)

---

## Data Schema

### employee.csv
| Column | Type | Description |
|--------|------|-------------|
| empid | Integer | Unique employee ID |
| name | String | Employee name |
| dob | String | Date of birth (YYYY-MM-DD) |
| department_id | Integer | FK to department.deptid |
| manager_id | Integer | FK to employee.empid (null for CEO) |

### salary.csv
| Column | Type | Description |
|--------|------|-------------|
| salid | Integer | Unique salary record ID |
| empid | Integer | FK to employee.empid |
| amount | Double | Salary amount |
| month | Integer | Month (1-12) |
| year | Integer | Year (2024 or 2025) |

### department.csv
| Column | Type | Description |
|--------|------|-------------|
| deptid | Integer | Unique department ID |
| dept_name | String | Department name |
| location | String | Office location |
