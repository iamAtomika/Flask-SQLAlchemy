import csv

def load_data(filename):
    data = {}
    with open(filename, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data[row['name']] = row
    return data