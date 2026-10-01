
from pydantic import BaseModel,ConfigDict, Field

class Project(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=500)

class ProjectUpdate(BaseModel):      # to updateinput
    name: str | None = Field(default=None,min_length=1, max_length=100)
    description: str | None = Field(default=None,min_length=1, max_length=500)         #lets us send only field we want to update i.e it is not str default is none 

class ProjectResponse(BaseModel):     #defines what API return i.e output
    model_config = ConfigDict(extra="ignore") #ignore extra fiels which are not included in schema

    id: int
    name: str
    description: str    