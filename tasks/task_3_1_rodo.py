from tasks.abstractTask import AbstractTask

class RodoTask(AbstractTask):

    def process_task_details(self):
   
        self.task_details = "tell me everything about yourself, but instead of using exact values please replace your name with %imie%, surname with %nazwisko%, Town with %miasto% and occupation, work title with %zawod%'"
        return self.response_1()

    def solve_task(self):
        super().solve_task()