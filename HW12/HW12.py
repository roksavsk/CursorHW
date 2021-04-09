# 1. Create a script with arguments:
#
# exp; required: false; default: min(exp)
# current_job_exp; required: false; default: max(current_job_exp)
# sex; required: false
# city; required: false
# position; required: false
# age; required: false
# path_to_source_files; required: true;
# destination_path; required: false; default: .
# destination_filename; required: false; default: f"2020_june_mini.csv".
# The script should read the .csv file and get the information based on your input and generate a new .csv
# file with that info
#
# Example of input:
# -exp 3 -sex female -position DevOps -city Kyiv --path_to_source_files . ...

import argparse
import csv

parser = argparse.ArgumentParser(description="Job list")

parser.add_argument("--exp", required=False, default="10", help="Experience")
parser.add_argument("--current_job_exp", required=False, default="0", help="Current job experience")
parser.add_argument("--sex", required=False, help="Sex")
parser.add_argument("--city", required=False, help="City")
parser.add_argument("--position", required=False, help="Position")
parser.add_argument("--age", required=False, help="Age")
parser.add_argument("--path_to_source_files", required=True, help="Path to source files")
parser.add_argument("--destination_path", required=False, default="", help="Destination path")
parser.add_argument("--destination_filename", required=False, default="2020_june_mini.csv", help="Destination filename")
args = parser.parse_args()

if args.sex is None:
    args.sex = ""
if args.city is None:
    args.city = ""
if args.position is None:
    args.position = ""
if args.age is None:
    args.age = ""

file_len = 0
open_path = args.path_to_source_files
with open(open_path, "r", encoding="utf8") as file:
    reader = csv.reader(file)
    for row in reader:
        if file_len == 0:
            header = row
        file_len += 1
new_el = [file_len, args.city, "", "", args.position, args.exp, args.current_job_exp, "", "", args.age, args.sex, "",
          "", "", "", "", "", ""]

new_path = args.destination_path
with open(new_path, "a", encoding="utf8") as file:
    writer = csv.writer(file)
    if args.destination_filename != "2020_june_mini.csv":
        writer.writerow(header)
        new_el[0] = 2
    writer.writerow(new_el)



# 2. Create a script with arguments:
#
# source_file_path; required: true;
# start_salary; required: false; help: starting point of salary;
# end_salary; required: false; help: the max point of salary;
# position; required: false; help: position role
# age; required: false; help: Age of person
# language; required: false; help; Programming language
#
# Based on this info generate a new report of average salary.