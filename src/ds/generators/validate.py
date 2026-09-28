"""
VALIDATION SCRIPT
==================
Run this to check your exercise answers.
Usage: python validate.py

It imports your functions from exercises.py, runs them,
and compares output against expected results.
"""
import sys
import os

# Ensure we're in the right directory
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Check that data files exist
if not os.path.exists("data/users.csv"):
    print("ERROR: Data files not found!")
    print("Run 'python setup_data.py' first to create sample data.")
    sys.exit(1)

# Import student's exercises
try:
    from exercises import (
        count_up,
        read_lines,
        skip_empty,
        parse_csv,
        filter_by,
        get_active_user_names,
        transform_orders,
        get_all_orders_with_tax,
        total_order_amount,
        parse_log_line,
        filter_errors,
        get_error_messages,
        read_multiple_csv,
        sum_with_list,
        sum_with_generator,
        category_summary,
    )
except ImportError as e:
    print(f"ERROR: Could not import from exercises.py: {e}")
    sys.exit(1)


# ── Utilities ──────────────────────────────────────────────

passed = 0
failed = 0
skipped = 0
total = 13


def check(exercise_num, description, func, expected, compare_fn=None):
    """Run one check and report pass/fail."""
    global passed, failed, skipped

    print(f"\n{'─' * 55}")
    print(f"  Exercise {exercise_num}: {description}")
    print(f"{'─' * 55}")

    try:
        result = func()

        if result is None:
            print(f"  ⏭  SKIPPED (function returned None — not implemented yet)")
            skipped += 1
            return

        if compare_fn:
            success = compare_fn(result, expected)
        else:
            success = result == expected

        if success:
            print(f"  ✅ PASSED!")
            if isinstance(result, list) and len(result) <= 10:
                print(f"     Output: {result}")
            elif isinstance(result, dict):
                for k, v in result.items():
                    print(f"     {k}: {v}")
            else:
                result_str = str(result)
                if len(result_str) > 80:
                    result_str = result_str[:80] + "..."
                print(f"     Output: {result_str}")
            passed += 1
        else:
            print(f"  ❌ FAILED")
            print(f"     Expected: {expected}")
            result_str = str(result)
            if len(result_str) > 200:
                result_str = result_str[:200] + "..."
            print(f"     Got:      {result_str}")
            failed += 1

    except Exception as e:
        print(f"  💥 ERROR: {type(e).__name__}: {e}")
        failed += 1


# ── Exercise Checks ────────────────────────────────────────

# Exercise 1: count_up
def check_ex1():
    result = count_up(5)
    if result is None:
        return None
    result_list = list(result)
    return result_list


check(1, "Basic Generator - count_up(5)", check_ex1, [1, 2, 3, 4, 5])


# Exercise 2: read_lines
def check_ex2():
    result = read_lines("data/users.csv")
    if result is None:
        return None
    lines = list(result)
    # Should have header + 12 data rows (including empty ones) = 13 lines
    # Return first line to verify stripping works
    return lines[0]


check(2, "Read Lines Generator", check_ex2, "id,name,email,status,age")


# Exercise 3: skip_empty
def check_ex3():
    result = skip_empty(["hello", "", "  ", "world", "\n", "test"])
    if result is None:
        return None
    return list(result)


check(3, "Skip Empty Lines", check_ex3, ["hello", "world", "test"])


# Exercise 4: parse_csv
def check_ex4():
    lines = ["name,age,city", "Alice,30,NYC", "Bob,25,LA"]
    result = parse_csv(iter(lines))
    if result is None:
        return None
    return list(result)


check(
    4,
    "Parse CSV Generator",
    check_ex4,
    [
        {"name": "Alice", "age": "30", "city": "NYC"},
        {"name": "Bob", "age": "25", "city": "LA"},
    ],
)


# Exercise 5: filter_by
def check_ex5():
    records = [
        {"name": "Alice", "status": "active"},
        {"name": "Bob", "status": "inactive"},
        {"name": "Charlie", "status": "active"},
    ]
    result = filter_by(records, "status", "active")
    if result is None:
        return None
    return list(result)


check(
    5,
    "Filter by Field",
    check_ex5,
    [
        {"name": "Alice", "status": "active"},
        {"name": "Charlie", "status": "active"},
    ],
)


