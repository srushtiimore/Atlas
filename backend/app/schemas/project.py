
from pydantic import BaseModel,ConfigDict, Field, model_validator

class Project(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=500)

class ProjectUpdate(BaseModel):      # to updateinput
    name: str | None = Field(default=None,min_length=1, max_length=100)
    description: str | None = Field(default=None,min_length=1, max_length=500)         #lets us send only field we want to update i.e it is not str default is none 

    @model_validator(mode="after")
    def validate_update(self):
        if not self.model_fields_set:
            raise ValueError("At least one field must be provided")
        if "name" in self.model_fields_set and self.name is None:
            raise ValueError("Name cannot be null")
        if "description" in self.model_fields_set and self.description is None:
            raise ValueError("Description cannot be null")
        return self


class ProjectResponse(BaseModel):     #defines what API return i.e output
    model_config = ConfigDict(extra="ignore") #ignore extra fiels which are not included in schema

    id: int
    name: str
    description: str    