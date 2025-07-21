import csv

# Open the original CSV
with open('data.csv', newline='') as infile:
    reader = csv.DictReader(infile)

    # Prepare output rows
    rows = []
    for row in reader:
        try:
            a = float(row['A'])
            b = float(row['B'])
            division = a / b if b != 0 else 'undefined'
        except ValueError:
            division = 'error'

        row['Division'] = division
        rows.append(row)

# Write new CSV with extra column
with open('data_with_division.csv', 'w', newline='') as outfile:
    fieldnames = ['A', 'B', 'Division']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)