# Exercise 6: get_active_user_names
check(
    6,
    "Full Pipeline - Active Users",
    get_active_user_names,
    ["Alice", "Charlie", "Diana", "Frank", "Grace", "Ivy", "Jack"],
)


# Exercise 7: transform_orders
def check_ex7():
    records = [
        {
            "order_id": "101",
            "user_id": "1",
            "product": "Laptop",
            "amount": "999.99",
            "date": "2024-01-15",
        }
    ]
    result = transform_orders(records)
    if result is None:
        return None
    items = list(result)
    if not items:
        return []
    return items


def compare_ex7(result, expected):
    if len(result) != 1:
        return False
    r = result[0]
    return (
        r.get("order_id") == "101"
        and r.get("product") == "Laptop"
        and abs(r.get("amount", 0) - 999.99) < 0.01
        and abs(r.get("amount_with_tax", 0) - 1079.99) < 0.02
    )


check(
    7,
    "Transform Orders",
    check_ex7,
    "order_id=101, product=Laptop, amount=999.99, amount_with_tax=1079.99",
    compare_fn=compare_ex7,
)


# Exercise 8: get_all_orders_with_tax
def check_ex8():
    result = get_all_orders_with_tax()
    if result is None:
        return None
    if not isinstance(result, list):
        return result
    return len(result)


check(8, "Orders Pipeline (count of orders)", check_ex8, 10)


# Exercise 9: total_order_amount
def compare_float(result, expected):
    try:
        return abs(float(result) - float(expected)) < 0.02
    except (TypeError, ValueError):
        return False


check(
    9,
    "Aggregation - Total Order Amount",
    total_order_amount,
    2189.89,
    compare_fn=compare_float,
)


# Exercise 10: get_error_messages
def check_ex10():
    result = get_error_messages()
    if result is None:
        return None
    if not isinstance(result, list):
        return result
    # Verify all messages are strings and come from ERROR entries
    return all(isinstance(m, str) and len(m) > 0 for m in result)


check(10, "Log Parser - Error Messages", check_ex10, True)


# Exercise 11: read_multiple_csv
def check_ex11():
    result = read_multiple_csv(["data/users.csv", "data/orders.csv"])
    if result is None:
        return None
    records = list(result)
    # users.csv has 10 data rows, orders.csv has 10 data rows = 20 total
    return len(records)


check(11, "yield from - Multiple CSVs", check_ex11, 20)


# Exercise 12: sum comparison
def check_ex12():
    r1 = sum_with_list()
    r2 = sum_with_generator()
    if r1 is None or r2 is None:
        return None
    return r1 == r2 and isinstance(r1, int) and r1 > 0


check(12, "Generator vs List (same result)", check_ex12, True)


# Exercise 13: category_summary (Bonus)
def check_ex13():
    result = category_summary()
    if result is None:
        return None
    if not isinstance(result, dict):
        return None
    # Verify structure
    expected_categories = {"Electronics", "Stationery", "Furniture"}
    if set(result.keys()) != expected_categories:
        return result
    # Check Electronics
    elec = result["Electronics"]
    return elec.get("count") == 5


check(13, "BONUS: Category Summary", check_ex13, True)


# ── Final Report ───────────────────────────────────────────

print(f"\n{'═' * 55}")
print(f"  RESULTS")
print(f"{'═' * 55}")
print(f"  ✅ Passed:  {passed}/{total}")
print(f"  ❌ Failed:  {failed}/{total}")
print(f"  ⏭  Skipped: {skipped}/{total}")
print(f"{'═' * 55}")

if passed == total:
    print("\n  🎉 PERFECT SCORE! All exercises completed!")
    print("  You've mastered generator pipelines!")
elif passed >= 10:
    print("\n  🌟 Great work! Almost there!")
    print("  Review the failed exercises and try again.")
elif passed >= 6:
    print("\n  👍 Good progress! Keep going!")
    print("  The pipeline exercises build on earlier ones.")
elif passed > 0:
    print("\n  🚀 Good start! Work through them in order.")
    print("  Each exercise builds on the previous one.")
else:
    print("\n  💪 Start with Exercise 1 — it's the easiest!")
    print("  Work through them in order, they build up step by step.")

print()
