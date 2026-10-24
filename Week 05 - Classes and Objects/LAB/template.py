"""
RECORD CHECK  -  my version
===========================

Name  :  Aliza Noor
Lane  :  AI Data Science
Date  :  21/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
# 1. Define a class called Record.
#
#    Threshold : __init__(self, label, value, limit) storing all three as
#                attributes. No methods yet.
#    Typical   : add a method status(self) that returns "OVER LIMIT" (100%+),
#                "WARNING" (90%+) or "OK", worked out from self.value and
#                self.limit. Give it a one-line docstring.
#    Excellent : also add over_limit_count as a class-level running total -
#                see the note below.

# your class goes here

class Record:

    over_limit_count = 0

    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit
        if self.status() == "OVER LIMIT":
            Record.over_limit_count += 1

    def status(self):
        """Returns OVER LIMIT, WARNING or OK based on the value and limit"""
        percent = (self.value / self.limit) * 100
        if percent >= 100:
            result = "OVER LIMIT"
        elif percent >= 90:
            result = "WARNING"
        else:
            result = "OK"
        return result

# ==================================================================== RECORDS
# 2. Create your records.
#
#    Threshold : create at least 2 Record instances directly in the code.
#    Typical   : same, but now print each one's .status() as well.
#    Excellent : instead, write load_records(path) that reads label,value,limit
#                lines from a file and returns a list of Record objects. Make
#                your own data file, one record per line.

def load_records(path):
    records = []
    with open(path, "r") as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append(Record(label, float(value), float(limit)))
    return records

with open("Week 05 - Classes and Objects/LAB/my_records.txt", "w") as f:
    f.write("R-001,150,100\n")
    f.write("R-002,30,100\n")
    f.write("R-003,95,100\n")

records = load_records("Week 05 - Classes and Objects/LAB/my_records.txt")

# ==================================================================== OUTPUT
# 3. Print a report for each record.
#
#    Threshold : label, value, limit, inside a border.
#    Typical   : add the result of .status().
#    Excellent : also keep a running count of how many came back OVER LIMIT
#                across every record, and print that once, after the loop.
#                (Simplest: a plain variable outside the loop, same pattern
#                as Week 4. If you want it to live ON the object instead,
#                that is a stretch worth trying - but a variable is enough.)

print("=" * 34)
for record in records:
    status = record.status()

    if status == "OVER LIMIT":
        Record.over_limit_count += 1
    
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)
    print(f"Value  : {record.value}")
    print(f"Limit  : {record.limit}")
    print(f"Status : {status}")
    print("=" * 34)

print()
print(f"{Record.over_limit_count} records were over limit")
print()

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring
