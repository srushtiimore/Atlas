#Receives requests and returns HTTP responses
from fastapi import APIRouter , HTTPException ,status    #HTTPEXCEPTION returns http errors- 404 not found 

from app.schemas.project import Project , ProjectUpdate,ProjectResponse
from app.services import project_services

router = APIRouter()

@router.get("/projects")
def projects_all():
    return project_services.get_all_projects()

#creating project schema and routing 
@router.post("/projects",response_model=ProjectResponse,status_code=status.HTTP_201_CREATED)
def create_project(project: Project):
    new_project = project.model_dump()      #conerts pydantic obj into py dict
    return project_services.create_project(new_project)  #service call

@router.get("/project/{id}")
def project_single(id:int):
    project = project_services.get_project_by_id(id)    #service call 

    if project is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )

    return project

@router.patch("/projects/{id}",response_model=ProjectResponse,status_code=status.HTTP_200_OK)
def update_project(id:int,updates:ProjectUpdate):  #updates-new info supplied in req body
    update_data=updates.model_dump(exclude_unset=True)  #exclude_unset=true -Include only the fields the client actually sent, rather than every field with its default value.
    updated_project = project_services.update_project(id, update_data)    #service call

    if updated_project is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )

    return updated_project  

@router.delete("/projects/{id}",status_code=status.HTTP_200_OK)
def delete_project(id:int):
    deleted_project = project_services.delete_project(id)     #service call

    if deleted_project is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )

    return {"message": "project deleted successfully"}   

