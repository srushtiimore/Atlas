
from fastapi import APIRouter
from app.schemas.project import project
from app.data.store import load_projects, save_projects

router = APIRouter()



@router.get("/projects/")
def projects_all():
    return load_projects()

#creating project schema and routing 
@router.post("/projects")
def create_project(project: project):
     projects = load_projects()

     new_project = project.model_dump()   #conerts pydantic obj into py dict
     new_project["id"] = len(projects) + 1   # adds id to project

     projects.append(new_project)        #adds it into the list
     save_projects(projects)            #saves this to the json

     return new_project

@router.get("/project/{id}")
def project_single(id:int):
    projects = load_projects()

    for project in projects:
        if project["id"] == id:
            return project

    return {"message": "Project not found"}
