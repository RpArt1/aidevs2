from tasks.task_5_liar import LiarTask
from tasks.task_6_inprompt import InpromptTask
from tasks.task_2_3_embeding import EmbeddingTask
from tasks.zadanie2_moderation import ModerationTask
from tasks.task_4_2_blogger import BloggerTask
import logging
from tasks.task_2_4_whisper import WhisperTask
from tasks.task_2_5_functions import FunctionsTask
from tasks.task_3_1_rodo import RodoTask
from tasks.task_3_2_scrapper import ScrapperTask
from tasks.task_3_3_whoami import WhoamiTask
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
    RODO = "rodo",
    SCRAPPER = "scraper",
    WHOAMI = "whoami"

TASKS_MAPPING = {
    TasksNames.MODERATION.value: ModerationTask,
    TasksNames.BLOGGER.value: BloggerTask,
    TasksNames.LIAR.value: LiarTask,
    TasksNames.INPROMPT.value: InpromptTask,
    TasksNames.EMBEDDING.value: EmbeddingTask,
    TasksNames.WHISPER.value: WhisperTask,
    TasksNames.FUNCTIONS.value: FunctionsTask,
    TasksNames.RODO.value: RodoTask,
    TasksNames.SCRAPPER.value: ScrapperTask,
    TasksNames.WHOAMI.value: WhoamiTask
}

def create_task_and_process(task_signature: str, send_to_aidevs: bool, mock: bool):
    task_class = TASKS_MAPPING.get(task_signature.lower())
    if task_class is None:
        print(f"No task found of that signature: [{task_signature}] => EXITING")
        return
    task = task_class(task_signature, send_to_aidevs, mock)
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
    create_task_and_process(TasksNames.WHOAMI.value, True, False)
    logging.info("###### closing program ########\n\n\n")
