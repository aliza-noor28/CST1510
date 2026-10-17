"""
RECORD CHECK  -  my version
===========================

Name  :  Aliza Noor
Lane  :  AI Data Science
Date  :  14/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

# your function(s) go here
def check_record(value, limit):
    '''Return the difference and percentage of value relative to limit'''
    difference = value - limit
    percent = value / limit * 100
    if value > limit:
        status = "OVER LIMIT"
    else:
        status = "OK"
    return difference, percent, status

def print_report(label, value, limit, difference, percent, status):
    '''Print a full report using label, value, limit, difference, percent and status'''
    print("=" * 35)
    print(f"RECORD - {label}")
    print(f"Rows loaded   : {value:>10.2f}")
    print(f"Rows expected : {limit:>10.2f}")
    print(f"Difference    : {difference:>10.2f}")
    print(f"Percent       : {percent:>10.2f}%")
    print(f"Status        : {status:>10}")
    print("=" * 35)



# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.

def load_records(path):
    '''Loads records from a file and returns a list of dictionaries'''
    records = []
    try:
        with open(path, "r") as f:
            for line in f:
                line = line.strip()
                label, value, limit = line.split(",")
                records.append({"label": label, "value": float(value), "limit": float(limit)})
    except FileNotFoundError:
        print("File not found")
    return records

def write_results(path, results):
    with open(path, "w") as f:
        for result in results:
            f.write(f"{result['label']}, {result['status']}\n")

def print_results(path):
    with open(path, "r") as f:
        text = f.read()
        print(text)

# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

# your loop goes here

records = load_records("records_sample.txt")

over_count = 0
results = []

for record in records:
    difference, percent, status = check_record(record["value"], record["limit"])
    print_report(record["label"], record["value"], record["limit"], difference, percent, status)
    results.append({"label": record["label"], "status": status})
    if status == "OVER LIMIT":
        over_count += 1

print(f"Records over limit: {over_count} out of {len(records)}")

write_results("results.txt", results)
print_results("results.txt")

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
