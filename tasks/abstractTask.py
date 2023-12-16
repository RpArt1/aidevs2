from abc import ABC, abstractmethod
from utils.assigment_utils import AssigmentUtils
import logging

class AbstractTask(ABC):

    GPT_MODEL = "gpt-3.5-turbo" # "gpt-4-1106-preview"  #

    def __init__(self, task_name, send_to_aidevs, mock):
        self.assignment_solution = None
        self.assignment_body = None
        self.task_name = task_name
        self.key = AssigmentUtils.get_key_for_assigment(self.task_name)
        self.send_to_aidevs = send_to_aidevs
        self.mock = mock
        logging.debug(f"Task created: {self.task_name} key for assignment {self.key}")

    @abstractmethod
    def process_task_details(self):
        """
        Each task has its own custom implementation
        Override this method with your own

        Returns repose in format which is required in task usually json
        -------

        """
        return

    def get_task_details(self):
        """
            Get task details from aidev and set it as class variable
        """
        assignment_body = AssigmentUtils.get_assigment(self.key)
        logging.info(f'assignment body: {assignment_body}')
        self.assignment_body = assignment_body

    def return_answer(self):
        """
        Send response to aidevs
        Returns None
        -------
        """
        logging.info(f'assignment solution: {self.assignment_solution}')
        response = AssigmentUtils.post_assigment(self.key, self.assignment_solution)
        logging.info(f"response from aidevs: {response}")

    @abstractmethod
    def solve_task(self):
        self.get_task_details()
        self.assignment_solution = self.process_task_details()
        if self.send_to_aidevs:
            logging.info("Sending answer to aidevs...")
            self.return_answer()
        else:
            logging.info("Won't send to aidevs... END")