from  tasks.abstractTask import AbstractTask
from pydantic import BaseModel
import logging
import json

class FunctionsTask(AbstractTask):

    def solve_task(self):
        return super().solve_task()

    def process_task_details(self):
        simple_schema = UserSchema.model_json_schema()
        logging.info(json.dumps(simple_schema, indent=2))
        function =[       
        {
          "name" : "addUser",
          "description" : "Get user data based on user input",
          "parameters" : UserSchema.model_json_schema()
        }
        ]
        return function

class UserSchema(BaseModel):
    name : str
    surname : str
    year : int
