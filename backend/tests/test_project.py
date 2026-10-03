from fastapi.testclient import TestClient
from app.main import app

client=TestClient(app)      #a test client that can send requests to your FastAPI application.  

#first test code
def test_get_projects():
    response = client.get("/projects")

    assert response.status_code==200   #assert-I expect the response status code to be 200.
    assert isinstance(response.json(), list)  #I expect the /projects response to contain a list of projects
    assert len(response.json()) > 0  #checking list is not empty

    projects = response.json()    
    print(projects)   #using pytest -s to run  bcoz of print

    for project in projects:
        assert "id" in project     #checking each project has id
        assert "name" in project    #name
        assert "description" in project   #descp

#get by id
def test_get_project_by_id():
    response=client.get("/project/4")    

    assert response.status_code ==200    

def test_get_project_not_found():

    response = client.get("/project/999")

    assert response.status_code == 404    

#post
def test_create_project(): 
    response=client.post("/projects",json={"name":"test post","description":"testing post for creating a project"})

    assert response.status_code ==201
    print(response.json())
    assert response.json()["id"] is not None
    assert response.json()["name"] == "test post"
#patch
def test_update_project():
    response =client.patch("/projects/12",json={"name":"patch project"})

    assert response.status_code ==200
    print(response.json())
    assert response.json()["name"]=="patch project"
    assert response.json()["description"] =="testing post for creating a project"

def test_update_project_not_found():

    response = client.patch( "/projects/999",json={"description": "Updated description"} )

    assert response.status_code == 404    

#delete
def test_delete_project():
    response=client.delete("/projects/26")

    assert response.status_code ==200
    assert response.json() ["message"]=="project deleted successfully"

def test_delete_id_not_found():   
    response=client.delete("/projects/111")

    assert response.status_code==404


#post validatiom
def test_create_project_invalid_data():
    response = client.post("/projects",json={"name": "Invalid Project"})

    assert response.status_code == 422    

#patch validation
def test_update_project_invalid_data():
    response = client.patch(
        "/projects/30",
        json={
            "name": 12
        }
    )

    assert response.status_code == 422