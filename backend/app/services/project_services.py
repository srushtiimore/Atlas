
#handles project operations
from app.repositories import project_repository

def get_all_projects():
    return project_repository.get_all()


def get_project_by_id(project_id: int):
    return project_repository.get_by_id(project_id)


def create_project(project_data:dict):    ##project_data contains the info for the new project,dict indicates that we expect a Py dict
    projects=project_repository.get_all()

    new_id=max(project["id"] for project in projects)+1
    project_data["id"]=new_id
    projects.append(project_data)
    project_repository.save_all(projects)
    return project_data


def update_project(project_id:int,update_data:dict):
    projects=project_repository.get_all()

    for project in projects:
        if project["id"]==project_id:
            project.update(update_data)
            project_repository.save_all(projects)
            return project
        
    return None    

def delete_project(project_id:id):
    projects=project_repository.get_all()

    for project in projects:
        if project["id"]==project_id:
            projects.remove(project)
            project_repository.save_all(projects)
            return project

    return None    

