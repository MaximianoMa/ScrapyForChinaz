import json
import csv

# Open the JSON file for reading
with open('new.json', 'r') as json_file:
    # Load JSON content
    json_data = json.load(json_file)

    # Open a CSV file for writing
    with open('final111.csv', 'w', newline='') as csv_file:
        # Create a CSV writer object
        csv_writer = csv.writer(csv_file)

        # Assuming the JSON data is a list of dictionaries
        # Write headers (keys of the first dictionary in the list)
        headers = json_data[0].keys()
        csv_writer.writerow(headers)

        # Write data rows
        for item in json_data:
            csv_writer.writerow(item.values())
