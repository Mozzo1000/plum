import os
import json

def create_new_file(filename='plum.json'):
    if os.path.isfile('plum.json'):
        print("plum.json configuration file already exists in current directory. Please remove it before running --init again.")
    else:
        name = input('Project name: ')
        data = {'name': name, "dependency": "requirements.txt", "devDependency": "requirements-dev.txt"}
        data['scripts'] = []
        data['scripts'].append({
            'start': f'python3 {name}/main.py'
        })
        try:
            with open(filename, 'w') as json_file:
                json.dump(data, json_file)
        except:
            print("Failed to create config file")
        print(f'Config file {filename} created successfully!')

def get_config(option, filename='plum.json'):
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
        try:
            return data[option]
        except KeyError:
            return None

def config_exists(filename='plum.json'):
    if os.path.isfile(filename):
        return True
    else:
        return False