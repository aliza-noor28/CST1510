"""
RECORD CHECK  -  my version
===========================

Name  :  Aliza Noor
Lane  :  AI Data Science
Date  :  09/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write parse_line(raw_line) that cleans and parses one raw, messy line
#    into a dict. Handle inconsistent spacing and case - that is the whole
#    point of this week.
#
#    Typical and above: also write status_of(...), shaped for your lane
#    (e.g. OVER LIMIT / WARNING / OK, or FLAGGED / OK). Give both a
#    one-line docstring.

# your function(s) go here

def parse_line(raw_line):
    '''Turns a messy and raw line into a clean dictionary'''
    line = raw_line.strip()
    survey_part, rest = line.split(",", 1)
    survey = survey_part.strip().lower()

    record = {"survey": survey}
    for piece in rest.split(","):
        key, value = piece.split("=")
        record[key.strip().lower()] = float(value.strip())

    return record

def status_of(rating, age):
    '''Returns OVER LIMIT, WARNING or OK for a rating/age pair'''
    percent = (rating / age) * 100

    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


# ====================================================================== INPUT
# 2. Your raw, messy records - at least 5, deliberately varied in spacing
#    and case. Match the shape to your lane:
#
#    AI / Data Science : "  Survey_2026 , rating=4 , age=23  "
#    Cyber Security     : "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED"
#    IT                  : "  Srv-01 , used=87 , total=100  "
#
#    Excellent: save these lines to a file and load them with open() /
#    a for loop over the file, instead of writing them directly here.

with open("my_messy_lines.txt", "w") as f:
    f.write("  Survey_2026 , rating=60 , age=80  \n")
    f.write("  survey_2025,rating=45,age=50\n")
    f.write("SURVEY_2024 , rating = 40 , age = 75\n")
    f.write("sUrVeY_2023,rating=130,age=100\n")
    f.write("Survey_2022 , rating=171 , age=180  \n")
    

# =============================================================== PROCESS + OUTPUT
# 3. Parse and report on every record.
#
#    Threshold : parse each record, print the cleaned dict.
#    Typical   : also call status_of(...) for each, print it alongside.
#    Excellent : print a one-line summary at the end - how many records,
#                how many flagged.

total_count = 0
flagged_count = 0

with open("my_messy_lines.txt", "r") as f:
    for line in f:
        record = parse_line(line)
        record["status"] = status_of(record["rating"], record["age"])
        print(record)
        total_count += 1
        if record["status"] != "OK":
            flagged_count += 1
    
print()
print("----------**SUMMARY**----------")
print("There were total", total_count, "records out of which", flagged_count, "were flagged.")
print("-------------*****-------------")

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring
