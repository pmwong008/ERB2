import csv


def safe_divide(a_str, b_str):
    try:
        if not a_str.strip() or not b_str.strip():
            return 'missing'

        a = float(a_str)
        b = float(b_str)

        if b == 0:
            return 'undefined'
        return round(a / b, 2)

    except ValueError:
        return 'error'


# Read input and prepare output
with open('data.csv', newline='') as infile:
    reader = csv.DictReader(infile)
    rows = []

    for row in reader:
        result = safe_divide(row.get('A', ''), row.get('B', ''))
        row['Division'] = result
        rows.append(row)

# Write output CSV
with open('data_with_division.csv', 'w', newline='') as outfile:
    fieldnames = ['A', 'B', 'Division']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)