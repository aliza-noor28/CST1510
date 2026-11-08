"""
RECORD CHECK  -  my version
===========================

Name  :  Aliza Noor
Lane  :  AI Data Science
Date  :  04/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd

# ==================================================================== LOAD
# 1. Read your data file with pd.read_csv(). Make your own CSV, header row
#    plus at least 5 data rows: label,value,limit (or your lane's own field
#    names - same shape, different words).

with open("data.csv", "w") as f:
    f.write("dataset_name,rows_loaded,row_expected\n")
    f.write("survey_2022,1050,1200\n")
    f.write("survey_2023,1290,1200\n")
    f.write("survey_2024,1064,1200\n")
    f.write("survey_2025,1230,1200\n")
    f.write("survey_2026,1187,1200\n")
df = pd.read_csv("data.csv")


# ================================================================= PROCESS
# 2. Add a "percent" column: (value / limit) * 100.
#
#    Typical and above: also add a "status" column using .apply() with a
#    lambda - "OVER LIMIT" (100%+), "WARNING" (90%+), otherwise "OK".

df["percent"] = ((df["rows_loaded"] / df["row_expected"]) * 100) .round(2)
df["status"] = df["percent"].apply(lambda x: "OVER LIMIT" if x >= 100 else "WARNING" if x >= 90 else "OK")


# ================================================================== OUTPUT
# 3. Print the DataFrame.
#
#    Threshold : print it as-is, with the percent column.
#    Typical   : also filter to show only the rows that are not "OK", using a
#                boolean condition in [] - not a loop.
#    Excellent : also group by "status" and print a count per group, save
#                the full DataFrame to a new CSV with .to_csv(), and save
#                one bar chart of the counts per status.

# Printing the DataFrame as it is, with the percent column
print(df)
print("-" * 65)

# Printing only the rows that are not "OK"
print(df[df["status"] != "OK"])
print("-" * 65)

# Grouping by "status" and printing a count per group
print(df.groupby("status").size())
print("-" * 65)

# Saving the counts per group to a CSV file
df.to_csv("data_report.csv", index = False)

# Saving a bar chart of the counts per status
import matplotlib.pyplot as plt
df.groupby("status").size().plot(kind="bar")
plt.title("Counts per Status")
plt.xlabel("Status")
plt.ylabel("Count")
plt.savefig("counts_per_status.png")
plt.tight_layout()
plt.show()


# ==========================================================================
# 4. Before you finish:
#    [ ] Run it and check the percent/status columns by hand for one row
#    [ ] Check you used & (not "and") if you combined more than one condition
#    [ ] Check every column your code refers to actually exists - watch case
