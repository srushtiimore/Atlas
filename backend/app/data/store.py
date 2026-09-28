import json
from pathlib import Path


STORE_FILE = Path(__file__).parent / "store.json"    


def load_projects():                        #"Give me all the projects currently saved."
    with open(STORE_FILE, "r") as file:      #r=read
        return json.load(file)


def save_projects(projects):          #Take my projects and save them.
    with open(STORE_FILE, "w") as file:   #w=write
        json.dump(projects, file, indent=4)