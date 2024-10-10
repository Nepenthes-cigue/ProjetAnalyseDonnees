import json
import os
import csv

file_path = os.path.join(os.path.dirname(__file__), 'data', 'hypotheses.json')

with open(file_path, 'r') as file:
    json_data = json.load(file)

csv_file_path = os.path.join(os.path.dirname(__file__), 'data', 'reponses.csv')

with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    etudiant_sums = {}

    next(csv_reader)  # Skip the header row
    for row in csv_reader:
        etudiant = row[0]
        if etudiant not in etudiant_sums:
            etudiant_sums[etudiant] = 0

        for i in range(1, len(row)):
            for key in json_data:
                for value in json_data[key]:
                    if value in row[i]:
                        etudiant_sums[etudiant] += json_data[key][value]


etudiant_results = {}

for etudiant in etudiant_sums:
    if etudiant_sums[etudiant] > 0:
        etudiant_results[etudiant] = {
            "result": "ASTRE",
        }
    elif etudiant_sums[etudiant] < 0:
        etudiant_results[etudiant] = {
            "result": "IPS",
        }
    else:
        etudiant_results[etudiant] = {
            "result": "HESITANT",
        }
    etudiant_results[etudiant]['score'] = etudiant_sums[etudiant]

output_file_path = os.path.join(os.path.dirname(__file__), 'data', 'etudiant_results.json')

with open(output_file_path, 'w') as output_file:
    json.dump(etudiant_results, output_file, indent=4)