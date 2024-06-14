import csv


def read_test_data_from_csv(file_path):
    test_data = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            test_data.append(row)

    return test_data
