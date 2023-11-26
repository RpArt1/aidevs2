import dotenv

from utils.assigment_utils import AssigmentUtils
import openai
from dotenv import load_dotenv


import os
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI


TASK_NAME = 'inprompt'
API_URL = 'https://api.openai.com/v1/chat/completions'

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

# Za pomocą modułu do weryfikacji zadań z API, pobierz bazę wiedzy dla zadania o nazwie „inprompt”,
# a następnie odpowiedz na pytanie umieszczone w polu ‘question’.
# Baza jest zbyt duża, aby użyć jej bezpośrednio w swoim zapytaniu.
# Musisz wymyślić dowolną metodę na jej przeszukiwanie na podstawie imienia osoby, której dotyczy pytanie zwracane przez API


def extract_name_from_question(question):
    # 1 from question extract name of person
    uppercase_words = []
    for word in question.split():
        if word[0].isupper():
            uppercase_words.append(word)
    if len(uppercase_words) > 1:
        raise Exception("More than one uppercase word in question")
    name = uppercase_words[0]
    special_chars = ",.! ?"
    for char in special_chars:
        name = name.replace(char, "")
    return name


def extract_entry_from_data(list, key):
    entries_with_key = [entry for entry in list if key in entry]
    if len(entries_with_key) == 0:
        raise Exception("No entry with name from question")
    elif len(entries_with_key) > 1:
        raise Exception("More than one entry with name from question")
    return entries_with_key[0]


def process_task_3_2():
    token = AssigmentUtils.get_key_for_assigment(TASK_NAME)
    task = AssigmentUtils.get_assigment(token)
    task_input = task['input']
    task_question = task['question']
    print(f'assigment_body: {task_input},\n question: {task_question}')

    name = extract_name_from_question(task_question)

    # 2 serch in list entry with name from #1

    entries_with_key = extract_entry_from_data(task_input, name)

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": entries_with_key},
            {"role": "user", "content": task_question}
        ]
    )
    result = completion['choices'][0]['message']['content']
    print(f'response: {result}')
    AssigmentUtils.post_assigment(token, result)
    return completion


def process_task_3_2_alternate_solution():
    """
        This is alternate solution to task 3.2, solveb by someone else in commuinity it uses langchain library to process task
        check https://github.com/hwchase17/langchain/blob/master/langchain/chains/retrieval_qa/prompt.py
    """
    token = AssigmentUtils.get_key_for_assigment(TASK_NAME)
    task = AssigmentUtils.get_assigment(token)

    # input jest zamieniany na wektory (z użyciem text-embedding-ada-002) i trafia do bazy wektorowej (Chroma, Pinecone etc)
    db = Chroma.from_texts(task['input'], OpenAIEmbeddings())
    retreiver = db.as_retriever()

    # Następnie tworzony jest chain do 'rozmowy z dokumentami', któremu można już zadawać pytania o dane zgromadzone w bazie wektorowej.
    # Chain wykonuje zapytanie do bazy wektorowej na bazie pytania z zadania, i to co dostanie z powrotem wrzuca w prompta do gpt.

    qa = RetrievalQA.from_chain_type(llm=OpenAI(), retriever=retreiver)
    answear = qa.run(task['question'])
    print(f'response: {answear}')


