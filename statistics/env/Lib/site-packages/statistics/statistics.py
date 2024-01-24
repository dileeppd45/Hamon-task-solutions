import csv
import argparse
from .statistics import main
from datetime import datetime

def read_csv(file_path):
    """Reads data from a CSV file and returns a list of dictionaries."""
    data = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data


def filter_data(data, country, from_date=None, to_date=None):
    """Filters data based on country and optional date range."""
    filtered_data = [row for row in data if row['Entity'] == country]

    if from_date:
        filtered_data = [row for row in filtered_data if
                         datetime.strptime(row['Year'], '%Y') >= datetime.strptime(from_date, '%Y')]
    if to_date:
        filtered_data = [row for row in filtered_data if
                         datetime.strptime(row['Year'], '%Y') <= datetime.strptime(to_date, '%Y')]

    return filtered_data


def calculate_statistics(data, operation='avg'):
    """Calculates statistics (avg, min, max) based on the specified operation."""
    if not data:
        raise ValueError("No data available for the specified country and date range.")

    values = [float(row['Unemployment, total (% of total labor force) (modeled ILO estimate)']) for row in data]

    if operation == 'avg':
        result = sum(values) / len(values)
    elif operation == 'min':
        result = min(values)
    elif operation == 'max':
        result = max(values)
    else:
        raise ValueError("Invalid operation. Use 'avg', 'min', or 'max'.")

    return result


def main():
    parser = argparse.ArgumentParser(description='Calculate unemployment rate statistics.')
    parser.add_argument('--country', required=True, help='The name of the country.')
    parser.add_argument('-o', '--operation', choices=['avg', 'min', 'max'], default='avg',
                        help='The operation to perform (avg, min, max).')
    parser.add_argument('--from', dest='from_date', help='Start date for the analysis.')
    parser.add_argument('--to', dest='to_date', help='End date for the analysis.')
    parser.add_argument('input_file', help='Path to the input CSV file.')

    args = parser.parse_args()

    # Read data from CSV file
    data = read_csv(args.input_file)

    # Filter data based on country and date range
    filtered_data = filter_data(data, args.country, args.from_date, args.to_date)

    # Calculate statistics
    result = calculate_statistics(filtered_data, args.operation)

    print(
        f"{args.operation.capitalize()} for {'/'.join(filter(None, [args.country, args.from_date, args.to_date]))}: {result}")


if __name__ == '__main__':
    main()