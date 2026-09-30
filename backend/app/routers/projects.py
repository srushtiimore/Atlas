
from fastapi import APIRouter , HTTPException ,status    #HTTPEXCEPTION returns http errors- 404 not found 
from app.schemas.project import Project , ProjectUpdate,ProjectResponse
from app.data.store import load_projects, save_projects

router = APIRouter()

@router.get("/projects")
def projects_all():
    return load_projects()

#creating project schema and routing 
@router.post("/projects",response_model=ProjectResponse,status_code=status.HTTP_201_CREATED)
def create_project(project: Project):
     projects = load_projects()

     new_project = project.model_dump()      #conerts pydantic obj into py dict
     new_project["id"] = max((item["id"] for item in projects),default=0) + 1  # adds id to project based on max id +1, default- if no id exist
    
     projects.append(new_project)            #adds it into the list
     save_projects(projects)                 #saves this to the json

     return new_project

@router.get("/project/{id}")
def project_single(id:int):
    projects = load_projects()

    for project in projects:
        if project["id"] == id:
            return project

    raise HTTPException(
            status_code=404,
            detail="Project not found "
    )



@router.patch("/projects/{id}",response_model=ProjectResponse,status_code=status.HTTP_200_OK)
def update_project(id:int,updates:ProjectUpdate):  #updates-new info supplied in req body
    projects=load_projects()

    for project in projects:
        if project["id"]==id: 
            update_data=updates.model_dump(exclude_unset=True)  #exclude_unset=true -Include only the fields the client actually sent, rather than every field with its default value.
            project.update(update_data)

            save_projects(projects)
            return project

    raise HTTPException(
        status_code=404,
        detail="Project not found"
     )    

@router.delete("/projects/{id}",status_code=status.HTTP_200_OK)
def delete_project(id:int):
    projects=load_projects()

    for project in projects:
        if project["id"]==id:
            projects.remove(project)

            save_projects(projects)
            return {"message":"project deleted successfully"}
    
    raise HTTPException(
        status_code=404,
        detail="Project not found "
    )      

