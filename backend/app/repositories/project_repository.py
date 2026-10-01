#for storing and retrieving the data

import json
from pathlib import Path    #find the location of store.json without hardcoding your entire file path.
DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "store.json"  #finds the path.found store.json


def get_all():
    with open(DATA_FILE, "r", encoding="utf-8") as file:     #reading store.json
        return json.load(file)


def save_all(projects):
    with open(DATA_FILE, "w", encoding="utf-8") as file:      #saving all updated projects
        json.dump(projects, file, indent=4)   #This converts the Python list into JSON and writes it into the file.


def get_by_id(project_id):     #Finding a project by ID
    projects = get_all()

    for project in projects:
        if project["id"] == project_id:
            return project

    return None