from tasks.task_5_liar import LiarTask
from tasks.task_6_inprompt import InpromptTask
from tasks.task_7_embeding import EmbeddingTask
from tasks.zadanie2_moderation import ModerationTask
from tasks.task_4_2_blogger import BloggerTask
import logging


def create_task_and_process(task_signature: str, send_to_aidevs: bool, mock: bool):
    match task_signature.lower():
        case "moderation":
            task = ModerationTask('moderation', send_to_aidevs, mock)
        case "blogger":
            task = BloggerTask('blogger', send_to_aidevs, mock)
        case "liar":
            task = LiarTask('liar', send_to_aidevs, mock)
        case "inprompt":
            task = InpromptTask('inprompt', send_to_aidevs, mock)
        case "embedding":
            task = EmbeddingTask('embedding', send_to_aidevs, mock)
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
    create_task_and_process("embedding", True, True)
    logging.info("###### closing program ########\n\n\n")
