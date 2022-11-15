import json
def format_data(data):
    with open("jsonDataFile.json", "w") as write_file:
        json.dump(data, write_file, indent=4)