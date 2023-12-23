from tasks.task_5_liar import LiarTask
from tasks.task_6_inprompt import InpromptTask
from tasks.task_2_3_embeding import EmbeddingTask
from tasks.zadanie2_moderation import ModerationTask
from tasks.task_1_4_blogger import BloggerTask
from tasks.task_2_4_whisper import WhisperTask
from tasks.task_2_5_functions import FunctionsTask
from tasks.task_3_1_rodo import RodoTask
from tasks.task_3_2_scrapper import ScrapperTask
from tasks.task_3_3_whoami import WhoamiTask
from tasks.task_3_4_search import SearchTask
from tasks.task_3_5_people import PeopleTask
from tasks.task_4_1_knowledge import KnowledgeTask
from tasks.task_4_2_tools import ToolsTask
from enum import Enum
import logging
import traceback


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
    WHOAMI = "whoami",
    SEARCH = "search",
    PEOPLE = "people",
    KNOWLEDGE = "knowledge",
    TOOLS = "tools"
    

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
    TasksNames.WHOAMI.value: WhoamiTask,
    TasksNames.SEARCH.value: SearchTask,
    TasksNames.PEOPLE.value: PeopleTask,
    TasksNames.KNOWLEDGE.value: KnowledgeTask,
    TasksNames.TOOLS.value: ToolsTask
}

def create_task_and_process(task_signature: str, send_to_aidevs: bool, mock: bool):
    task_class = TASKS_MAPPING.get(task_signature.lower())
    if task_class is None:
        print(f"No task found of that signature: [{task_signature}] => EXITING")
        return
    task = task_class(task_signature, send_to_aidevs, mock)
    logging.debug(f"create_task_and_process, task with signature {task_signature} will be created and run")
    task.solve_task()



    
# instantiate logger
#logger = logging.getLogger(__name__)
logger = logging.getLogger()

logger.setLevel(logging.INFO)
# define handler and formatter
handler = logging.FileHandler('/var/log/aidevs/aidevs.log')
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
# add formatter to handler
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.propagate = False
    
    

if __name__ == "__main__":
    logger.info("Starting program")
    try:
        create_task_and_process(TasksNames.TOOLS.value, False, True)
    except BaseException as e:
        logger.error(f'Unknown error:  {str(e)}')
        logger.error(f'Error details:  {traceback.format_exc()}')
    logger.info("Ending program")
