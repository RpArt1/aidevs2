from tasks.task_5_liar import LiarTask
from tasks.task_6_inprompt import InpromptTask
from tasks.task_2_3_embeding import EmbeddingTask
from tasks.zadanie2_moderation import ModerationTask
from tasks.task_4_2_blogger import BloggerTask
import logging
from tasks.task_2_4_whisper import WhisperTask
from tasks.task_2_5_functions import FunctionsTask
import logging
from enum import Enum

class TasksNames(Enum):
    MODERATION = "moderation",
    BLOGGER = "blogger",
    LIAR = "liar",
    INPROMPT = "inprompt",
    EMBEDDING = "embedding",
    WHISPER = "whisper",
    FUNCTIONS = "functions"

def create_task_and_process(task_signature: str, send_to_aidevs: bool, mock: bool):
    match task_signature.lower():
        case TasksNames.MODERATION.value:
            task = ModerationTask(TasksNames.MODERATION.value, send_to_aidevs, mock)
        case TasksNames.BLOGGER.value:
            task = BloggerTask(TasksNames.BLOGGER.value, send_to_aidevs, mock)
        case TasksNames.LIAR.value:
            task = LiarTask(TasksNames.LIAR.value, send_to_aidevs, mock)
        case TasksNames.INPROMPT.value:
            task = InpromptTask(TasksNames.INPROMPT.value, send_to_aidevs, mock)
        case TasksNames.EMBEDDING.value:
            task = EmbeddingTask(TasksNames.EMBEDDING.value, send_to_aidevs, mock)
        case TasksNames.WHISPER.value:
            task = WhisperTask(TasksNames.WHISPER.value, send_to_aidevs, mock)
        case TasksNames.FUNCTIONS.value:
            task = FunctionsTask(TasksNames.FUNCTIONS.value, send_to_aidevs, mock)
        case _:
            print(f"No task found of that signature: [{task_signature}] => EXITING")
            return
    logging.debug(f"create_task_and_process, task with signature {task_signature} will be created and run")
    task.solve_task()


def set_up_logging():
    # Configure the logging system
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(module)s.%(funcName)s -  %(message)s',
        handlers=[
            logging.FileHandler('/var/log/aidevs/aidevs.log'),  # Save logs to a file
            logging.StreamHandler()  # Print logs to the console
        ]
    )


if __name__ == "__main__":
    set_up_logging()
    create_task_and_process(TasksNames.FUNCTIONS.value, False, False)
    logging.info("###### closing program ########\n\n\n")
