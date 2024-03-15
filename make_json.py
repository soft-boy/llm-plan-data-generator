import os
import json

def gen_x_json(directory='x_data'):
    data = {}
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                key = os.path.splitext(filename)[0]
                data[key] = file.read()

    # Sort the dictionary by key converted to integer
    sorted_data = {k: data[k] for k in sorted(data, key=lambda x: int(x))}

    with open('x_data.json', 'w', encoding='utf-8') as json_file:
        json.dump(sorted_data, json_file, ensure_ascii=False, indent=4)

def gen_y_json(directory='y_data'):
    data = {}
    for filename in os.listdir(directory):
        if filename.endswith('.py'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                key = os.path.splitext(filename)[0]
                data[key] = file.read()

    # Sort the dictionary by key converted to integer
    sorted_data = {k: data[k] for k in sorted(data, key=lambda x: int(x))}

    with open('y_data.json', 'w', encoding='utf-8') as json_file:
        json.dump(sorted_data, json_file, ensure_ascii=False, indent=4)

# Example usage
gen_x_json()
gen_y_json()
