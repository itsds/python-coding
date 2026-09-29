"""
================================================================================
VALIDATE.PY — Automated Output Checker
================================================================================
Usage (inside any question file):
    from validate import check
    check(result_df, "q01_below_avg_quarter")

This compares your PySpark DataFrame against the expected output CSV,
showing PASS/FAIL and a detailed diff if anything doesn't match.
================================================================================
"""
import os
import sys


def check(df, question_id):
    """
    Compare a PySpark DataFrame against the expected output CSV.

    Args:
        df: Your PySpark result DataFrame
        question_id: e.g. "q01_below_avg_quarter" (matches CSV filename)
    """
    from pyspark.sql import functions as F

    expected_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "expected_output",
        f"{question_id}.csv"
    )

    if not os.path.exists(expected_path):
        print(f"\n{'='*60}")
        print(f"  ERROR: Expected output file not found!")
        print(f"  Path: {expected_path}")
        print(f"{'='*60}\n")
        return False

    # Read expected output
    spark = df.sparkSession
    expected = spark.read.csv(expected_path, header=True, inferSchema=True)

    # Get column lists
    result_cols = sorted(df.columns)
    expected_cols = sorted(expected.columns)

    print(f"\n{'='*60}")
    print(f"  VALIDATING: {question_id}")
    print(f"{'='*60}")

    # Check 1: Column names match
    if result_cols != expected_cols:
        print(f"\n  FAIL — Column mismatch!")
        print(f"  Expected columns: {expected_cols}")
        print(f"  Your columns:     {result_cols}")
        missing = set(expected_cols) - set(result_cols)
        extra = set(result_cols) - set(expected_cols)
        if missing:
            print(f"  Missing: {missing}")
        if extra:
            print(f"  Extra:   {extra}")
        print(f"\n{'='*60}\n")
        return False

    # Check 2: Row count
    result_count = df.count()
    expected_count = expected.count()

    if result_count != expected_count:
        print(f"\n  FAIL — Row count mismatch!")
        print(f"  Expected: {expected_count} rows")
        print(f"  Yours:    {result_count} rows")
        if result_count < expected_count:
            print(f"  (You're missing {expected_count - result_count} rows)")
        else:
            print(f"  (You have {result_count - expected_count} extra rows)")
        print(f"\n{'='*60}\n")
        return False

    # Check 3: Data comparison
    # Cast all columns to string for reliable comparison, handle nulls
    select_cols = expected.columns

    def to_comparable(dataframe, label):
        """Convert DataFrame to sorted list of tuples for comparison."""
        rows = dataframe.select(*select_cols).collect()
        result = []
        for row in rows:
            # Round floats to 2 decimal places for comparison
            vals = []
            for v in row:
                if isinstance(v, float):
                    vals.append(round(v, 2))
                else:
                    vals.append(v)
            result.append(tuple(vals))
        return sorted(result)

    try:
        result_rows = to_comparable(df, "yours")
        expected_rows = to_comparable(expected, "expected")
    except Exception as e:
        print(f"\n  FAIL — Error during comparison: {e}")
        print(f"\n{'='*60}\n")
        return False

    if result_rows == expected_rows:
        print(f"\n  *** PASS ***")
        print(f"  {result_count} rows, {len(select_cols)} columns — all match!")
        print(f"\n{'='*60}\n")
        return True
    else:
        print(f"\n  FAIL — Data mismatch!")
        print(f"  Columns: {select_cols}")

        # Find and show differences (up to 10)
        mismatches = 0
        max_show = 10

        # Find rows in expected but not in result
        for row in expected_rows:
            if row not in result_rows:
                if mismatches < max_show:
                    if mismatches == 0:
                        print(f"\n  Rows in EXPECTED but missing from yours:")
                    print(f"    {row}")
                mismatches += 1

        # Find rows in result but not in expected
        extra_count = 0
        for row in result_rows:
            if row not in expected_rows:
                if extra_count < max_show:
                    if extra_count == 0:
                        print(f"\n  Rows in YOURS but not in expected:")
                    print(f"    {row}")
                extra_count += 1

        if mismatches > max_show:
            print(f"  ... and {mismatches - max_show} more missing rows")
        if extra_count > max_show:
            print(f"  ... and {extra_count - max_show} more extra rows")

        print(f"\n  TIP: Check your filtering, joins, and column calculations.")
        print(f"\n{'='*60}\n")
        return False
