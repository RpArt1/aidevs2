import json

from assigment_utils import AssigmentUtils
from tasks.abstractTask import AbstractTask


class ModerationTask(AbstractTask):
    # source: https://community.ahoy.so/c/lekcje-programu-cf0f7c/po-prostu-zrob-to-co-powiem

    TASK_NAME = 'moderation'
    MODERATION_API_URL = 'https://api.openai.com/v1/moderations'

    def solve_task(self):
        super().solve_task()

    def moderate_input(self, input_to_moderate: str):
        try:
            result = AssigmentUtils.process_request(ModerationTask.MODERATION_API_URL, 'POST', input_to_moderate)
            my_dict = json.loads(result.text)
            # print(f'moderate_input: {input} result: {my_dict["results"][0]["flagged"]}')
            return int(my_dict['results'][0]['flagged'])
        except Exception as e:
            print(f"Exception: An unexpected error occurred: {e}")
            return None

    def process_task_details(self):
        moderation_result = []
        i = 0
        while i <= len(self.assignment_body):
            entry_to_moderate = {"input": self.assignment_body['input'][i]}
            print(f"process_task_details => entry_to_moderate: {entry_to_moderate}")
            moderation_result.append(self.moderate_input(entry_to_moderate))
            i += 1
        return moderation_result
