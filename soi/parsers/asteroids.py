import csv

def get_asteroid_data(filename):
    data = []
    with open(filename, 'rb') as f:
        csv_data = csv.reader(f)
        for row in csv_data:
            data.append(row)
    return data

